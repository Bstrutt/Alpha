# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:40:56 2019

@author: Bryce
"""

from alpha_vantage.timeseries import TimeSeries
import os
import pickle as pickle
import pandas as pd
import retrievalUtilities as r


#simple symbol list
symbols = {'FB','GOOG','MSFT', 'AAPL', 'GOOGL'}
interval = '5min'

"""
This function updates the symbols in the symbol list
It will be called regularly to update lists which will be used in analysis
"""
def main():    
    dirname = os.path.dirname(__file__) 
    for symbol in symbols:
        filename = os.path.join(dirname, 'SymbolPickles', symbol, interval)
        os.makedirs(os.path.dirname(filename), exist_ok=True)    
        r.updateSymbol(symbol, interval)
        
        
if __name__== "__main__":
    main()