pip install matplotlib.pyplot
pip install plotly
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
# buat title
st.write('### Tokopedia sentiment analysis')

# input dataframe 
df = pd.read_csv('tokopedia_sentiment_analysis_clean.csv').reset_index(drop=True)
st.dataframe(df,use_container_width=True)

fig, ax = plt.subplots(figsize = (2, 2))
sizes = [count for count in df['sentiment'].value_counts()]
labels = list(df['sentiment'].value_counts().index)
explode = (0.1, 0, 0)
ax.pie(x = sizes, labels = labels, autopct = '%1.1f%%', explode = explode, textprops={'fontsize': 4})
ax.set_title('Distribution of Sentimen in Tokopedia tweet', fontsize = 8)
st.pyplot(fig)
