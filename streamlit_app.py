import streamlit as st
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

st.title("Welcome to app")

# Alusta NLTK:n sentimenttianalysaattori
nltk.download('vader_lexicon')  # Lataa sanakirja sentimenttianalyysiä varten
sia = SentimentIntensityAnalyzer()

# Määritä värit
positive_color = "#32CD32"  # Vihreä
negative_color = "#FF6347"  # Punainen

# Otsikko
st.title("Sentiment Analysis UI")

# Lomake syötteen ottamiseksi
user_input = st.text_input("Enter your sentence here:")

# Analysoi sentimentti, kun käyttäjä lähettää syötteen
if st.button("Submit"):
    sentiment_scores = sia.polarity_scores(user_input)
    sentiment = "Positive" if sentiment_scores["compound"] > 0 else "Negative"
    
    # Määritä väri sentimentin perusteella
    color = positive_color if sentiment == "Positive" else negative_color
    
    # Näytä tulos värillä
    st.write(f"Input: {user_input} - Sentiment: <span style='color:{color}'>{sentiment}</span>", unsafe_allow_html=True)