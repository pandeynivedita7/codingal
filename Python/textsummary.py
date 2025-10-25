#pip install tf-keras
#pip install torch gradio
import torch
import gradio as gr
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM


model_path=("snapshots\a4f8f3ea906ed274767e9906dbaede7531d660ff")
# Use summarization pipeline with PyTorch only
textsummary = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",
    torch_dtype=torch.bfloat16,
    framework="pt"
)

text='''Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and investor.
He is the founder, chairman, CEO, and CTO of SpaceX; angel investor, CEO, product architect,
and former chairman of Tesla, Inc.; owner, executive chairman, and CTO of X Corp.;
 founder of the Boring Company and xAI; co-founder of Neuralink and OpenAI; and president
 of the Musk Foundation. He is one of the wealthiest people in the world; as of April 2024,
 Forbes estimates his net worth to be $178 billion.[4]'''
# print(text_summary(text));"
print(textsummary(text))


# Load tokenizer and model (optional if you're using just pipeline)
#tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
#model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")
