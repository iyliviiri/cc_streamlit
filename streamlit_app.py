import streamlit as st
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['sentenceInput']
    sentiment = analyze_sentiment(text)
    return render_template('result.html', text=text, sentiment=sentiment)

def analyze_sentiment(text):
    # Tässä voit lisätä koodin sentimenttianalyysin suorittamiseksi
    # Esimerkiksi käyttämällä NLTK:n tai TextBlobin sentimenttianalyysityökaluja
    # Palauta tulokset sentimenttianalyysista, esim. "positive" tai "negative"
    # Tässä esimerkissä palautetaan satunnainen tulos vain demonstrointitarkoituksessa
    import random
    return random.choice(['positive', 'negative'])

if __name__ == '__main__':
    app.run(debug=True)