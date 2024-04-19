import streamlit as st
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize NLTK's sentiment analyzer
nltk.download('vader_lexicon')  # Download dictionary for sentiment analysis
sia = SentimentIntensityAnalyzer()

# Assign colors to the response
positive_color = "#32CD32"  # green
negative_color = "#FF6347"  # red

# Title
st.title("Sentiment Analysis UI")

# Form to take input
user_input = st.text_input("Enter your sentence here:")

# Analyze the sentiment when a user submits a feed
if st.button("Submit"):
    sentiment_scores = sia.polarity_scores(user_input)
    sentiment = "Positive" if sentiment_scores["compound"] > 0 else "Negative"
    
    # Define color based on sentiment
    color = positive_color if sentiment == "Positive" else negative_color
    
    # Display the result in color
    st.write(f"Input: {user_input} - Sentiment: <span style='color:{color}'>{sentiment}</span>", unsafe_allow_html=True)