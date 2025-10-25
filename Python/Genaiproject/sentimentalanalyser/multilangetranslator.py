import torch
import gradio as gr
import json
import os
from transformers import pipeline

# Absolute path to your local model
model_path = (r"C:\Users\swapn\.cache\huggingface\hub\models--facebook--nllb-200-distilled-600M"
              r"\snapshots\f8d333a098d19b4fd9a8b18f94170487ad3f821d")

# Load model
text_translator = pipeline(
    "translation",
    model=model_path,   # local model path
    torch_dtype=torch.bfloat16
)

# JSON file path
json_file = "language.json"

# If language.json does not exist, create it with required codes
if not os.path.exists(json_file):
    default_languages = [
        {"Language": "German", "FLORES-200 code": "deu_Latn"},
        {"Language": "French", "FLORES-200 code": "fra_Latn"},
        {"Language": "Hindi", "FLORES-200 code": "hin_Deva"},
        {"Language": "Romanian", "FLORES-200 code": "ron_Latn"}
    ]
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(default_languages, f, indent=4, ensure_ascii=False)

# Load JSON mapping
with open(json_file, 'r', encoding="utf-8") as file:
    language_data = json.load(file)

def get_FLORES_code_from_language(language):
    for entry in language_data:
        if entry['Language'].lower() == language.lower():
            return entry['FLORES-200 code']
    return None

def translate_text(text, destination_language):
    dest_code = get_FLORES_code_from_language(destination_language)
    if dest_code is None:
        return f"Language '{destination_language}' not found in JSON"
    translation = text_translator(
        text,
        src_lang="eng_Latn",
        tgt_lang=dest_code
    )
    return translation[0]["translation_text"]

# Build Gradio interface
gr.close_all()
demo = gr.Interface(
    fn=translate_text,
    inputs=[
        gr.Textbox(label="Input text to translate", lines=6),
        gr.Dropdown(["German", "French", "Hindi", "Romanian"], label="Select Destination Language")
    ],
    outputs=[gr.Textbox(label="Translated text", lines=4)],
    title="@GenAILearniverse Project 4: Multi language translator",
    description="Translate any English text to multiple languages."
)
demo.launch()