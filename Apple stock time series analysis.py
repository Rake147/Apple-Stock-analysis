#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import yfinance as yf
import datetime 
from datetime import date, timedelta
today=date.today()

d1 = today.strftime("%Y-%m-%d")
end_date=d1
d2=date.today() - timedelta(days=720)
d2=d2.strftime('%Y-%m-%d')
start_date=d2

data=yf.download('AAPL', start=start_date, end=end_date, progress=False)
data.head()


# In[2]:


import plotly.express as px
figure=px.line(data,x=data.index,y='Close',title='Time series analysis(line plot)')
figure.show()


# In[3]:


import plotly.graph_objects as go
figure=go.Figure(data=[go.Candlestick(x=data.index,open=data['Open'],high=data['High'],low=data['Low'],close=data['Close'])])


# In[4]:


figure.update_layout(title='Time Series Analysis (Candlestick chart)', xaxis_rangeslider_visible=False)
figure.show()


# In[5]:


figure=px.bar(data,x=data.index,y='Close',title='Time Series Analysis(Bar Plot)')
figure.show()


# Bar plot shows increase in stock price for long term but previously when visualized in candlestick or lineplot we were not able to understand whether the price is increasing or decreasing 

# In[6]:


# Analyzing stock prices between the period of two specific dates
figure=px.line(data,x=data.index,y='Close',range_x=['2021-07-01','2021-12-31'], title="Time series anlysis(Custom Date Range)")
figure.show()


# In[7]:


figure=go.Figure(data=[go.Candlestick(x=data.index,open=data['Open'],high=data['High'],low=data['Low'],close=data['Close'])])
figure.update_layout(title='Time Series Analysis (Candlestick chart with buttons)')

figure.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1,label='1m',step='month',stepmode='backward'),
            dict(count=6,label='6m',step='month',stepmode='backward'),
            dict(count=1,label='YTD',step='year',stepmode='todate'),
            dict(count=1,label='1y',step='year',stepmode='backward'),
            dict(step='all')
        ])
    )
)
figure.show()

