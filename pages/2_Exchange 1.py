import streamlit as st
import pandas as pd

# from bokeh.palettes import Spectral4
# from bokeh.plotting import figure, show
# from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT

# Time Series Visualization:

# Create a time series chart showing the number of messages over time.
# Use different colors or shapes to represent different message types (NewOrderRequest, NewOrderAcknowledged).
# Animate the chart to show the flow of messages in real-time.
# Symbol Price Trends:

# Visualize the price trends for each symbol over time.
# Use a line chart to connect the order prices for each symbol.
# Apply color gradients to represent the price changes.
st.title("Exchange 1")
# p = figure(width=800, height=250, x_axis_type="datetime")
# p.title.text = 'Click on legend entries to hide the corresponding lines'

# for data, name, color in zip([AAPL, IBM, MSFT, GOOG], ["AAPL", "IBM", "MSFT", "GOOG"], Spectral4):
#     df = pd.DataFrame(data)
#     df['date'] = pd.to_datetime(df['date'])
#     p.line(df['date'], df['close'], line_width=2, color=color, alpha=0.8, legend_label=name)

# p.legend.location = "top_left"
# p.legend.click_policy="hide"

# st.bokeh_chart(p, use_container_width=True)