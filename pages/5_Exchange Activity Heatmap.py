import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.title("Exchange Heatmap over Time")
st.subheader("", divider='grey')
st.text('Using colour and shade to detect hottest Exchanges over periods in minutes.\nThis plots the number of Orders Acknowledged.')

with open("./datafiles/Exchange_1.json", "r") as file:
    data1 = json.load(file)

with open("./datafiles/Exchange_2.json", "r") as file:
    data2 = json.load(file)

with open("./datafiles/Exchange_3.json", "r") as file:
    data3 = json.load(file)

json_data = data1 + data2 + data3

df = pd.DataFrame(json_data)
df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])
df['Minute'] = df['TimeStamp'].dt.minute

heatmap_data = df.pivot_table(index='Exchange', columns='Minute', aggfunc='size', fill_value=0)

plot = plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", fmt='g', linewidths=.5)
plt.title('Exchange Activity Heatmap')
plt.xlabel('Minute')
plt.ylabel('Exchange')
st.pyplot(plot.get_figure())