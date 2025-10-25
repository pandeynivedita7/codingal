# yt_summarizer_with_whisper_fallback.py
import os
import re
import tempfile
import subprocess
import shutil
from pathlib import Path
import torch
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from transformers import pipeline
import gradio as gr

# Optional/accelerated transcriber
try:
    from faster_whisper import WhisperModel
    _WHISPER_IMPL = "faster"
except Exception:
    try:
        import whisper
        _WHISPER_IMPL = "openai"
    except Exception:
        _WHISPER_IMPL = None

# Device setup
CUDA = torch.cuda.is_available()
TRANSFORMER_DEVICE = 0 if CUDA else -1
WHISPER_DEVICE = "cuda" if CUDA else "cpu"

# Summarizer pipeline
SUMMARIZER = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",
    framework="pt",
    from_pt=True,
    torch_dtype=torch.float32
)

# ---------- Utilities ----------
def extract_video_id(url: str) -> str | None:
    regex = (
        r"(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)"
        r"([a-zA-Z0-9_-]{11})"
    )
    m = re.search(regex, url)
    return m.group(1) if m else None

def seconds_to_timestamp(s: float) -> str:
    s = int(s)
    h, r = divmod(s, 3600)
    m, sec = divmod(r, 60)
    if h:
        return f"{h:02d}:{m:02d}:{sec:02d}"
    return f"{m:02d}:{sec:02d}"

def run_ffmpeg_to_wav(src_path: str, dst_path: str) -> None:
    cmd = ["ffmpeg", "-y", "-i", src_path, "-ar", "16000", "-ac", "1", dst_path]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# ---------- Transcription (YouTube captions first, Whisper fallback) ----------
def get_captions_segments(video_id: str):
    raw = YouTubeTranscriptApi.get_transcript(video_id)
    segments = []
    for item in raw:
        text = item.get("text", "").strip()
        start = float(item.get("start", 0.0))
        if text:
            segments.append({"start": start, "text": text})
    return segments

def download_audio(video_url: str, tmpdir: str) -> str:
    import yt_dlp
    outtmpl = os.path.join(tmpdir, "%(id)s.%(ext)s")
    ydl_opts = {"format": "bestaudio/best", "outtmpl": outtmpl, "quiet": True, "no_warnings": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
    filename = os.path.join(tmpdir, f"{info['id']}.{info.get('ext','m4a')}")
    return filename

def transcribe_with_whisper(audio_path: str, model_size: str = "small"):
    if _WHISPER_IMPL == "faster":
        # CHANGED THIS LINE: The original line was causing the error.
        # It's now changed to "float32" to ensure compatibility with all hardware.
        model = WhisperModel(model_size, device=WHISPER_DEVICE, compute_type="float32")
        segments, _ = model.transcribe(audio_path, beam_size=5)
        segs = []
        for seg in segments:
            segs.append({"start": float(seg.start), "text": seg.text.strip()})
        return segs
    elif _WHISPER_IMPL == "openai":
        import whisper
        model = whisper.load_model(model_size, device=WHISPER_DEVICE)
        res = model.transcribe(audio_path)
        segs = []
        for s in res.get("segments", []):
            segs.append({"start": float(s["start"]), "text": s["text"].strip()})
        return segs
    else:
        raise RuntimeError("No whisper implementation available. Install 'faster-whisper' or 'openai-whisper'.")

def get_transcript_segments(video_url: str, whisper_model_size: str = "small"):
    vid = extract_video_id(video_url)
    if not vid:
        raise ValueError("Could not extract video ID from URL.")
    # Try YouTube captions first
    try:
        return get_captions_segments(vid)
    except Exception:
        # Fallback to audio -> whisper
        tmpdir = tempfile.mkdtemp(prefix="yt_audio_")
        try:
            audio_file = download_audio(video_url, tmpdir)
            wav_path = os.path.join(tmpdir, Path(audio_file).stem + ".wav")
            run_ffmpeg_to_wav(audio_file, wav_path)
            segments = transcribe_with_whisper(wav_path, model_size=whisper_model_size)
            return segments
        finally:
            shutil.rmtree(tmpdir, ignore_errors=True)

# ---------- Chunking and summarization ----------
def make_chunks_from_segments(segments, max_chars=2800):
    chunks = []
    cur_text = ""
    cur_start = None
    for seg in segments:
        t = seg["text"]
        s = seg["start"]
        if cur_start is None:
            cur_start = s
        if len(cur_text) + len(t) + 1 <= max_chars:
            cur_text = (cur_text + " " + t).strip() if cur_text else t
        else:
            chunks.append({"start": cur_start, "text": cur_text})
            cur_text = t
            cur_start = s
    if cur_text:
        chunks.append({"start": cur_start, "text": cur_text})
    return chunks

def summarize_text(text: str):
    # short and robust wrapper
    out = SUMMARIZER(text, max_length=130, min_length=30, do_sample=False)
    return out[0]["summary_text"]

def summarize_video_url(video_url: str, whisper_model_size: str = "small"):
    vid = extract_video_id(video_url)
    if not vid:
        return "Error: invalid YouTube URL."

    try:
        segments = get_transcript_segments(video_url, whisper_model_size=whisper_model_size)
        if not segments:
            return "No transcript / transcription empty."
        chunks = make_chunks_from_segments(segments, max_chars=2800)
        chunk_summaries = []
        bullets = []
        for c in chunks:
            s = summarize_text(c["text"])
            chunk_summaries.append(s)
            ts = seconds_to_timestamp(c["start"])
            link = f"https://youtu.be/{vid}?t={int(c['start'])}"
            bullets.append(f"[{ts}] {s} — {link}")

        # Final consolidation
        joined = " ".join(chunk_summaries)
        if len(joined) > 2500:
            final = summarize_text(joined)
        else:
            final = joined

        result = "FINAL SUMMARY:\n" + final + "\n\nSEGMENTED (timestamped):\n" + "\n\n".join(bullets)
        return result
    except Exception as e:
        return f"Error during processing: {e}"

# ---------- Gradio UI ----------
def entry_point(url: str, whisper_model_size: str = "small"):
    return summarize_video_url(url.strip(), whisper_model_size=whisper_model_size)

gr.close_all()
demo = gr.Interface(
    fn=entry_point,
    inputs=[
        gr.Textbox(label="YouTube URL", lines=1, placeholder="https://youtu.be/XXXX"),
        gr.Dropdown(label="Whisper model (fallback)", choices=["tiny","base","small","medium","large"], value="small")
    ],
    outputs=gr.Textbox(label="Summary and timestamps", lines=15),
    title="YouTube Summarizer with Whisper fallback",
    description="Tries captions first. If none, downloads audio and uses Whisper to transcribe then summarize."
)

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7861, inbrowser=True, share=False)