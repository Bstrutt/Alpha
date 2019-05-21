"""
Created on Mon May 20 15:19:45 2019
@author: Bryce
"""

import unittest
from pandas import DataFrame
import pandas as pd
import utilityfunctions as u
from datetime import datetime 

class TestDataRetrieval(unittest.TestCase):
    
   
    #%%
    def setUp(self):
        self.D = pd.Timestamp(datetime(2018, 1, 1))
        self.idx = pd.date_range('2018-01-01', periods=5, freq='min')        
        self.Data = {'1. open' : [26.51, 26.49, 26.3535, 26.3166, 26.4051],
                     '2. high':[26.51, 26.52, 26.41, 26.41, 26.4051],
                     '3. low':[26.4, 26.35, 26.22, 26.285, 26.28],
                     '4. close':[26.4951, 26.36, 26.3103, 26.4067, 26.28],
                     '5. volume':[762853.0, 765975.0, 971940.0, 633485.0, 488864.0]
        }
        self.T = DataFrame(self.Data, self.idx)
    def test_ToStringEqual(self):  
        self.assertEqual(u.timeToString(self.D), '2018-01-01 00:00:00')
        
    def test_ToStringNotEqual(self):
        self.assertNotEqual(u.timeToString(self.D), '2018-02-01 00:00:00')            
    
    def test_WithinRange(self):
        self.assertTrue(u.withinRange(1.5, 1, .5))
        
    def test_OutsideRange(self):
        self.assertFalse(u.withinRange(1.6, 1, .5))
        
if __name__ == '__main__':
    unittest.main(verbosity = 2)