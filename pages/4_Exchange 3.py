import json
import streamlit as st
import pandas as pd
from bokeh.palettes import Spectral4
from bokeh.plotting import figure, show
from bokeh.models import DatetimeTickFormatter

with open("./datafiles/Exchange_3.json", "r") as file:
    json_data = file.read()

data = json.loads(json_data)

df = pd.DataFrame(data)
df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])

df_acknowledged = df[df['MessageType'] == 'NewOrderAcknowledged']

# Bokeh
p = figure(width=800, height=250, x_axis_type="datetime")
p.title.text = 'OrderPrice of MessageType "NewOrderAcknowledged" over Time'

# Order Price vs TimeStamp
for symbol, color in zip(df_acknowledged['Symbol'].unique(), Spectral4):
    symbol_data = df_acknowledged[df_acknowledged['Symbol'] == symbol]
    p.line(symbol_data['TimeStamp'], symbol_data['OrderPrice'], line_width=2, color=color, alpha=0.8, legend_label=symbol)

p.legend.location = "top_left"
p.legend.click_policy = "hide"

st.bokeh_chart(p, use_container_width=True)