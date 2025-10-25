import torch
import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline

# Load Hugging Face sentiment analysis pipeline
analyzer = pipeline(
    "text-classification",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

def sentiment_analyzer(review):
    """Run HuggingFace pipeline on a single review"""
    sentiment = analyzer(review)
    return sentiment[0]['label']

def sentiment_chart(df):
    """Generate pie chart of sentiment distribution"""
    sentiment_counts = df['Sentiment'].value_counts()
    fig, ax = plt.subplots()
    sentiment_counts.plot(
        kind='pie',
        ax=ax,
        autopct='%1.1f%%',
        colors=['green', 'red']
    )
    ax.set_ylabel('')  
    ax.set_title('Review Sentiment Distribution')
    return fig

def read_reviews_and_analyze_sentiment(file_object):
    """Read CSV/XLSX, analyze sentiments, return df and chart"""
    file_name = str(file_object.name).lower()

    if file_name.endswith(".csv"):
        df = pd.read_csv(file_object)
    elif file_name.endswith(".xlsx"):
        df = pd.read_excel(file_object)
    else:
        raise ValueError("Unsupported file format. Please upload CSV or XLSX.")

    # Normalize column names
    df.columns = df.columns.str.strip().str.lower()

    if 'reviews' not in df.columns:
        raise ValueError("File must contain a 'Reviews' column.")

    # Sentiment analysis
    df['Sentiment'] = df['reviews'].apply(sentiment_analyzer)

    # Chart
    chart_object = sentiment_chart(df)

    return df, chart_object

# Gradio interface
demo = gr.Interface(
    fn=read_reviews_and_analyze_sentiment,
    inputs=[gr.File(type="file", file_types=[".csv", ".xlsx"], label="Upload your review file")],
    outputs=[
        gr.Dataframe(label="Sentiments"),
        gr.Plot(label="Sentiment Analysis")
    ],
    title="@GenAILearniverse Project 3: Sentiment Analyzer",
    description="Upload a CSV or Excel file containing a 'Reviews' column to analyze sentiment."
)

if __name__ == "__main__":
    demo.launch()
