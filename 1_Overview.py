import streamlit as st
from bokeh.io import show
from bokeh.models import (ColumnDataSource, DataCube, GroupingInfo,
                          StringFormatter, SumAggregator, TableColumn)
from bokeh.plotting import figure
from dataParser import Ex1_symbols_latest_prices_list, Ex2_symbols_latest_prices_list,Ex3_symbols_latest_prices_list

st.set_page_config(
    page_title="InfoExchange",
    page_icon="💲",
)

st.title("Today's Overview")

st.subheader('By Exchange', divider='grey')
st.text('This is a dropdown the ticker Symbols of each Exchange and the price of \ntheir most recent order aknowledged or executed.')

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

st.subheader('Trend overview', divider='grey')
st.text('Graphical representation of recently executed prices of ticker symbols.')

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)