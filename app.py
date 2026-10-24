from pathlib import Path
import streamlit as st
import joblib

# Get the folder where app.py is located
BASE_DIR = Path(__file__).resolve().parent

# Load model and vectorizer
model = joblib.load(BASE_DIR / "Fake news model.pkl")
tfidf = joblib.load(BASE_DIR / "TFIDF vectorizer.pkl")
# Page settings
st.set_page_config(page_title="Fake News Detector")

st.title("📰 Fake News Detection")
st.write("Enter a news article to classify it as Fake or Real.")

# User input
news_text = st.text_area("Enter news article:")

if st.button("Predict"):
    if news_text.strip() == "":
        st.warning("Please enter a news article first.")
    else:
        news_tfidf = tfidf.transform([news_text])
        prediction = model.predict(news_tfidf)

        if prediction[0] == 0:
            st.error("Prediction: Fake News")
        else:
            st.success("Prediction: Real News")

st.caption(
    "This model predicts based on patterns learned from its training data. "
    "It does not independently verify whether a news article is true."
)