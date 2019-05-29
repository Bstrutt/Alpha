
__author__ = 'Bryce Struttman' 

f = open("key.txt", "r")
key = f.read()
from alpha_vantage.timeseries import TimeSeries

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc

import numpy as np
import pandas as pd
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
        self.rangeDataFrame = u.createRange(data, start, end)
        
#%%    
def toCandlestick(trend):
    ohlc = list()
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
    iterator = trend.end
    while iterator < trend.start :
        append_me = iterator, u.getOpenData(trend.rangeDataFrame, iterator), u.getHighData(trend.rangeDataFrame, iterator), u.getLowData(trend.rangeDataFrame, iterator), u.getCloseData(trend.rangeDataFrame, iterator), u.getVolumeData(trend.rangeDataFrame, iterator) 
        ohlc.append(append_me)
        iterator = iterator + timedelta(minutes = 1)
    
    candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('AMD')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()
        



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
 
ts_date = TimeSeries(key=key, output_format='pandas')
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




    
    

    
    
    
