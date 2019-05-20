# -*- coding: utf-8 -*-
"""
Created on Mon May 20 15:19:45 2019

@author: Bryce
"""

import unittest
from pandas import DataFrame
import pandas as pd



class TestDataRetrieval(unittest.TestCase):

    @classmethod
    def setUpClass():
        idx = pd.date_range('2018-01-01', periods=5, freq='min')
        
        Data = {'1. open' : [26.51, 26.49, 26.3535, 26.3166, 26.4051],
                '2. high':[26.51, 26.52, 26.41, 26.41, 26.4051],
                '3. low':[26.4, 26.35, 26.22, 26.285, 26.28],
                '4. close':[26.4951, 26.36, 26.3103, 26.4067, 26.28],
                '5. volume':[762853.0, 765975.0, 971940.0, 633485.0, 488864.0]
                }
        T = DataFrame(Data, idx)
    #%%    
    def testToString(self):
        
        self.assertEqual()
