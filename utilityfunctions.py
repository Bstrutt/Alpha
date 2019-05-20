import pandas as pd

"""
Created on Mon May 20 14:59:01 2019
@author: Bryce
"""

"""
Converts timestamps to string for use in indexing dataframes
"""  
def timeToString(t):
    return t.strftime("%Y-%m-%d %H:%M:%S")
"""
Returns close data on the time parameter
"""
def getCloseData(data, time):
    return data.loc[timeToString(time), '4. close']

"""
Returns opening data at the time parameter
"""
def getOpenData(data, time):
    return data.loc[timeToString(time), '1. open']

"""
Returns high data at the time parameter
"""
def getHighData(data, time):
    return data.loc[timeToString(time), '2. high']

"""
Returns low data on the time parameter
"""
def getLowData(data, time):
    return data.loc[timeToString(time), '3. low']

"""
Returns boolean if testVal is within mean plus or minus rangeValue
"""
def withinRange(testVal, mean, rangeValue):
    if testVal > mean + rangeValue:
        return False
    if testVal < mean - rangeValue:
        return False
    return True