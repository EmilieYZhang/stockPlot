import json
import streamlit as st
import pandas as pd
from bokeh.palettes import Category10
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource

st.title("Exchange 2")

st.subheader('Order Price over Time', divider='grey')
st.text('This is a dropdown the ticker Symbols of each Exchange and the price of \ntheir most recent order aknowledged or executed.')

with open("./datafiles/Exchange_2.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data)
df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])

df_acknowledged = df[df['MessageType'] == 'NewOrderAcknowledged']

# Get the top 10 most recurring symbols
top_symbols = df_acknowledged['Symbol'].value_counts().nlargest(10).index

p = figure(width=800, height=250, x_axis_type="datetime")
p.title.text = 'OrderPrice of MessageType "NewOrderAcknowledged" over Time'

for symbol, color in zip(top_symbols, Category10[10]):
    symbol_data = df_acknowledged[df_acknowledged['Symbol'] == symbol]
    source = ColumnDataSource(symbol_data)
    p.line('TimeStamp', 'OrderPrice', source=source, line_width=2, line_color=color, alpha=0.8, legend_label=symbol)

hover = HoverTool(
    tooltips=[
        ("TimeStamp", "@TimeStamp{%F %T}"),
        ("OrderID", "@OrderID"),
        ("Symbol", "@Symbol"),
        ("OrderPrice", "@OrderPrice"),
    ],
    formatters={"@TimeStamp": "datetime"},
    mode="mouse",
)

p.add_tools(hover)

p.legend.location = "top_left"
p.legend.click_policy = "hide"

st.bokeh_chart(p, use_container_width=True)