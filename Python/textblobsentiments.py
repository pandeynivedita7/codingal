from textblob import TextBlob

# Input text
text = "HI i am happy ice cream !?"

# Create a TextBlob object
blob = TextBlob(text)

# Sentiment analysis
print("Sentiment Analysis:")
print(f"  Polarity: {blob.sentiment.polarity}")
print(f"  Subjectivity: {blob.sentiment.subjectivity}")

# Noun Phrases
print("\nNoun Phrases:")
print(blob.noun_phrases)

# Part-of-speech tagging
print("\nPart-of-Speech Tags:")
for word, tag in blob.tags:
    print(f"  {word}: {tag}")
