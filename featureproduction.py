# -*- coding: utf-8 -*-
"""
Created on Wed May 22 14:39:34 2019

@author: Bryce
"""

#import utilityfunctions as u
#import numpy
import talib

"""
Calculates a simple moving average, generalized to any time period

length: The amount of points being averaged, no minimum but the first length
    of points will have value = NaN
data: a pandas dataframe containing ohlc data, specifically the one created by
    alpha_vantage with close at [3]
returns: a Series of float64 with timestamps as index
"""
def sma(length, data):
    size = data.shape[0] - 1
    x = data.iloc[0:size, 3]
    return talib.SMA(x, length)

"""
Calculates an exponential moving average, generalized to any time period

length: The amount of points being averaged, no minimum but the first length
    of points will have value = NaN
data: a pandas dataframe containing ohlc data, specifically the one created by
    alpha_vantage with close at [3]
returns: a Series of float64 with timestamps as index
"""    
def ema(length, data):
    size = data.shape[0] - 1
    x = data.iloc[0:size, 3]
    return talib.EMA(x, length)