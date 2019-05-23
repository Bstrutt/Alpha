# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:40:56 2019

@author: Bryce
"""
demo = '59C9BBMYJLO1R7FJ'
from alpha_vantage.timeseries import TimeSeries
symbols = {'AAPL', 'GOOG', 'GOOGL', 'MSFT', 'FB', 'CSCO', 'TSM', 'INTC', 'ORCL'}
data = list()
metadata = list()
ts_date = TimeSeries(key=demo, output_format='pandas')
for i in symbols:
    d, m = ts_date.get_intraday(symbol= i,interval='5min', outputsize='full')
    data.append(d)
    metadata.append(m)