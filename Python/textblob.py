from textblob import TextBlob

# Create a TextBlob object
text = "I love programming. It is very interesting and enjoyable!"
blob = TextBlob(text)

# Sentiment Analysis
print("Sentiment polarity:", blob.sentiment.polarity)
print("Sentiment subjectivity:", blob.sentiment.subjectivity)

# Noun Phrase Extraction
print("Noun phrases:", blob.noun_phrases)

# Word Tokenization
print("Words:", blob.words)

# Spelling Correction
wrong_text = TextBlob("I havv good speling!")
print("Corrected text:", wrong_text.correct())
