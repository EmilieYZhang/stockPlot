import pandas as pd
import streamlit as st
import json
from bokeh.models import ColumnDataSource, StringFormatter, TableColumn, SumAggregator, GroupingInfo, DataCube
from bokeh.plotting import figure
from bokeh.palettes import Category10_3
from bokeh.transform import dodge
from dataParser import Ex1_symbols_latest_prices_list, Ex2_symbols_latest_prices_list, Ex3_symbols_latest_prices_list

st.set_page_config(
    page_title="InfoExchange",
    page_icon="💲",
)

st.title("InfoExchange: Overview")
st.text('Using Naitonal Bank\'s database of stock trades, we identify, analyze trends, \npatterns and anomalies across all exchanges.')
st.text('Useful Tip: Graphs are interactive and instances can be saved as images.')

st.subheader('Lastest Trading Prices', divider='grey')
st.text('This is a dropdown the traded ticker Symbols of each Exchange and the price of \ntheir most recent order.')

# Python list variables with tuple pairs for Exchange 1, Exchange 2, and Exchange 3
Pairs1 = Ex1_symbols_latest_prices_list
Pairs2 = Ex2_symbols_latest_prices_list
Pairs3 = Ex3_symbols_latest_prices_list


data = {
    'exchange': ['Exchange 1'] * len(Pairs1) + ['Exchange 2'] * len(Pairs2) + ['Exchange 3'] * len(Pairs3),
    'symbol': [pair[0] for pair in Pairs1 + Pairs2 + Pairs3],
    'px': [pair[1] for pair in Pairs1 + Pairs2 + Pairs3],
}

source = ColumnDataSource(data=data)

target = ColumnDataSource(data=dict(row_indices=[], labels=[]))

formatter = StringFormatter(font_style='bold')

columns = [
    TableColumn(field='symbol', title='Name', width=80, sortable=False, formatter=formatter),
    TableColumn(field='px', title='Price', width=40, sortable=False),
]

grouping = [
    GroupingInfo(getter='exchange', aggregators=[SumAggregator(field_='px')]),
]

#create datacube
cube = DataCube(source=source, columns=columns, grouping=grouping, target=target)


st.bokeh_chart(cube, use_container_width=True)

st.subheader('Activity Graph', divider='grey')
st.text('Number of Message types for all traded stocks.')

### SECOND GRAPH: grouped bar graph by traded symbols

with open("./datafiles/Exchange_1.json", "r") as file:
    data1 = json.load(file)

with open("./datafiles/Exchange_2.json", "r") as file:
    data2 = json.load(file)

with open("./datafiles/Exchange_3.json", "r") as file:
    data3 = json.load(file)

json_data = data1 + data2 + data3

df = pd.DataFrame(json_data)

grouped_data = df.groupby(['Symbol', 'MessageType']).size().reset_index(name='Count')

target_symbols = [pair[0] for pair in Pairs1 + Pairs2 + Pairs3]

p = figure(x_range=target_symbols, plot_height=400, title="Symbol Activity",
           toolbar_location=None, tools="")

color_mapper = {'NewOrderRequest': Category10_3[0], 'Trade': Category10_3[1], 'Cancelled': Category10_3[2]}

dodge_amount = 0.2

for i, msg_type in enumerate(['NewOrderRequest', 'Trade', 'Cancelled']):
    source = ColumnDataSource(grouped_data[grouped_data['MessageType'] == msg_type])
    p.vbar(x=dodge('Symbol', dodge_amount * (i - 1), range=p.x_range), top='Count',
           width=0.2, source=source, color=color_mapper[msg_type], legend_label=msg_type)

p.xgrid.grid_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"

st.bokeh_chart(p, use_container_width=True)