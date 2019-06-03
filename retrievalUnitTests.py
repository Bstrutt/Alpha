# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:46:04 2019

@author: Bryce
"""

import unittest
from pandas import DataFrame
import pandas as pd
import retrievalUtilities as r
from datetime import datetime 


#r.updateSymbol('AMZN','5min')
#Amazon5 = r.readSymbol('AMZN', '5min')



Apple5 = r.readSymbol('AAPL','5min')
Facebook5 = r.readSymbol('FB','5min')
Microsoft5 = r.readSymbol('MSFT','5min')
Google5 = r.readSymbol('GOOG', '5min')
Apple1 = r.readSymbol('AAPL','1min')
Facebook1 = r.readSymbol('FB','1min')
Microsoft1 = r.readSymbol('MSFT','1min')
Google1= r.readSymbol('GOOG', '1min')