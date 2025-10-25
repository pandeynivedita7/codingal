import torch
import gradio as gr
import pandas as pd
from transformers import pipeline

analyzer = pipeline("text-classification",
                    model="distilbert-base-uncased-finetuned-sst-2-english")

# print(analyzer(["This production is good", "This product was quite expensive"]))

def sentiment_analyzer(review):
    sentiment = analyzer(review)
    return sentiment[0]['label']

def read_reviews_and_analyze_sentiment(excel_path):
    # Load the Excel file into a DataFrame
    df = pd.read_excel(excel_path)

    # Check if 'Review' column is in the DataFrame
    if 'Reviews' not in df.columns:
        raise ValueError("Excel file must contain a 'Review' column.")

    # Apply the get_sentiment function to each review in the DataFrame
    df['Sentiment'] = df['Reviews'].apply(sentiment_analyzer)
   
    return df

result = read_reviews_and_analyze_sentiment("sentimentalanalyser\reviews.xlsx")
print(result)


demo=gr.Interface( fn=sentiment_analyzer,
                  inputs=[gr.Textbox(label="Input your review comment",lines=4)],
                  outputs=[gr.Textbox(label="Sentiment",lines=1)],
                  title="@GenerativeAIproject",
                  description="This application of sentiment based analyzer"
                  )

demo.launch()