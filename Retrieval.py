# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:40:56 2019

@author: Bryce
"""

from alpha_vantage.timeseries import TimeSeries


f = open("key.txt", "r")
key = f.read()
symbols = {'AAPL', 'GOOG', 'GOOGL', 'MSFT', 'FB'}
data = list()
metadata = list()
ts_date = TimeSeries(key=key, output_format='pandas')
for i in symbols:
    d, m = ts_date.get_intraday(symbol= i,interval='5min', outputsize='full')
    data.append(d)
    metadata.append(m)