import json
import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Multi-dimensional Models")
st.subheader('Exchange vs Price vs Time', divider='grey')
st.text('Some models can be most useful in 3D, try this one to see if there are any anomalies.')

with open("./datafiles/Exchange_1.json", "r") as file:
    data1 = json.load(file)

with open("./datafiles/Exchange_2.json", "r") as file:
    data2 = json.load(file)

with open("./datafiles/Exchange_3.json", "r") as file:
    data3 = json.load(file)

data = data1 + data2 + data3

df = pd.DataFrame(data)
df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])
df = df[df['MessageType'] == 'NewOrderAcknowledged']

df['TimeStamp_minutes'] = df['TimeStamp'].dt.minute

fig = px.scatter_3d(df, x='TimeStamp_minutes', y='OrderPrice', z='Exchange', title='3D Scatter Plot with Streamlit',
                 labels={'TimeStamp_minutes': 'Time (minutes)', 'OrderPrice': 'Order Price', 'Exchange': 'Exchange'}, hover_data=['Symbol'])

st.plotly_chart(fig)