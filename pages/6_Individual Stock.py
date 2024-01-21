import json
import streamlit as st
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource

st.title("Individual Stock Order Prices")
st.subheader('Order Price over Time', divider='grey')
st.text('This is a dropdown of the Symbols of each Exchange and the price of \ntheir most recent order aknowledged or executed.')

with open("./datafiles/Exchange_1.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data)
df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])

df_acknowledged = df[df['MessageType'] == 'NewOrderAcknowledged']

symbol_options = df_acknowledged['Symbol'].unique()
selected_symbol = st.selectbox('Select Symbol:', symbol_options)

p = figure(width=800, height=250, x_axis_type="datetime")
p.title.text = 'OrderPrice of MessageType "NewOrderAcknowledged" over Time'

symbol_data = df_acknowledged[df_acknowledged['Symbol'] == selected_symbol]
source = ColumnDataSource(symbol_data)
p.line('TimeStamp', 'OrderPrice', source=source, line_width=2, line_color="gray", alpha=0.8, legend_label=selected_symbol)

hover = HoverTool(
    tooltips=[
        ("TimeStamp", "@TimeStamp{%F %T}"),
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