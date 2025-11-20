# twitter_rnn.py

import nltk
import re
import pickle
import numpy as np
import tensorflow as tf

from nltk.corpus import twitter_samples, stopwords
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

# -----------------------------------------
# 1️⃣ Download NLTK Data
# -----------------------------------------
nltk.download('twitter_samples')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# -----------------------------------------
# 2️⃣ Load Twitter Dataset
# -----------------------------------------
positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')

tweets = positive_tweets + negative_tweets
labels = [1] * len(positive_tweets) + [0] * len(negative_tweets)

# -----------------------------------------
# 3️⃣ Cleaning Function
# -----------------------------------------
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_tweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub(r"http\S+|www\S+|https\S+", "", tweet)  # remove URLs
    tweet = re.sub(r"@\w+", "", tweet)  # remove mentions
    tweet = re.sub(r"[^a-zA-Z\s]", "", tweet)  # remove punctuation & numbers
    tokens = nltk.word_tokenize(tweet)
    tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words]
    return " ".join(tokens)

cleaned_tweets = [clean_tweet(t) for t in tweets]

# -----------------------------------------
# 4️⃣ Tokenization & Padding
# -----------------------------------------
tokenizer = Tokenizer(num_words=10000, oov_token="<OOV>")
tokenizer.fit_on_texts(cleaned_tweets)

sequences = tokenizer.texts_to_sequences(cleaned_tweets)
padded = pad_sequences(sequences, maxlen=40, padding='post')

X = padded
y = np.array(labels)

# -----------------------------------------
# 5️⃣ Train Test Split
# -----------------------------------------
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------------------
# 6️⃣ Build RNN Model
# -----------------------------------------
model = Sequential([
    Embedding(10000, 64, input_length=40),
    SimpleRNN(64),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

model.summary()

# -----------------------------------------
# 7️⃣ Train Model
# -----------------------------------------
model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=5,
    batch_size=64,
    verbose=1
)

# -----------------------------------------
# 8️⃣ Evaluation
# -----------------------------------------
loss, acc = model.evaluate(X_test, y_test)
print(f"Twitter Test Accuracy: {acc * 100:.2f}%")

# -----------------------------------------
# 9️⃣ Prediction Example
# -----------------------------------------
def predict_tweet(tweet):
    cleaned = clean_tweet(tweet)
    seq = tokenizer.texts_to_sequences([cleaned])
    pad = pad_sequences(seq, maxlen=40)
    pred = model.predict(pad)[0][0]
    return "Positive 😀" if pred > 0.5 else "Negative 😞"

print(predict_tweet("I love this! Amazing work"))
print(predict_tweet("This is the worst day ever"))

# -----------------------------------------
# 🔟 Save Model & Tokenizer
# -----------------------------------------
model.save("twitter_sentiment_rnn.h5")

with open("twitter_tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

print("Twitter RNN model saved successfully!")
