import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as data
import streamlit as st
start = '2010-01-01'
end = '2021-10-14'
st.title('stock prediction')
user_input=st.text_input('enter stock ticker','AMZN')
df=data.DataReader(user_input,'yahoo',start,end)
st.subheader('Data from 2010-2019')
st.write(df.describe())
st.subheader('closing price vs time chart')
fig=plt.figure(figsize=(12,6))
plt.plot(df.Close)
st.pyplot(fig)
fig=plt.figure(figsize=(12,6))
ma100=df.Close.rolling(100).mean()
plt.plot(df.Close)
plt.plot(ma100)
st.subheader('closing price vs time chart 100mA')
st.pyplot(fig)
ma200=df.Close.rolling(200).mean()
plt.plot(df.Close)
plt.plot(ma200)
st.subheader('closing price vs time chart 200Ma')
st.pyplot(fig)
fig=plt.figure(figsize=(12,6))
plt.plot(df.Close)
plt.plot(ma100,'r')
plt.plot(ma200,'g')
st.subheader('closing price vs time chart moving averages')
st.pyplot(fig)