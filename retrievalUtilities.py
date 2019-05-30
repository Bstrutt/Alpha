# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:50:17 2019

@author: Bryce
"""
from alpha_vantage.timeseries import TimeSeries
import os
import pandas as pd
from datetime import timedelta
from datetime import datetime
import utilityfunctions as u

"""
Reads in stored data for use in feature production
"""
def readSymbol(symbol, interval):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'SymbolPickles', symbol, interval)
    return pd.read_pickle(filename)

"""
Writes the data given in a file named by symbol/interval combinations
"""
def writeSymbol(symbol, interval, data):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'SymbolPickles', symbol, interval)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    data.to_pickle(filename, protocol=3)


"""
Returns the latest time in a pandas dataframe
"""
def latestDatetime(data):
    size = data.shape[0]
    latest = data.iloc[size - 1]
    return latest.name

"""
input: symbol and interval to be edited
output: Updates the stored versions of the symbol/interval
"""
def updateSymbol(symbol, interval):
    #Get Key
    f = open("key.txt", "r")
    key = f.read()  
    f.close()
    
    #Read stored data 
    data = readSymbol(symbol, interval)
    
    #find the latest time that is stored
    latest = latestDatetime(data)
    
    #increment latest time to add subsequent data points
    latest = datetime.strptime(latest, "%Y-%m-%d %H:%M:%S")
    latest = latest + timedelta(minutes = 1)
    latest = u.timeToString(latest)
    
    #Retrieve new data to update stored data
    ts_date = TimeSeries(key=key, output_format='pandas')
    d, m = ts_date.get_intraday(symbol= symbol,interval=interval, outputsize='full')
    
    #append stored data from latest onwards
    updatedData = data.append(d[latest:])
    writeSymbol(symbol, interval, updatedData)
    
    