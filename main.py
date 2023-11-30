import streamlit as st
import plotly.express as px
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import glob
from pathlib import Path

filepath = glob.glob('diary/*.txt')
dates = []
for i in filepath:
    date = Path(i).stem
    dates.append(date)

positivity = []
negativity = []
for file in filepath:
    with open(file, 'r') as day:
        mood = day.read()
        analayser = SentimentIntensityAnalyzer()
        scores = analayser.polarity_scores(mood)
        print(scores)
        positivity.append(scores['pos'])
        negativity.append(scores['neg'])

st.title('Diary Tone')

st.subheader('Positivity')
figure1 = px.line(x=dates, y=positivity, labels={'x': 'Dates', 'y': 'Positivity'})
st.plotly_chart(figure1)

st.subheader('Negativity')
figure2 = px.line(x=dates, y=negativity, labels={'x': 'Dates', 'y': 'Negativity'})
st.plotly_chart(figure2)
