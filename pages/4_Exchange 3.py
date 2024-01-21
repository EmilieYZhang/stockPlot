import json
import streamlit as st
import pandas as pd
from bokeh.palettes import Spectral4
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource, GraphRenderer

st.title("Exchange 3")

st.subheader('Order Price over Time', divider='grey')
st.text('This is a dropdown the ticker Symbols of each Exchange and the price of \ntheir most recent order aknowledged or executed.')

with open("./datafiles/Exchange_3.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data)
df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])

df_acknowledged = df[df['MessageType'] == 'NewOrderAcknowledged']

source = ColumnDataSource(df_acknowledged)
p = figure(width=800, height=250, x_axis_type="datetime")
p.title.text = 'OrderPrice of MessageType "NewOrderAcknowledged" over Time'

for symbol, color in zip(df_acknowledged['Symbol'].unique(), Spectral4):
    symbol_data = df_acknowledged[df_acknowledged['Symbol'] == symbol]
    p.line('TimeStamp', 'OrderPrice', source=source, line_width=2, color=color, alpha=0.8, legend_label=symbol)

hover = HoverTool(
    tooltips=[
        ("TimeStamp", "@TimeStamp{%F %T}"),
        ("OrderID", "@OrderID"),
        ("Symbol", "@Symbol"),
        ("OrderPrice", "@OrderPrice"),
    ],
    formatters={"@TimeStamp": "datetime"},
    mode="vline",
)

p.add_tools(hover)

p.legend.location = "top_left"
p.legend.click_policy = "hide"

st.bokeh_chart(p, use_container_width=True)