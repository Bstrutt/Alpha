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

x = r.readSymbol('AAPL','1min')
z = r.latestDatetime(x)
r.updateSymbol('AAPL', '1min')
x = r.readSymbol('AAPL','1min')
