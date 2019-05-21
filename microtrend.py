
__author__ = 'Bryce Struttman' 

demo = '59C9BBMYJLO1R7FJ'
from alpha_vantage.timeseries import TimeSeries
import numpy as np
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
from datetime import datetime 
from datetime import timedelta
import utilityfunctions as u

class microTrend:
    start = 0
    end = 0
    initial_price = 0
    close_price = 0
    total_volume = 0
    rangeDataFrame = 0
    def __init__(self, start, end, data):
        self.start = start
        self.end = end
        self.initial_price = u.getCloseData(data, start)
        self.close_price = u.getCloseData(data, end)
        self.rangeDataFrame = createRange(start, end)
        


"""
Returns a new dataframe within the start and end times from data
"""
def createRange(start, end):
    return data[u.timeToString(end):u.timeToString(start)]

#%%    
"""
start : time in dataframe that we try to match 
end: the time that we want to go back to find matches
trend_length: the length of microtrend that we want to match
variability: how forgiving we want to be to the match in ratio (.1)
data: the dataframe we are analyzing
"""
def findMicroTrends(analyzed_time, end, trend_length, variability, data):
    
    time_iterat = analyzed_time - timedelta(minutes = 1)
    """ Iterating backwards towards the beginning of the dataframe
        Stops before end + trend_length
    """
    while(time_iterat >= (end + timedelta(minutes = trend_length))):
        
        count = 1
        while(count < trend_length):
            
            """Find data at test points"""
            try:
                testprev = u.getCloseData(data, time_iterat - timedelta(minutes = count))
                test = u.getCloseData(data, time_iterat - timedelta(minutes = count - 1))
            except KeyError:
                break
            """
            Find analyzed data 
            In the future, this should be calculated outside 
            to save resources
            """
            origin = u.getCloseData(data, analyzed_time - timedelta(minutes = count))
            originprev = u.getCloseData(data, analyzed_time - timedelta(minutes = count - 1))
            
            count = count + 1
            if(u.withinRange(testprev/test, originprev/origin, variability)):
                if(count == trend_length):
                    try:
                        microTrend(time_iterat, time_iterat - timedelta(minutes = trend_length), data)
                    except KeyError:
                        break
                    else:
                        arrTrends.append(microTrend(time_iterat, time_iterat - timedelta(minutes = trend_length), data))

                continue
            else:
                break
        
        time_iterat = time_iterat - timedelta(minutes = 1)
    
    
 #%%
 # retrieve data as pandas dataframe
 
ts_date = TimeSeries(key=demo, output_format='pandas')
data, meta_data = ts_date.get_intraday(symbol='AMD',interval='1min', outputsize='full')

"""
This section of code is retrieving latest time and close data
"""

#%%

#Test Driver for getting data
latest_time = pd.to_datetime(meta_data['3. Last Refreshed'])
second_time = latest_time - timedelta(minutes = 1)
arrTrends = []
first_time = latest_time - timedelta(minutes = data.shape[0])
findMicroTrends(latest_time, first_time, 10, .01, data)
data['4. close'].plot()
plt.title('Intraday Times Series for the AMD stock (1 min)')
plt.show()




    
    

    
    
    
