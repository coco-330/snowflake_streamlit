import streamlit as st
from io import BytesIO
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


df = pd.read_csv('mercari_shops_transaction_data.csv')
# Generate the text for word cloud
text = " ".join(df['item_name'].astype(str))

wc = WordCloud(width=800, height=400, background_color="white").generate(text)
fig, ax = plt.subplots(figsize=(10, 5))
ax.axis("off")
st.title("Hot items Word Cloud")
st.image(wc.to_array())