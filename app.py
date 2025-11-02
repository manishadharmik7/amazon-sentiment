import streamlit as st
import joblib
import re, string

# Load model and vectorizer
tfidf = joblib.load('tfidf.pkl')
model = joblib.load('sentiment_model.pkl')

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    return text.strip()

st.title("🛒 Amazon Review Sentiment Analyzer")

review = st.text_area("Enter your product review:")
if st.button("Analyze"):
    clean_text = preprocess_text(review)
    vector = tfidf.transform([clean_text])
    pred = model.predict(vector)[0]
    sentiment = "😊 Positive" if pred == 1 else "😞 Negative"
    st.subheader(sentiment)
