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
Reads in stored data for use in updating symbol storage
"""
def readSymbolHelper(symbol, interval):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'SymbolPickles', symbol, interval)
    return pd.read_pickle(filename)

"""
Standalone symbol reader for use by user
"""
def readSymbol(symbol, interval):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'SymbolPickles', symbol, interval)
    try:
        return pd.read_pickle(filename)
    except FileNotFoundError:
        print('That symbol/interval is not stored')
"""
Writes the data given in a file named by symbol/interval combinations
Checks for existing file and writes a new file if there is none existing
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
    ts_date = TimeSeries(key=key, output_format='pandas')
    
    #Read stored data 
    try:
        #This can throw an error
        data = readSymbolHelper(symbol, interval)

        #Find the latest time stored and increment it by 1 to make appending
        #easier. There's probably a better way to do this.
        latest = latestDatetime(data)
        latest = datetime.strptime(latest, "%Y-%m-%d %H:%M:%S")
        latest = latest + timedelta(minutes = 1)
        latest = u.timeToString(latest)
        
        #Retrieve new data to update stored data
        d, m = ts_date.get_intraday(symbol= symbol,interval=interval, outputsize='full')
        
        #append stored data from latest onwards
        updatedData = data.append(d[latest:])
        #Write the symbol
        writeSymbol(symbol, interval, updatedData)
        
    except FileNotFoundError:
        #If there is no file previously, do this
        d, m = ts_date.get_intraday(symbol= symbol, interval=interval, outputsize='full')
        writeSymbol(symbol, interval, d)
        
    
