import streamlit as st
from datetime import date

import yfinance as yf
from fbprophet import Prophet
from fprophet.plot import plot_plotly
from plotly import graph_obj as go


START="2015-01-01"
TODAY=date.today().strftime("%Y-%m-%d")

st.title("stock prdiction")
stocks =("AAPL", "GOOG", "MSFT")
selected_stocks=st.selectbox("select dataset for prediction", stocks)
n_years=st.slider("years of prediction:", 1 ,4)
period=n_years*365
