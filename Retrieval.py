# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:40:56 2019

@author: Bryce
"""

from alpha_vantage.timeseries import TimeSeries
import os
import pickle as pickle
import pandas as pd


#read in key
f = open("key.txt", "r")
key = f.read()
f.close()

dirname = os.path.dirname(__file__)
#simple symbol list
symbols = {'AAPL', 'GOOG', 'GOOGL', 'MSFT', 'FB'}
data = list()
metadata = list()
interval = '1min'

ts_date = TimeSeries(key=key, output_format='pandas')
for i in symbols:
    d, m = ts_date.get_intraday(symbol= i,interval=interval, outputsize='full')
    
    
    filename = os.path.join(dirname, 'SymbolPickles', i, interval)
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    d.to_pickle(filename, protocol=3)
    
    data.append(d)
    metadata.append(m)