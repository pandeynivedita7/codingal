import torch
import gradio as gr
from transformers import pipeline



# Correct usage of pipeline
text_summary = pipeline(
    "summarization",
    model=r"C:\Users\swapn\Downloads\codingal\CodingalGit\codingal\Python\models--sshleifer--distilbart-cnn-12-6\snapshots\a4f8f3ea906ed274767e9906dbaede7531d660ff",
    torch_dtype=torch.bfloat16,
    framework="pt")
# Summarization function
def summary(input):
    output = text_summary(input)
    return output[0]['summary_text']

# Close previous Gradio sessions if any
gr.close_all()

# Launch Gradio interface
demo = gr.Interface(
    fn=summary,
    inputs=[gr.Textbox(label="Input text to summarize", lines=6)],
    outputs=[gr.Textbox(label="Summarized text", lines=4)],
    title="@GenAILearniverse Project 1: Text Summarizer",
    description="THIS APPLICATION WILL BE USED TO SUMMARIZE THE TEXT"
)

demo.launch()
