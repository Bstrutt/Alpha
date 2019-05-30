# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:50:17 2019

@author: Bryce
"""
from alpha_vantage.timeseries import TimeSeriess
import os
import pandas as pd


"""
Reads in stored data for use in feature production
"""
def readStoredSymbol(symbol, interval):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'SymbolPickles', symbol, interval)
    return pd.read_pickle(filename)

def latestDatetime(data):
    size = data.shape[0]
    latest = data.iloc[size - 1]
    return latest.name

def updateSymbol(symbol, interval):
    #Get Key
    f = open("key.txt", "r")
    key = f.read()  
    f.close()
    
    #Read stored data and find latest point
    data = readStoredSymbol(symbol, interval)
    latest = latestDatetime(data)
    
    #Retrieve new data to update stored data
    ts_date = TimeSeries(key=key, output_format='pandas')
    d, m = ts_date.get_intraday(symbol= symbol,interval=interval, outputsize='full')
    
    
    