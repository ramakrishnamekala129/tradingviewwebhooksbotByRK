from pprint import pprint
import json
import ccxt 
from actions import exchange
import datetime
import time
import numpy as np
import pandas as pd
from actions import signals
from database import db ,dbnse
from sentiment import *
from actions import *
from actions import percentage
from Trade import *
import pymongo
from Exchangeside import *
from technicalta import *
import dateutil
from stocktrends import indicators
from nsepy import get_history
from datetime import date
#data=get_history(symbol='SBIN',start=date(2015,1,1),end=date(2020,6,5))
#pprint(data)
#data[['Close']].plot()

#from nsepy.history import get_price_list
#prices = get_price_list(dt=date(2020,6,5))
#pprint(prices)
#from nsepy import get_index_pe_history
#nifty_pe = get_index_pe_history(symbol="NIFTY",start=date(2015,1,1),end=date(2020,6,5))
#pprint(nifty_pe)
'''
nifty_opt = get_history(symbol="NIFTY",
                        start=date(2015,1,1),
                        end=date(2015,1,10),
                        index=True,
                        option_type='CE',
                        strike_price=8200,
                        expiry_date=date(2015,1,29))
nifty_opt = get_history(symbol="NIFTY",
                        start=date(2020,5,1),
                        end=date(2020,5,10),
                        index=True,
                        option_type='PE',
                        strike_price=8900,
                        expiry_date=date(2020,6,29))

pprint(nifty_opt)
'''
'''

import pandas as pd

from pandas_datareader import data

start_date = '2014-01-01'
end_date = '2018-01-01'
SRC_DATA_FILENAME = 'goog_data.pkl'

try:
  goog_data2 = pd.read_pickle(SRC_DATA_FILENAME)
except FileNotFoundError:
  goog_data2 = data.DataReader('GOOG', 'yahoo', start_date, end_date)
  goog_data2.to_pickle(SRC_DATA_FILENAME)

goog_data = goog_data2.tail(620)

close = goog_data['Close']


The Relative Strength Index (RSI) was published
 by J. Welles Wilder. The current price is normalized as a percentage
 between 0 and 100. The name of this oscillator is misleading because
 it does not compare the instrument relative to another instrument
 or set of instruments, but rather represents the current price relative
 to other recent pieces within the selected lookback window length.

 RSI = 100 - (100 / (1 + RS))

Where:
 RS = ratio of smoothed average of n-period gains divided by the
 absolute value of the smoothed average of n-period losses.

 
from pandas_datareader import data
start_date = '2014-01-01'
end_date = '2018-01-01'
goog_data = data.DataReader('GOOG', 'yahoo', start_date, end_date)


import numpy as np
import pandas as pd

goog_data_signal = pd.DataFrame(index=goog_data.index)
goog_data_signal['price'] = goog_data['Adj Close']
goog_data_signal['daily_difference'] = goog_data_signal['price'].diff()
goog_data_signal['signal'] = 0.0
goog_data_signal['signal'][:] = np.where(goog_data_signal['daily_difference'][:] > 0, 1.0, 0.0)

goog_data_signal['positions'] = goog_data_signal['signal'].diff()


import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Google price in $')
goog_data_signal['price'].plot(ax=ax1, color='r', lw=2.)

ax1.plot(goog_data_signal.loc[goog_data_signal.positions == 1.0].index,
         goog_data_signal.price[goog_data_signal.positions == 1.0],
         '^', markersize=5, color='m')

ax1.plot(goog_data_signal.loc[goog_data_signal.positions == -1.0].index,
         goog_data_signal.price[goog_data_signal.positions == -1.0],
         'v', markersize=5, color='k')

#plt.show()
'''
'''
# Set the initial capital
initial_capital= float(1000.0)

positions = pd.DataFrame(index=goog_data_signal.index).fillna(0.0)
portfolio = pd.DataFrame(index=goog_data_signal.index).fillna(0.0)


positions['GOOG'] = goog_data_signal['signal']
portfolio['positions'] = (positions.multiply(goog_data_signal['price'], axis=0))
portfolio['cash'] = initial_capital - (positions.diff().multiply(goog_data_signal['price'], axis=0)).cumsum()
portfolio['total'] = portfolio['positions'] + portfolio['cash']
portfolio.plot()
plt.show()


fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Portfolio value in $')
portfolio['total'].plot(ax=ax1, lw=2.)
ax1.plot(portfolio.loc[goog_data_signal.positions == 1.0].index,portfolio.total[goog_data_signal.positions == 1.0],'^', markersize=10, color='m')
ax1.plot(portfolio.loc[goog_data_signal.positions == -1.0].index,portfolio.total[goog_data_signal.positions == -1.0],'v', markersize=10, color='k')
plt.show()

data=db.BTCUSDT_1d.find().sort('_id',pymongo.DESCENDING)
data=pd.DataFrame(data)




data['condition']=np.where(data['Close']>=data['Close'].shift(1), 1, -1)


data['Long_condition']=np.where(data['Close']>=data['Close'].shift(1), 'Long', 0)
data['Long_condition']=np.where((data['Long_condition'].shift(1) == 'Long') ,np.where(data['Close']<=data['Close'].shift(1),'Long_End','Long'), 0)

data['Short_condition']=np.where(data['Close']<=data['Close'].shift(1), 'Short', 0)
data['Short_condition']=np.where((data['Short_condition'].shift(1) == 'Short') ,np.where(data['Close']>=data['Close'].shift(1),'Short_End','Short'), 0)

data['condition']=(data['condition'].diff(1))/2
#data['Profit/Loss']=data['condition']
data['Profit/Loss']=np.where(data['condition']=='Long',data['Close'], 0)
pprint(data)
'''

# get trading data from cryptocompare


STOCKS=["ADANIPORTS",
"ASIANPAINT",
"AXISBANK",
"BAJAJ-AUTO",
"BAJFINANCE",
"BAJAJFINSV",
"BHARTIARTL",
"INFRATEL",
"BPCL",
"BRITANNIA",
"CIPLA",
"COALINDIA",
"DRREDDY",
"EICHERMOT",
"GAIL",
"GRASIM",
"HCLTECH",
"HDFC",
"HDFCBANK",
"HEROMOTOCO",
"HINDALCO",
"HINDUNILVR",
"ICICIBANK",
"INDUSINDBK",
"INFY",
"IOC",
"ITC",
"JSWSTEEL",
"KOTAKBANK",
"LT",
"M&M",
"MARUTI",
"NESTLEIND",
"NTPC",
"ONGC",
"POWERGRID",
"RELIANCE",
"SHREECEM",
"SBIN",
"SUNPHARMA",
"TCS",
"TATAMOTORS",
"TATASTEEL",
"TECHM",
"TITAN",
"ULTRACEMCO",
"UPL",
"VEDL",
"WIPRO",
"ZEEL"]

#pprint(Data_all)
#HEADER='{"symbols":{"tickers":["NSE:ADANIPORTS","NSE:ASIANPAINT","NSE:AXISBANK","NSE:BAJAJ-AUTO","NSE:BAJFINANCE","NSE:BAJAJFINSV","NSE:BHARTIARTL","NSE:INFRATEL","NSE:BPCL","NSE:BRITANNIA","NSE:CIPLA","NSE:COALINDIA","NSE:DRREDDY","NSE:EICHERMOT","NSE:GAIL","NSE:GRASIM","NSE:HCLTECH","NSE:HDFC","NSE:HDFCBANK","NSE:HEROMOTOCO","NSE:HINDALCO","NSE:HINDUNILVR","NSE:ICICIBANK","NSE:INDUSINDBK","NSE:INFY","NSE:IOC","NSE:ITC","NSE:JSWSTEEL","NSE:KOTAKBANK","NSE:LT","NSE:M&M","NSE:MARUTI","NSE:NESTLEIND","NSE:NTPC","NSE:ONGC","NSE:POWERGRID","NSE:RELIANCE","NSE:SHREECEM","NSE:SBIN","NSE:SUNPHARMA","NSE:TCS","NSE:TATAMOTORS","NSE:TATASTEEL","NSE:TECHM","NSE:TITAN","NSE:ULTRACEMCO","NSE:UPL","NSE:VEDL","NSE:WIPRO","NSE:ZEEL"],"query":{"types":[]}},"columns":["Recommend.Other|1","Recommend.All|1","Recommend.MA|1","RSI|1","RSI[1]|1","Stoch.K|1","Stoch.D|1","Stoch.K[1]|1","Stoch.D[1]|1","CCI20|1","CCI20[1]|1","ADX|1","ADX+DI|1","ADX-DI|1","ADX+DI[1]|1","ADX-DI[1]|1","AO|1","AO[1]|1","Mom|1","Mom[1]|1","MACD.macd|1","MACD.signal|1","Rec.Stoch.RSI|1","Stoch.RSI.K|1","Rec.WR|1","W.R|1","Rec.BBPower|1","BBPower|1","Rec.UO|1","UO|1","EMA5|1","close|1","SMA5|1","EMA10|1","SMA10|1","EMA20|1","SMA20|1","EMA30|1","SMA30|1","EMA50|1","SMA50|1","EMA100|1","SMA100|1","EMA200|1","SMA200|1","Rec.Ichimoku|1","Ichimoku.BLine|1","Rec.VWMA|1","VWMA|1","Rec.HullMA9|1","HullMA9|1","Pivot.M.Classic.S3|1","Pivot.M.Classic.S2|1","Pivot.M.Classic.S1|1","Pivot.M.Classic.Middle|1","Pivot.M.Classic.R1|1","Pivot.M.Classic.R2|1","Pivot.M.Classic.R3|1","Pivot.M.Fibonacci.S3|1","Pivot.M.Fibonacci.S2|1","Pivot.M.Fibonacci.S1|1","Pivot.M.Fibonacci.Middle|1","Pivot.M.Fibonacci.R1|1","Pivot.M.Fibonacci.R2|1","Pivot.M.Fibonacci.R3|1","Pivot.M.Camarilla.S3|1","Pivot.M.Camarilla.S2|1","Pivot.M.Camarilla.S1|1","Pivot.M.Camarilla.Middle|1","Pivot.M.Camarilla.R1|1","Pivot.M.Camarilla.R2|1","Pivot.M.Camarilla.R3|1","Pivot.M.Woodie.S3|1","Pivot.M.Woodie.S2|1","Pivot.M.Woodie.S1|1","Pivot.M.Woodie.Middle|1","Pivot.M.Woodie.R1|1","Pivot.M.Woodie.R2|1","Pivot.M.Woodie.R3|1","Pivot.M.Demark.S1|1","Pivot.M.Demark.Middle|1","Pivot.M.Demark.R1|1","Recommend.Other|5","Recommend.All|5","Recommend.MA|5","RSI|5","RSI[1]|5","Stoch.K|5","Stoch.D|5","Stoch.K[1]|5","Stoch.D[1]|5","CCI20|5","CCI20[1]|5","ADX|5","ADX+DI|5","ADX-DI|5","ADX+DI[1]|5","ADX-DI[1]|5","AO|5","AO[1]|5","Mom|5","Mom[1]|5","MACD.macd|5","MACD.signal|5","Rec.Stoch.RSI|5","Stoch.RSI.K|5","Rec.WR|5","W.R|5","Rec.BBPower|5","BBPower|5","Rec.UO|5","UO|5","EMA5|5","close|5","SMA5|5","EMA10|5","SMA10|5","EMA20|5","SMA20|5","EMA30|5","SMA30|5","EMA50|5","SMA50|5","EMA100|5","SMA100|5","EMA200|5","SMA200|5","Rec.Ichimoku|5","Ichimoku.BLine|5","Rec.VWMA|5","VWMA|5","Rec.HullMA9|5","HullMA9|5","Pivot.M.Classic.S3|5","Pivot.M.Classic.S2|5","Pivot.M.Classic.S1|5","Pivot.M.Classic.Middle|5","Pivot.M.Classic.R1|5","Pivot.M.Classic.R2|5","Pivot.M.Classic.R3|5","Pivot.M.Fibonacci.S3|5","Pivot.M.Fibonacci.S2|5","Pivot.M.Fibonacci.S1|5","Pivot.M.Fibonacci.Middle|5","Pivot.M.Fibonacci.R1|5","Pivot.M.Fibonacci.R2|5","Pivot.M.Fibonacci.R3|5","Pivot.M.Camarilla.S3|5","Pivot.M.Camarilla.S2|5","Pivot.M.Camarilla.S1|5","Pivot.M.Camarilla.Middle|5","Pivot.M.Camarilla.R1|5","Pivot.M.Camarilla.R2|5","Pivot.M.Camarilla.R3|5","Pivot.M.Woodie.S3|5","Pivot.M.Woodie.S2|5","Pivot.M.Woodie.S1|5","Pivot.M.Woodie.Middle|5","Pivot.M.Woodie.R1|5","Pivot.M.Woodie.R2|5","Pivot.M.Woodie.R3|5","Pivot.M.Demark.S1|5","Pivot.M.Demark.Middle|5","Pivot.M.Demark.R1|5","Recommend.Other|15","Recommend.All|15","Recommend.MA|15","RSI|15","RSI[1]|15","Stoch.K|15","Stoch.D|15","Stoch.K[1]|15","Stoch.D[1]|15","CCI20|15","CCI20[1]|15","ADX|15","ADX+DI|15","ADX-DI|15","ADX+DI[1]|15","ADX-DI[1]|15","AO|15","AO[1]|15","Mom|15","Mom[1]|15","MACD.macd|15","MACD.signal|15","Rec.Stoch.RSI|15","Stoch.RSI.K|15","Rec.WR|15","W.R|15","Rec.BBPower|15","BBPower|15","Rec.UO|15","UO|15","EMA5|15","close|15","SMA5|15","EMA10|15","SMA10|15","EMA20|15","SMA20|15","EMA30|15","SMA30|15","EMA50|15","SMA50|15","EMA100|15","SMA100|15","EMA200|15","SMA200|15","Rec.Ichimoku|15","Ichimoku.BLine|15","Rec.VWMA|15","VWMA|15","Rec.HullMA9|15","HullMA9|15","Pivot.M.Classic.S3|15","Pivot.M.Classic.S2|15","Pivot.M.Classic.S1|15","Pivot.M.Classic.Middle|15","Pivot.M.Classic.R1|15","Pivot.M.Classic.R2|15","Pivot.M.Classic.R3|15","Pivot.M.Fibonacci.S3|15","Pivot.M.Fibonacci.S2|15","Pivot.M.Fibonacci.S1|15","Pivot.M.Fibonacci.Middle|15","Pivot.M.Fibonacci.R1|15","Pivot.M.Fibonacci.R2|15","Pivot.M.Fibonacci.R3|15","Pivot.M.Camarilla.S3|15","Pivot.M.Camarilla.S2|15","Pivot.M.Camarilla.S1|15","Pivot.M.Camarilla.Middle|15","Pivot.M.Camarilla.R1|15","Pivot.M.Camarilla.R2|15","Pivot.M.Camarilla.R3|15","Pivot.M.Woodie.S3|15","Pivot.M.Woodie.S2|15","Pivot.M.Woodie.S1|15","Pivot.M.Woodie.Middle|15","Pivot.M.Woodie.R1|15","Pivot.M.Woodie.R2|15","Pivot.M.Woodie.R3|15","Pivot.M.Demark.S1|15","Pivot.M.Demark.Middle|15","Pivot.M.Demark.R1|15","Recommend.Other|60","Recommend.All|60","Recommend.MA|60","RSI|60","RSI[1]|60","Stoch.K|60","Stoch.D|60","Stoch.K[1]|60","Stoch.D[1]|60","CCI20|60","CCI20[1]|60","ADX|60","ADX+DI|60","ADX-DI|60","ADX+DI[1]|60","ADX-DI[1]|60","AO|60","AO[1]|60","Mom|60","Mom[1]|60","MACD.macd|60","MACD.signal|60","Rec.Stoch.RSI|60","Stoch.RSI.K|60","Rec.WR|60","W.R|60","Rec.BBPower|60","BBPower|60","Rec.UO|60","UO|60","EMA5|60","close|60","SMA5|60","EMA10|60","SMA10|60","EMA20|60","SMA20|60","EMA30|60","SMA30|60","EMA50|60","SMA50|60","EMA100|60","SMA100|60","EMA200|60","SMA200|60","Rec.Ichimoku|60","Ichimoku.BLine|60","Rec.VWMA|60","VWMA|60","Rec.HullMA9|60","HullMA9|60","Pivot.M.Classic.S3|60","Pivot.M.Classic.S2|60","Pivot.M.Classic.S1|60","Pivot.M.Classic.Middle|60","Pivot.M.Classic.R1|60","Pivot.M.Classic.R2|60","Pivot.M.Classic.R3|60","Pivot.M.Fibonacci.S3|60","Pivot.M.Fibonacci.S2|60","Pivot.M.Fibonacci.S1|60","Pivot.M.Fibonacci.Middle|60","Pivot.M.Fibonacci.R1|60","Pivot.M.Fibonacci.R2|60","Pivot.M.Fibonacci.R3|60","Pivot.M.Camarilla.S3|60","Pivot.M.Camarilla.S2|60","Pivot.M.Camarilla.S1|60","Pivot.M.Camarilla.Middle|60","Pivot.M.Camarilla.R1|60","Pivot.M.Camarilla.R2|60","Pivot.M.Camarilla.R3|60","Pivot.M.Woodie.S3|60","Pivot.M.Woodie.S2|60","Pivot.M.Woodie.S1|60","Pivot.M.Woodie.Middle|60","Pivot.M.Woodie.R1|60","Pivot.M.Woodie.R2|60","Pivot.M.Woodie.R3|60","Pivot.M.Demark.S1|60","Pivot.M.Demark.Middle|60","Pivot.M.Demark.R1|60","Recommend.Other|240","Recommend.All|240","Recommend.MA|240","RSI|240","RSI[1]|240","Stoch.K|240","Stoch.D|240","Stoch.K[1]|240","Stoch.D[1]|240","CCI20|240","CCI20[1]|240","ADX|240","ADX+DI|240","ADX-DI|240","ADX+DI[1]|240","ADX-DI[1]|240","AO|240","AO[1]|240","Mom|240","Mom[1]|240","MACD.macd|240","MACD.signal|240","Rec.Stoch.RSI|240","Stoch.RSI.K|240","Rec.WR|240","W.R|240","Rec.BBPower|240","BBPower|240","Rec.UO|240","UO|240","EMA5|240","close|240","SMA5|240","EMA10|240","SMA10|240","EMA20|240","SMA20|240","EMA30|240","SMA30|240","EMA50|240","SMA50|240","EMA100|240","SMA100|240","EMA200|240","SMA200|240","Rec.Ichimoku|240","Ichimoku.BLine|240","Rec.VWMA|240","VWMA|240","Rec.HullMA9|240","HullMA9|240","Pivot.M.Classic.S3|240","Pivot.M.Classic.S2|240","Pivot.M.Classic.S1|240","Pivot.M.Classic.Middle|240","Pivot.M.Classic.R1|240","Pivot.M.Classic.R2|240","Pivot.M.Classic.R3|240","Pivot.M.Fibonacci.S3|240","Pivot.M.Fibonacci.S2|240","Pivot.M.Fibonacci.S1|240","Pivot.M.Fibonacci.Middle|240","Pivot.M.Fibonacci.R1|240","Pivot.M.Fibonacci.R2|240","Pivot.M.Fibonacci.R3|240","Pivot.M.Camarilla.S3|240","Pivot.M.Camarilla.S2|240","Pivot.M.Camarilla.S1|240","Pivot.M.Camarilla.Middle|240","Pivot.M.Camarilla.R1|240","Pivot.M.Camarilla.R2|240","Pivot.M.Camarilla.R3|240","Pivot.M.Woodie.S3|240","Pivot.M.Woodie.S2|240","Pivot.M.Woodie.S1|240","Pivot.M.Woodie.Middle|240","Pivot.M.Woodie.R1|240","Pivot.M.Woodie.R2|240","Pivot.M.Woodie.R3|240","Pivot.M.Demark.S1|240","Pivot.M.Demark.Middle|240","Pivot.M.Demark.R1|240","Recommend.Other","Recommend.All","Recommend.MA","RSI","RSI[1]","Stoch.K","Stoch.D","Stoch.K[1]","Stoch.D[1]","CCI20","CCI20[1]","ADX","ADX+DI","ADX-DI","ADX+DI[1]","ADX-DI[1]","AO","AO[1]","Mom","Mom[1]","MACD.macd","MACD.signal","Rec.Stoch.RSI","Stoch.RSI.K","Rec.WR","W.R","Rec.BBPower","BBPower","Rec.UO","UO","EMA5","close","SMA5","EMA10","SMA10","EMA20","SMA20","EMA30","SMA30","EMA50","SMA50","EMA100","SMA100","EMA200","SMA200","Rec.Ichimoku","Ichimoku.BLine","Rec.VWMA","VWMA","Rec.HullMA9","HullMA9","Pivot.M.Classic.S3","Pivot.M.Classic.S2","Pivot.M.Classic.S1","Pivot.M.Classic.Middle","Pivot.M.Classic.R1","Pivot.M.Classic.R2","Pivot.M.Classic.R3","Pivot.M.Fibonacci.S3","Pivot.M.Fibonacci.S2","Pivot.M.Fibonacci.S1","Pivot.M.Fibonacci.Middle","Pivot.M.Fibonacci.R1","Pivot.M.Fibonacci.R2","Pivot.M.Fibonacci.R3","Pivot.M.Camarilla.S3","Pivot.M.Camarilla.S2","Pivot.M.Camarilla.S1","Pivot.M.Camarilla.Middle","Pivot.M.Camarilla.R1","Pivot.M.Camarilla.R2","Pivot.M.Camarilla.R3","Pivot.M.Woodie.S3","Pivot.M.Woodie.S2","Pivot.M.Woodie.S1","Pivot.M.Woodie.Middle","Pivot.M.Woodie.R1","Pivot.M.Woodie.R2","Pivot.M.Woodie.R3","Pivot.M.Demark.S1","Pivot.M.Demark.Middle","Pivot.M.Demark.R1","Recommend.Other|1W","Recommend.All|1W","Recommend.MA|1W","RSI|1W","RSI[1]|1W","Stoch.K|1W","Stoch.D|1W","Stoch.K[1]|1W","Stoch.D[1]|1W","CCI20|1W","CCI20[1]|1W","ADX|1W","ADX+DI|1W","ADX-DI|1W","ADX+DI[1]|1W","ADX-DI[1]|1W","AO|1W","AO[1]|1W","Mom|1W","Mom[1]|1W","MACD.macd|1W","MACD.signal|1W","Rec.Stoch.RSI|1W","Stoch.RSI.K|1W","Rec.WR|1W","W.R|1W","Rec.BBPower|1W","BBPower|1W","Rec.UO|1W","UO|1W","EMA5|1W","close|1W","SMA5|1W","EMA10|1W","SMA10|1W","EMA20|1W","SMA20|1W","EMA30|1W","SMA30|1W","EMA50|1W","SMA50|1W","EMA100|1W","SMA100|1W","EMA200|1W","SMA200|1W","Rec.Ichimoku|1W","Ichimoku.BLine|1W","Rec.VWMA|1W","VWMA|1W","Rec.HullMA9|1W","HullMA9|1W","Pivot.M.Classic.S3|1W","Pivot.M.Classic.S2|1W","Pivot.M.Classic.S1|1W","Pivot.M.Classic.Middle|1W","Pivot.M.Classic.R1|1W","Pivot.M.Classic.R2|1W","Pivot.M.Classic.R3|1W","Pivot.M.Fibonacci.S3|1W","Pivot.M.Fibonacci.S2|1W","Pivot.M.Fibonacci.S1|1W","Pivot.M.Fibonacci.Middle|1W","Pivot.M.Fibonacci.R1|1W","Pivot.M.Fibonacci.R2|1W","Pivot.M.Fibonacci.R3|1W","Pivot.M.Camarilla.S3|1W","Pivot.M.Camarilla.S2|1W","Pivot.M.Camarilla.S1|1W","Pivot.M.Camarilla.Middle|1W","Pivot.M.Camarilla.R1|1W","Pivot.M.Camarilla.R2|1W","Pivot.M.Camarilla.R3|1W","Pivot.M.Woodie.S3|1W","Pivot.M.Woodie.S2|1W","Pivot.M.Woodie.S1|1W","Pivot.M.Woodie.Middle|1W","Pivot.M.Woodie.R1|1W","Pivot.M.Woodie.R2|1W","Pivot.M.Woodie.R3|1W","Pivot.M.Demark.S1|1W","Pivot.M.Demark.Middle|1W","Pivot.M.Demark.R1|1W","Recommend.Other|1M","Recommend.All|1M","Recommend.MA|1M","RSI|1M","RSI[1]|1M","Stoch.K|1M","Stoch.D|1M","Stoch.K[1]|1M","Stoch.D[1]|1M","CCI20|1M","CCI20[1]|1M","ADX|1M","ADX+DI|1M","ADX-DI|1M","ADX+DI[1]|1M","ADX-DI[1]|1M","AO|1M","AO[1]|1M","Mom|1M","Mom[1]|1M","MACD.macd|1M","MACD.signal|1M","Rec.Stoch.RSI|1M","Stoch.RSI.K|1M","Rec.WR|1M","W.R|1M","Rec.BBPower|1M","BBPower|1M","Rec.UO|1M","UO|1M","EMA5|1M","close|1M","SMA5|1M","EMA10|1M","SMA10|1M","EMA20|1M","SMA20|1M","EMA30|1M","SMA30|1M","EMA50|1M","SMA50|1M","EMA100|1M","SMA100|1M","EMA200|1M","SMA200|1M","Rec.Ichimoku|1M","Ichimoku.BLine|1M","Rec.VWMA|1M","VWMA|1M","Rec.HullMA9|1M","HullMA9|1M","Pivot.M.Classic.S3|1M","Pivot.M.Classic.S2|1M","Pivot.M.Classic.S1|1M","Pivot.M.Classic.Middle|1M","Pivot.M.Classic.R1|1M","Pivot.M.Classic.R2|1M","Pivot.M.Classic.R3|1M","Pivot.M.Fibonacci.S3|1M","Pivot.M.Fibonacci.S2|1M","Pivot.M.Fibonacci.S1|1M","Pivot.M.Fibonacci.Middle|1M","Pivot.M.Fibonacci.R1|1M","Pivot.M.Fibonacci.R2|1M","Pivot.M.Fibonacci.R3|1M","Pivot.M.Camarilla.S3|1M","Pivot.M.Camarilla.S2|1M","Pivot.M.Camarilla.S1|1M","Pivot.M.Camarilla.Middle|1M","Pivot.M.Camarilla.R1|1M","Pivot.M.Camarilla.R2|1M","Pivot.M.Camarilla.R3|1M","Pivot.M.Woodie.S3|1M","Pivot.M.Woodie.S2|1M","Pivot.M.Woodie.S1|1M","Pivot.M.Woodie.Middle|1M","Pivot.M.Woodie.R1|1M","Pivot.M.Woodie.R2|1M","Pivot.M.Woodie.R3|1M","Pivot.M.Demark.S1|1M","Pivot.M.Demark.Middle|1M","Pivot.M.Demark.R1|1M"]}'
columns=["open|1","open|5","open|15","open|60","open|240","open","open|1W","open|1M","high|1","high|5","high|15","high|60","high|240","high","high|1W","high|1M","low|1","low|5","low|15","low|60","low|240","low","low|1W","low|1M","close|1","close|5","close|15","close|60","close|240","close","close|1W","close|1M","volume|1","volume|5","volume|15","volume|60","volume|240","volume","volume|1W","volume|1M"]
#pprint(columns)
'''for i in columns:
	i=i.replace(".","_").replace("|","_").replace("[","_").replace("]","_")
	print('"{}",'.format(i))

'''

#'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'


'''
listing=db.BTCUSDT_15m.find()
df=pd.DataFrame(listing)

df['open']=df['Open']
df['close']=df['Close']
df['high']= df['High']
df['low']=df['Low']
df.set_index('date',inplace=False)
pprint(df)
renko = indicators.Renko(df)
renko.brick_size=100
renko.chart_type = indicators.Renko.PERIOD_CLOSE
data = renko.get_ohlc_data()
pprint(data)


#pprint(list(db.list_collection_names()))
#data=db.position.find_one(sort=[('_id',pymongo.DESCENDING)])
#pprint(data['openingTimestamp'])
#data1=db.ETHUSDT_15m.find_one(sort=[('_id',pymongo.DESCENDING)])
#pprint(data1)
#data=list(db.ETHUSDT_1m.find({'date':{'$gte':data['openingTimestamp'],'$lte':data1['date']}}).sort("_id", pymongo.ASCENDING))#.limit(100))
#data=list(db.ETHUSDT_15m.find()).sort({'date':{'$gt':data['openingTimestamp']}}, pymongo.DESCENDING).limit(100))

#data1=list(db.ETHUSDT_15m.find().sort("_id", pymongo.DESCENDING).limit(10))
#pprint(data)
#pprint(data1)

timeframe='1h'
symbol='ETH/USD'
percent=3

position=db.position.find_one({'symbol':symbolizer(symbol)},sort=[('_id',pymongo.DESCENDING)])
if position:
	if symbol == 'ETH/USD':
		symbol='ETHUSDT'
	elif symbol == 'BTC/USD':
		symbol='BTCUSDT'
	else:
		print('Error Ocuured')

	last_time=db['{}_{}'.format(symbol,timeframe)].find_one(sort=[('_id',pymongo.DESCENDING)])	
	if last_time:
		
		data=list(db['{}_{}'.format(symbol,timeframe)].find({'date':{'$gte':position['openingTimestamp'],'$lte':last_time['date']}}).sort("_id", pymongo.ASCENDING))
		
		if data:
			df=pd.DataFrame(data)


			if position['Side'] == 'Long':
				percent=(100-percent)/100
				boughtprice=data[0]['Close']

				#STOPLOSS
				stoploss=percent*boughtprice
				df['STOPLOSS']=stoploss


				#Trailing STOP
				trailstop=percent*boughtprice
				df['Highest']=df['High'].cummax()
				df['TrailingStop']=df['Highest']*percent


				#TrailingstopDotDot
				trailstop=percent*boughtprice
				#df['Trail']=trailstop
					#		df['Trail']=np.where(df['Close']>df['Close'].shift(1), df['Trail']+df['Close']-df['Close'].shift(1), df['Trail'].shift(1))
					#		print(len(df))
							
				df['Trailing']=0
				df['Trailing'][0]=trailstop
				#print(df['Trailing'][0])
				for i in range(1,len(df)):
					if df['Close'][i] > df['Close'][i-1]:
						df['Trailing'][i]=df['Trailing'][i-1]+df['Close'][i]- df['Close'][i-1]
					else:
						df['Trailing'][i]=df['Trailing'][i-1]
					#print(df['Trailing'][i])


				df['Stoploss_triggered']=0
				#df['Stoploss_triggered'][0]=trailstop
				#print(df['Stoploss_triggered'][0])
				for i in range(1,len(df)):
					if df['Close'][i] < df['STOPLOSS'][i]:
						df['Stoploss_triggered'][i]=1
					else:
						df['Stoploss_triggered'][i]=0
					#print(df['Stoploss_triggered'][i])


				df['Trail_Stoploss_triggered']=0
				#df['Stoploss_triggered'][0]=trailstop
				#print(df['Trail_Stoploss_triggered'][0])
				for i in range(1,len(df)):
					if df['Close'][i] < df['Trailing'][i]:
						df['Trail_Stoploss_triggered'][i]=1
					else:
						df['Trail_Stoploss_triggered'][i]=0
					#print(df['Trail_Stoploss_triggered'][i])
				
			elif position['Side'] == 'Short':
				percent=(100+percent)/100
				boughtprice=data[0]['Close']

				#STOPLOSS
				stoploss=percent*boughtprice
				df['STOPLOSS']=stoploss


				#Trailing STOP
				trailstop=percent*boughtprice
				df['Lowest']=df['Low'].cummin()
				df['TrailingStop']=df['Lowest']*percent
			else:
				print('Error Ocurred')

			#Take_Profit


			#Trailing Profit

			pprint(df)


'''

























'''
print('hi0')
p=list(db.position.find({'symbol':'ETHUSD'}).sort("_id", pymongo.DESCENDING).limit(1))
p=db.position.find_one({'symbol':'ETHUSD'},sort=[('_id', pymongo.DESCENDING)])
pprint(p)
def side(data):
	if data['currentQty'] > 0:
		side='Long'
	else:
		side='Short'
	return side

exchange_position=exchange.private_get_position()
for data in exchange_position:
	file='{}_Orders'.format(data['symbol'])
	orders=db[file]
	if file not in db.list_collection_names():
		
		post={
		'date':datetime.datetime.now(),
		'EntryPrice':data['avgEntryPrice'],
		'openingTimestamp':dateutil.parser.isoparse(data['openingTimestamp']),
		'isOpen':data['isOpen'],
		'lastPrice':data['lastPrice'],
		'currentTimestamp':dateutil.parser.isoparse(data['currentTimestamp']),
		'currentQty':data['currentQty'],
		'Side':side(data)
		}
		save=db[file].insert_one(post)
		print(save)
	else:
		print('hi')
		check=db[file].find_one(sort=[('_id', pymongo.DESCENDING)])
		if check['isOpen'] == False:
			post={
			'date':datetime.datetime.now(),
			'EntryPrice':data['avgEntryPrice'],
			'openingTimestamp':dateutil.parser.isoparse(data['openingTimestamp']),
			'isOpen':data['isOpen'],
			'lastPrice':data['lastPrice'],
			'currentTimestamp':dateutil.parser.isoparse(data['currentTimestamp']),
			'currentQty':data['currentQty'],
			'Side':side(data)
			}
			save=db[file].insert_one(post)
			print(save)
		elif check['isOpen'] == True:
			_id=check['_id']
			query={'_id':_id}
			newvalues = { "$set": {'date':datetime.datetime.now(),
			'EntryPrice':data['avgEntryPrice'],
			'openingTimestamp':dateutil.parser.isoparse(data['openingTimestamp']),
			'isOpen':data['isOpen'],
			'lastPrice':data['lastPrice'],
			'currentTimestamp':dateutil.parser.isoparse(data['currentTimestamp']),
			'currentQty':data['currentQty'],
			'Side':side(data)
			}}
			db[file].update_one(query, newvalues)
		else:
			_id=check['_id']
			query={'_id':_id}
'''

'''
def Trade_Management(exchange):
    data1=exchange.private_get_position({'filter': json.dumps({"isOpen": True})})
    #data=data[0]
    if data1 :
        for data in data1:
            position=db.position
            #p=list(db.position.find({'symbol':data['symbol']}).sort("_id", pymongo.DESCENDING).limit(1))
            #p=p[0]
            p=db.position.find_one({'symbol':data['symbol']},sort=[('_id', pymongo.DESCENDING)])
            if 'position' not in db.list_collection_names():
            	post={'date':datetime.datetime.utcnow(),'account':data['account'],'symbol':data['symbol'],'currency':data['currency'],'underlying':data['underlying'],'quoteCurrency':data['quoteCurrency'],'commission':data['commission'],'initMarginReq':data['initMarginReq'],'maintMarginReq':data['maintMarginReq'],'riskLimit':data['riskLimit'],'leverage':data['leverage'],'crossMargin':data['crossMargin'],'deleveragePercentile':data['deleveragePercentile'],'rebalancedPnl':data['rebalancedPnl'],'prevRealisedPnl':data['prevRealisedPnl'],'prevUnrealisedPnl':data['prevUnrealisedPnl'],'prevClosePrice':data['prevClosePrice'],'openingTimestamp':dateutil.parser.isoparse(data['openingTimestamp']),'openingQty':data['openingQty'],'openingCost':data['openingCost'],'openingComm':data['openingComm'],'openOrderBuyQty':data['openOrderBuyQty'],'openOrderBuyCost':data['openOrderBuyCost'],'openOrderBuyPremium':data['openOrderBuyPremium'],'openOrderSellQty':data['openOrderSellQty'],'openOrderSellCost':data['openOrderSellCost'],'openOrderSellPremium':data['openOrderSellPremium'],'execBuyQty':data['execBuyQty'],'execBuyCost':data['execBuyCost'],'execSellQty':data['execSellQty'],'execSellCost':data['execSellCost'],'execQty':data['execQty'],'execCost':data['execCost'],'execComm':data['execComm'],'currentTimestamp':dateutil.parser.isoparse(data['currentTimestamp']),'currentQty':data['currentQty'],'currentCost':data['currentCost'],'currentComm':data['currentComm'],'realisedCost':data['realisedCost'],'unrealisedCost':data['unrealisedCost'],'grossOpenCost':data['grossOpenCost'],'grossOpenPremium':data['grossOpenPremium'],'grossExecCost':data['grossExecCost'],'isOpen':data['isOpen'],'markPrice':data['markPrice'],'markValue':data['markValue'],'riskValue':data['riskValue'],'homeNotional':data['homeNotional'],'foreignNotional':data['foreignNotional'],'posState':data['posState'],'posCost':data['posCost'],'posCost2':data['posCost2'],'posCross':data['posCross'],'posInit':data['posInit'],'posComm':data['posComm'],'posLoss':data['posLoss'],'posMargin':data['posMargin'],'posMaint':data['posMaint'],'posAllowance':data['posAllowance'],'taxableMargin':data['taxableMargin'],'initMargin':data['initMargin'],'maintMargin':data['maintMargin'],'sessionMargin':data['sessionMargin'],'targetExcessMargin':data['targetExcessMargin'],'varMargin':data['varMargin'],'realisedGrossPnl':data['realisedGrossPnl'],'realisedTax':data['realisedTax'],'realisedPnl':data['realisedPnl'],'unrealisedGrossPnl':data['unrealisedGrossPnl'],'longBankrupt':data['longBankrupt'],'shortBankrupt':data['shortBankrupt'],'taxBase':data['taxBase'],'indicativeTaxRate':data['indicativeTaxRate'],'indicativeTax':data['indicativeTax'],'unrealisedTax':data['unrealisedTax'],'unrealisedPnl':data['unrealisedPnl'],'unrealisedPnlPcnt':data['unrealisedPnlPcnt'],'unrealisedRoePcnt':data['unrealisedRoePcnt'],'simpleQty':data['simpleQty'],'simpleCost':data['simpleCost'],'simpleValue':data['simpleValue'],'simplePnl':data['simplePnl'],'simplePnlPcnt':data['simplePnlPcnt'],'avgCostPrice':data['avgCostPrice'],'avgEntryPrice':data['avgEntryPrice'],'breakEvenPrice':data['breakEvenPrice'],'marginCallPrice':data['marginCallPrice'],'liquidationPrice':data['liquidationPrice'],'bankruptPrice':data['bankruptPrice'],'timestamp':dateutil.parser.isoparse(data['timestamp']),'lastPrice':data['lastPrice'],'lastValue':data['lastValue'],'Side':side(data)}
            	position_id=position.insert_one(post).inserted_id
				#print(position_id)
            elif p['isOpen'] == False:    
                #for i,d in j.items():
                    #print("'{}':data['{}'],".format(i,i))
                post={
                'date':datetime.datetime.utcnow(),
                'account':data['account'],
                'symbol':data['symbol'],
                'currency':data['currency'],
                'underlying':data['underlying'],
                'quoteCurrency':data['quoteCurrency'],
                'commission':data['commission'],
                'initMarginReq':data['initMarginReq'],
                'maintMarginReq':data['maintMarginReq'],
                'riskLimit':data['riskLimit'],
                'leverage':data['leverage'],
                'crossMargin':data['crossMargin'],
                'deleveragePercentile':data['deleveragePercentile'],
                'rebalancedPnl':data['rebalancedPnl'],
                'prevRealisedPnl':data['prevRealisedPnl'],
                'prevUnrealisedPnl':data['prevUnrealisedPnl'],
                'prevClosePrice':data['prevClosePrice'],
                'openingTimestamp':dateutil.parser.isoparse(data['openingTimestamp']),
                'openingQty':data['openingQty'],
                'openingCost':data['openingCost'],
                'openingComm':data['openingComm'],
                'openOrderBuyQty':data['openOrderBuyQty'],
                'openOrderBuyCost':data['openOrderBuyCost'],
                'openOrderBuyPremium':data['openOrderBuyPremium'],
                'openOrderSellQty':data['openOrderSellQty'],
                'openOrderSellCost':data['openOrderSellCost'],
                'openOrderSellPremium':data['openOrderSellPremium'],
                'execBuyQty':data['execBuyQty'],
                'execBuyCost':data['execBuyCost'],
                'execSellQty':data['execSellQty'],
                'execSellCost':data['execSellCost'],
                'execQty':data['execQty'],
                'execCost':data['execCost'],
                'execComm':data['execComm'],
                'currentTimestamp':dateutil.parser.isoparse(data['currentTimestamp']),
                'currentQty':data['currentQty'],
                'currentCost':data['currentCost'],
                'currentComm':data['currentComm'],
                'realisedCost':data['realisedCost'],
                'unrealisedCost':data['unrealisedCost'],
                'grossOpenCost':data['grossOpenCost'],
                'grossOpenPremium':data['grossOpenPremium'],
                'grossExecCost':data['grossExecCost'],
                'isOpen':data['isOpen'],
                'markPrice':data['markPrice'],
                'markValue':data['markValue'],
                'riskValue':data['riskValue'],
                'homeNotional':data['homeNotional'],
                'foreignNotional':data['foreignNotional'],
                'posState':data['posState'],
                'posCost':data['posCost'],
                'posCost2':data['posCost2'],
                'posCross':data['posCross'],
                'posInit':data['posInit'],
                'posComm':data['posComm'],
                'posLoss':data['posLoss'],
                'posMargin':data['posMargin'],
                'posMaint':data['posMaint'],
                'posAllowance':data['posAllowance'],
                'taxableMargin':data['taxableMargin'],
                'initMargin':data['initMargin'],
                'maintMargin':data['maintMargin'],
                'sessionMargin':data['sessionMargin'],
                'targetExcessMargin':data['targetExcessMargin'],
                'varMargin':data['varMargin'],
                'realisedGrossPnl':data['realisedGrossPnl'],
                'realisedTax':data['realisedTax'],
                'realisedPnl':data['realisedPnl'],
                'unrealisedGrossPnl':data['unrealisedGrossPnl'],
                'longBankrupt':data['longBankrupt'],
                'shortBankrupt':data['shortBankrupt'],
                'taxBase':data['taxBase'],
                'indicativeTaxRate':data['indicativeTaxRate'],
                'indicativeTax':data['indicativeTax'],
                'unrealisedTax':data['unrealisedTax'],
                'unrealisedPnl':data['unrealisedPnl'],
                'unrealisedPnlPcnt':data['unrealisedPnlPcnt'],
                'unrealisedRoePcnt':data['unrealisedRoePcnt'],
                'simpleQty':data['simpleQty'],
                'simpleCost':data['simpleCost'],
                'simpleValue':data['simpleValue'],
                'simplePnl':data['simplePnl'],
                'simplePnlPcnt':data['simplePnlPcnt'],
                'avgCostPrice':data['avgCostPrice'],
                'avgEntryPrice':data['avgEntryPrice'],
                'breakEvenPrice':data['breakEvenPrice'],
                'marginCallPrice':data['marginCallPrice'],
                'liquidationPrice':data['liquidationPrice'],
                'bankruptPrice':data['bankruptPrice'],
                'timestamp':dateutil.parser.isoparse(data['timestamp']),
                'lastPrice':data['lastPrice'],
                'lastValue':data['lastValue'],
                'Side':side(data)}

                #print(data)

                position=db.position
                position_id=position.insert_one(post).inserted_id
                print(position_id)
            else:
                position=db.position
                k=db.position.find_one({'symbol':data['symbol']},sort=[('_id', pymongo.DESCENDING)])
                k=k['_id']
        #print(k)
                myquery = { "_id": k }
                d=False
                newvalues = { "$set": { 'date':datetime.datetime.utcnow(),
                'account':data['account'],
                'symbol':data['symbol'],
                'currency':data['currency'],
                'underlying':data['underlying'],
                'quoteCurrency':data['quoteCurrency'],
                'commission':data['commission'],
                'initMarginReq':data['initMarginReq'],
                'maintMarginReq':data['maintMarginReq'],
                'riskLimit':data['riskLimit'],
                'leverage':data['leverage'],
                'crossMargin':data['crossMargin'],
                'deleveragePercentile':data['deleveragePercentile'],
                'rebalancedPnl':data['rebalancedPnl'],
                'prevRealisedPnl':data['prevRealisedPnl'],
                'prevUnrealisedPnl':data['prevUnrealisedPnl'],
                'prevClosePrice':data['prevClosePrice'],
                'openingTimestamp':dateutil.parser.isoparse(data['openingTimestamp']),
                'openingQty':data['openingQty'],
                'openingCost':data['openingCost'],
                'openingComm':data['openingComm'],
                'openOrderBuyQty':data['openOrderBuyQty'],
                'openOrderBuyCost':data['openOrderBuyCost'],
                'openOrderBuyPremium':data['openOrderBuyPremium'],
                'openOrderSellQty':data['openOrderSellQty'],
                'openOrderSellCost':data['openOrderSellCost'],
                'openOrderSellPremium':data['openOrderSellPremium'],
                'execBuyQty':data['execBuyQty'],
                'execBuyCost':data['execBuyCost'],
                'execSellQty':data['execSellQty'],
                'execSellCost':data['execSellCost'],
                'execQty':data['execQty'],
                'execCost':data['execCost'],
                'execComm':data['execComm'],
                'currentTimestamp':dateutil.parser.isoparse(data['currentTimestamp']),
                'currentQty':data['currentQty'],
                'currentCost':data['currentCost'],
                'currentComm':data['currentComm'],
                'realisedCost':data['realisedCost'],
                'unrealisedCost':data['unrealisedCost'],
                'grossOpenCost':data['grossOpenCost'],
                'grossOpenPremium':data['grossOpenPremium'],
                'grossExecCost':data['grossExecCost'],
                'isOpen':data['isOpen'],
                'markPrice':data['markPrice'],
                'markValue':data['markValue'],
                'riskValue':data['riskValue'],
                'homeNotional':data['homeNotional'],
                'foreignNotional':data['foreignNotional'],
                'posState':data['posState'],
                'posCost':data['posCost'],
                'posCost2':data['posCost2'],
                'posCross':data['posCross'],
                'posInit':data['posInit'],
                'posComm':data['posComm'],
                'posLoss':data['posLoss'],
                'posMargin':data['posMargin'],
                'posMaint':data['posMaint'],
                'posAllowance':data['posAllowance'],
                'taxableMargin':data['taxableMargin'],
                'initMargin':data['initMargin'],
                'maintMargin':data['maintMargin'],
                'sessionMargin':data['sessionMargin'],
                'targetExcessMargin':data['targetExcessMargin'],
                'varMargin':data['varMargin'],
                'realisedGrossPnl':data['realisedGrossPnl'],
                'realisedTax':data['realisedTax'],
                'realisedPnl':data['realisedPnl'],
                'unrealisedGrossPnl':data['unrealisedGrossPnl'],
                'longBankrupt':data['longBankrupt'],
                'shortBankrupt':data['shortBankrupt'],
                'taxBase':data['taxBase'],
                'indicativeTaxRate':data['indicativeTaxRate'],
                'indicativeTax':data['indicativeTax'],
                'unrealisedTax':data['unrealisedTax'],
                'unrealisedPnl':data['unrealisedPnl'],
                'unrealisedPnlPcnt':data['unrealisedPnlPcnt'],
                'unrealisedRoePcnt':data['unrealisedRoePcnt'],
                'simpleQty':data['simpleQty'],
                'simpleCost':data['simpleCost'],
                'simpleValue':data['simpleValue'],
                'simplePnl':data['simplePnl'],
                'simplePnlPcnt':data['simplePnlPcnt'],
                'avgCostPrice':data['avgCostPrice'],
                'avgEntryPrice':data['avgEntryPrice'],
                'breakEvenPrice':data['breakEvenPrice'],
                'marginCallPrice':data['marginCallPrice'],
                'liquidationPrice':data['liquidationPrice'],
                'bankruptPrice':data['bankruptPrice'],
                'timestamp':dateutil.parser.isoparse(data['timestamp']),
                'lastPrice':data['lastPrice'],
                'lastValue':data['lastValue'],
                'Side':side(data)} }
        
                k=position.update_one(myquery, newvalues)
                print('Updated Position Data')
                #checking=list(position.find({'symbol':'XBTUSD'}))[-1]
                #print(checking)


    else:

        position=db.position
        k=db.position.find_one({'symbol':'XBTUSD'},sort=[('_id', pymongo.DESCENDING)])
        k=k['_id']
        myquery = { "_id": k }
        d=False
        newvalues = { "$set": { 'isOpen': d } }
        k=position.update_one(myquery, newvalues)
        position=db.position
        k=db.position.find_one({'symbol':'ETHUSD'},sort=[('_id', pymongo.DESCENDING)])
        k=k['_id']
        #print(k)
        myquery = { "_id": k }
        d=False
        newvalues = { "$set": { 'isOpen': d } }
        k=position.update_one(myquery, newvalues)


'''
'''
	#current_time=datetime.now().timestamp()
	timestamp=dateutil.parser.isoparse(data['openingTimestamp'])
	print(timestamp)
	#if current_time < timestamp:
	date=datetime.fromtimestamp(timestamp)
	#time1=date+timingdelta(timeframe)
	time=date.isoformat()
	print(time)
	'''
'''
[{'account': 179347,
'avgCostPrice': 203.48,
'avgEntryPrice': 203.48,
'bankruptPrice': 100.25,
'breakEvenPrice': 209.7,
'commission': 0.00075,
'crossMargin': True,
'currency': 'XBt',
'currentComm': 45034,
'currentCost': 2665575,
'currentQty': 131,
'currentTimestamp': '2020-05-31T03:50:30.376Z',
'deleveragePercentile': 1,
'execBuyCost': 0,
'execBuyQty': 0,
'execComm': 0,
'execCost': 0,
'execQty': 0,
'execSellCost': 0,
'execSellQty': 0,
'foreignNotional': -297.8014762269939,
'grossExecCost': 0,
'grossOpenCost': 0,
'grossOpenPremium': 0,
'homeNotional': 1.2557515337423313,
'indicativeTax': 0,
'indicativeTaxRate': None,
'initMargin': 0,
'initMarginReq': 0.02,
'isOpen': True,
'lastPrice': 237.15,
'lastValue': 3106665,
'leverage': 50,
'liquidationPrice': 101.9,
'longBankrupt': 0,
'maintMargin': 496506,
'maintMarginReq': 0.008,
'marginCallPrice': 101.9,
'markPrice': 237.15,
'markValue': 3106665,
'openOrderBuyCost': 0,
'openOrderBuyPremium': 0,
'openOrderBuyQty': 0,
'openOrderSellCost': 0,
'openOrderSellPremium': 0,
'openOrderSellQty': 0,
'openingComm': 45034,
'openingCost': 2665575,
'openingQty': 131,
'openingTimestamp': '2020-05-31T03:00:00.000Z',
'posAllowance': 0,
'posComm': 2104,
'posCost': 2665575,
'posCost2': 2750889,
'posCross': 85314,
'posInit': 53312,
'posLoss': 85314,
'posMaint': 23429,
'posMargin': 55416,
'posState': '',
'prevClosePrice': 242.84,
'prevRealisedPnl': -3769,
'prevUnrealisedPnl': 0,
'quoteCurrency': 'USD',
'realisedCost': 0,
'realisedGrossPnl': 0,
'realisedPnl': -45034,
'realisedTax': 0,
'rebalancedPnl': -36259,
'riskLimit': 5000000000,
'riskValue': 3106665,
'sessionMargin': 0,
'shortBankrupt': 0,
'simpleCost': None,
'simplePnl': None,
'simplePnlPcnt': None,
'simpleQty': None,
'simpleValue': None,
'symbol': 'ETHUSD',
'targetExcessMargin': 0,
'taxBase': 0,
'taxableMargin': 0,
'timestamp': '2020-05-31T03:50:30.376Z',
'underlying': 'ETH',
'unrealisedCost': 2665575,
'unrealisedGrossPnl': 441090,
'unrealisedPnl': 441090,
'unrealisedPnlPcnt': 0.1655,
'unrealisedRoePcnt': 8.2738,
'unrealisedTax': 0,
'varMargin': 0}]

df=data_maker()
pprint(df)

d=df['Volume'].diff(periods=1)
pprint(d)
'''

'''
listof1=[
'Double Exponential Moving Average',
'Exponential Moving Average',
'Hilbert Transform - Instantaneous Trendline',
'Kaufman Adaptive Moving Average',
'Moving average',
'Moving average with variable period',
'MidPoint over period',
'Midpoint Price over period',
'Parabolic SAR',
'Parabolic SAR - Extended',
'Simple Moving Average',
'Triple Exponential Moving Average (T3)',
'Triple Exponential Moving Average',
'Triangular Moving Average',
'Weighted Moving Average',
'Average Directional Movement Index',
'Average Directional Movement Index Rating',
'Absolute Price Oscillator',
'Aroon Oscillator',
'Balance Of Power',
'Commodity Channel Index',
'Chande Momentum Oscillator',
'Directional Movement Index',
'MACD with controllable MA type',
'Money Flow Index',
'Minus Directional Indicator',
'Minus Directional Movement',
'Momentum',
'Plus Directional Indicator',
'Plus Directional Movement',
'Percentage Price Oscillator',
'Rate of change',
'Rate of change Percentage',
'Rate of change ratio',
'Rate of change ratio 100 scale',
'Relative Strength Index',
'one-day Rate-Of-Change ROC of a Triple Smooth EMA',
'Ultimate Oscillator',
'Williams',
'Chaikin A/D Line',
'Chaikin A/D Oscillator',
'On Balance Volume',
'Two Crows',
'Three Black Crows',
'Three Inside Up/Down',
'Three-Line Strike',
'Three Outside Up/Down',
'Three Stars In The South',
'Three Advancing White Soldiers',
'Abandoned Baby',
'Advance Block',
'Belt-hold',
'Breakaway',
'Closing Marubozu',
'Concealing Baby Swallow',
'Counterattack',
'Dark Cloud Cover',
'Doji',
'Doji Star',
'Dragonfly Doji',
'Engulfing Pattern',
'Evening Doji Star',
'Evening Star',
'Up/Down-gap side-by-side white lines',
'Gravestone Doji',
'Hammer',
'Hanging Man',
'Harami Pattern',
'Harami Cross Pattern',
'High-Wave Candle',
'Hikkake Pattern',
'Modified Hikkake Pattern',
'Homing Pigeon',
'Identical Three Crows',
'In-Neck Pattern',
'Inverted Hammer',
'Kicking',
'Kicking - bull/bear',
'Ladder Bottom',
'Long Legged Doji',
'Long Line Candle',
'Marubozu',
'Matching Low',
'Mat Hold',
'Morning Doji Star',
'Morning Star',
'On-Neck Pattern',
'Piercing Pattern',
'Rickshaw Man',
'Rising/Falling Three Methods',
'Separating Lines',
'Shooting Star',
'Short Line Candle',
'Spinning Top',
'Stalled Pattern',
'Stick Sandwich',
'Takuri',
'Tasuki Gap',
'Thrusting Pattern',
'Tristar Pattern',
'Unique 3 River',
'Upside Gap Two Crows',
'Upside/Downside Gap Three Methods'
]
listof3=['Bollinger Bands','Moving Average Convergence-Divergence Fix','Moving Average Convergence-Divergence']

listof2=['Aroon','MESA Adaptive Moving Average','Stochastic','Stochastic Fast','Stochastic Relative Strength Index']
b=""

'''


'''for i in range(0,2):
	a="graphJSON{}=graphJSON{},".format(i,i)
	b+=a
print(b)
'''
'''
for k in listof1:
    i=texterconversion(k)
    print("def {}_Plot():".format(i))
    print("    from technicalta import indicator_data_level_1")
    print("    from plotly.subplots import make_subplots")
    print("    import plotly.graph_objects as go")
    print("    df=indicator_data_level_1()")
    print("    df=df.reset_index()")
    print("    fig1=go.Figure()")
    print("    fig1.add_trace(go.Scatter(x=df['date'], y=df['{}'],name='{}'))".format(i,k))
    print("    fig1.update_layout(title='{}',xaxis_title='Time',yaxis_title='{}')".format(k,k))
    print("    return fig1")


for k in listof2:
    i=texterconversion(k)
    print("def {}_Plot():".format(i))
    print("    from technicalta import indicator_data_level_2")
    print("    from plotly.subplots import make_subplots")
    print("    import plotly.graph_objects as go")
    print("    df=indicator_data_level_2()")
    print("    df=df.reset_index()")
    print("    fig1=go.Figure()")
    print("    fig1.add_trace(go.Scatter(x=df['date'], y=df['{}_0'],name='{}_0'))".format(i,k))
    print("    fig1.add_trace(go.Scatter(x=df['date'], y=df['{}_1'],name='{}_1'))".format(i,k))
    print("    fig1.update_layout(title='{}',xaxis_title='Time',yaxis_title='{}')".format(k,k))
    print("    return fig1")
for k in listof3:
    i=texterconversion(k)
    print("def {}_Plot():".format(i))
    print("    from technicalta import indicator_data_level_3")
    print("    from plotly.subplots import make_subplots")
    print("    import plotly.graph_objects as go")
    print("    df=indicator_data_level_3()")
    print("    df=df.reset_index()")
    print("    fig1=go.Figure()")
    print("    fig1.add_trace(go.Scatter(x=df['date'], y=df['{}_0'],name='{}_0'))".format(i,k))
    print("    fig1.add_trace(go.Scatter(x=df['date'], y=df['{}_1'],name='{}_1'))".format(i,k))
    print("    fig1.add_trace(go.Scatter(x=df['date'], y=df['{}_2'],name='{}_1'))".format(i,k))
    print("    fig1.update_layout(title='{}',xaxis_title='Time',yaxis_title='{}')".format(k,k))
    print("    return fig1")
'''
'''
def indicator_data_level_():
    from technicalta import texterconversion,listof1,listof3,listof2,technicalselector
    chart=db.chart.find_one(sort=[('_id', pymongo.DESCENDING)])
    symbol=chart['symbols'].replace("/","")
    tf=chart['tf']
    coin="{}_{}".format(symbol,tf)
    indicator=chart['technical']
    #print(chart)
    df=data_maker()
    listof3=listof3
    listof2=listof2
    listof1=listof1
    listof3=[texterconversion(file) for file in listof3 ]
    listof2=[texterconversion(file) for file in listof2 ]
    listof1=[texterconversion(file) for file in listof1 ]
    names_indicator=list([texterconversion(file) for file in indicator if texterconversion(file) in listof3])
    data=list([list(technicalselector(file,df)) for file in names_indicator ])
    columns_names=list([texterconversion(file) for file in indicator if texterconversion(file) in listof3])
    #pprint(data)
    length=len(columns_names)
    #pprint(columns_names)
    for i in range(0,length):
        df1=pd.DataFrame(data[i]).transpose()
        df1.columns=["{}_0".format(columns_names[i]),"{}_1".format(columns_names[i]),"{}_2".format(columns_names[i])]
        #pprint(df1)
        df=df.join(df1)
    #pprint(df)
    df.set_index("date", inplace = True)
    df=df.drop(columns=['_id','Open','Low','High','Volume','Close'])
    #pprint(df)
    return df

df=indicator_data_level_()
print(df)

'''











'''
for i in range(0,250):
	print("<script type='text/javascript'>var graphs{}=".format(i),"{{","graph[{}] | safe".format(i),"}};","Plotly.plot('chart{}',graphs{},".format(i,i),"{""});</script>")
'''

'''
for i in range(0,250):
 	print('<div id="chart{}"></div>'.format(i))'''
'''
for i in listof1:
	i =texterconversion(i)
	print("elif technical == '{}':".format(i))
	print('    tech={}_Plot()'.format(i))
for i in listof2:
	i =texterconversion(i)
	print("elif technical == '{}':".format(i))
	print('    tech={}_Plot()'.format(i))
for i in listof3:
	i =texterconversion(i)
	print("elif technical == '{}':".format(i))
	print('    tech={}_Plot()'.format(i))


'''
'''
def technical_plotter(technical):
	technical=texterconversion(technical)
	if technical == 'Double_Exponential_Moving_Average':
	    tech=Double_Exponential_Moving_Average_Plot()
	elif technical == 'Exponential_Moving_Average':
	    tech=Exponential_Moving_Average_Plot()
	elif technical == 'Hilbert_Transform___Instantaneous_Trendline':
	    tech=Hilbert_Transform___Instantaneous_Trendline_Plot()
	elif technical == 'Kaufman_Adaptive_Moving_Average':
	    tech=Kaufman_Adaptive_Moving_Average_Plot()
	elif technical == 'Moving_average':
	    tech=Moving_average_Plot()
	elif technical == 'Moving_average_with_variable_period':
	    tech=Moving_average_with_variable_period_Plot()
	elif technical == 'MidPoint_over_period':
	    tech=MidPoint_over_period_Plot()
	elif technical == 'Midpoint_Price_over_period':
	    tech=Midpoint_Price_over_period_Plot()
	elif technical == 'Parabolic_SAR':
	    tech=Parabolic_SAR_Plot()
	elif technical == 'Parabolic_SAR___Extended':
	    tech=Parabolic_SAR___Extended_Plot()
	elif technical == 'Simple_Moving_Average':
	    tech=Simple_Moving_Average_Plot()
	elif technical == 'Triple_Exponential_Moving_Average_T3':
	    tech=Triple_Exponential_Moving_Average_T3_Plot()
	elif technical == 'Triple_Exponential_Moving_Average':
	    tech=Triple_Exponential_Moving_Average_Plot()
	elif technical == 'Triangular_Moving_Average':
	    tech=Triangular_Moving_Average_Plot()
	elif technical == 'Weighted_Moving_Average':
	    tech=Weighted_Moving_Average_Plot()
	elif technical == 'Average_Directional_Movement_Index':
	    tech=Average_Directional_Movement_Index_Plot()
	elif technical == 'Average_Directional_Movement_Index_Rating':
	    tech=Average_Directional_Movement_Index_Rating_Plot()
	elif technical == 'Absolute_Price_Oscillator':
	    tech=Absolute_Price_Oscillator_Plot()
	elif technical == 'Aroon_Oscillator':
	    tech=Aroon_Oscillator_Plot()
	elif technical == 'Balance_Of_Power':
	    tech=Balance_Of_Power_Plot()
	elif technical == 'Commodity_Channel_Index':
	    tech=Commodity_Channel_Index_Plot()
	elif technical == 'Chande_Momentum_Oscillator':
	    tech=Chande_Momentum_Oscillator_Plot()
	elif technical == 'Directional_Movement_Index':
	    tech=Directional_Movement_Index_Plot()
	elif technical == 'MACD_with_controllable_MA_type':
	    tech=MACD_with_controllable_MA_type_Plot()
	elif technical == 'Money_Flow_Index':
	    tech=Money_Flow_Index_Plot()
	elif technical == 'Minus_Directional_Indicator':
	    tech=Minus_Directional_Indicator_Plot()
	elif technical == 'Minus_Directional_Movement':
	    tech=Minus_Directional_Movement_Plot()
	elif technical == 'Momentum':
	    tech=Momentum_Plot()
	elif technical == 'Plus_Directional_Indicator':
	    tech=Plus_Directional_Indicator_Plot()
	elif technical == 'Plus_Directional_Movement':
	    tech=Plus_Directional_Movement_Plot()
	elif technical == 'Percentage_Price_Oscillator':
	    tech=Percentage_Price_Oscillator_Plot()
	elif technical == 'Rate_of_change':
	    tech=Rate_of_change_Plot()
	elif technical == 'Rate_of_change_Percentage':
	    tech=Rate_of_change_Percentage_Plot()
	elif technical == 'Rate_of_change_ratio':
	    tech=Rate_of_change_ratio_Plot()
	elif technical == 'Rate_of_change_ratio_100_scale':
	    tech=Rate_of_change_ratio_100_scale_Plot()
	elif technical == 'Relative_Strength_Index':
	    tech=Relative_Strength_Index_Plot()
	elif technical == 'one_day_Rate_Of_Change_ROC_of_a_Triple_Smooth_EMA':
	    tech=one_day_Rate_Of_Change_ROC_of_a_Triple_Smooth_EMA_Plot()
	elif technical == 'Ultimate_Oscillator':
	    tech=Ultimate_Oscillator_Plot()
	elif technical == 'Williams':
	    tech=Williams_Plot()
	elif technical == 'Chaikin_AD_Line':
	    tech=Chaikin_AD_Line_Plot()
	elif technical == 'Chaikin_AD_Oscillator':
	    tech=Chaikin_AD_Oscillator_Plot()
	elif technical == 'On_Balance_Volume':
	    tech=On_Balance_Volume_Plot()
	elif technical == 'Two_Crows':
	    tech=Two_Crows_Plot()
	elif technical == 'Three_Black_Crows':
	    tech=Three_Black_Crows_Plot()
	elif technical == 'Three_Inside_UpDown':
	    tech=Three_Inside_UpDown_Plot()
	elif technical == 'Three_Line_Strike':
	    tech=Three_Line_Strike_Plot()
	elif technical == 'Three_Outside_UpDown':
	    tech=Three_Outside_UpDown_Plot()
	elif technical == 'Three_Stars_In_The_South':
	    tech=Three_Stars_In_The_South_Plot()
	elif technical == 'Three_Advancing_White_Soldiers':
	    tech=Three_Advancing_White_Soldiers_Plot()
	elif technical == 'Abandoned_Baby':
	    tech=Abandoned_Baby_Plot()
	elif technical == 'Advance_Block':
	    tech=Advance_Block_Plot()
	elif technical == 'Belt_hold':
	    tech=Belt_hold_Plot()
	elif technical == 'Breakaway':
	    tech=Breakaway_Plot()
	elif technical == 'Closing_Marubozu':
	    tech=Closing_Marubozu_Plot()
	elif technical == 'Concealing_Baby_Swallow':
	    tech=Concealing_Baby_Swallow_Plot()
	elif technical == 'Counterattack':
	    tech=Counterattack_Plot()
	elif technical == 'Dark_Cloud_Cover':
	    tech=Dark_Cloud_Cover_Plot()
	elif technical == 'Doji':
	    tech=Doji_Plot()
	elif technical == 'Doji_Star':
	    tech=Doji_Star_Plot()
	elif technical == 'Dragonfly_Doji':
	    tech=Dragonfly_Doji_Plot()
	elif technical == 'Engulfing_Pattern':
	    tech=Engulfing_Pattern_Plot()
	elif technical == 'Evening_Doji_Star':
	    tech=Evening_Doji_Star_Plot()
	elif technical == 'Evening_Star':
	    tech=Evening_Star_Plot()
	elif technical == 'UpDown_gap_side_by_side_white_lines':
	    tech=UpDown_gap_side_by_side_white_lines_Plot()
	elif technical == 'Gravestone_Doji':
	    tech=Gravestone_Doji_Plot()
	elif technical == 'Hammer':
	    tech=Hammer_Plot()
	elif technical == 'Hanging_Man':
	    tech=Hanging_Man_Plot()
	elif technical == 'Harami_Pattern':
	    tech=Harami_Pattern_Plot()
	elif technical == 'Harami_Cross_Pattern':
	    tech=Harami_Cross_Pattern_Plot()
	elif technical == 'High_Wave_Candle':
	    tech=High_Wave_Candle_Plot()
	elif technical == 'Hikkake_Pattern':
	    tech=Hikkake_Pattern_Plot()
	elif technical == 'Modified_Hikkake_Pattern':
	    tech=Modified_Hikkake_Pattern_Plot()
	elif technical == 'Homing_Pigeon':
	    tech=Homing_Pigeon_Plot()
	elif technical == 'Identical_Three_Crows':
	    tech=Identical_Three_Crows_Plot()
	elif technical == 'In_Neck_Pattern':
	    tech=In_Neck_Pattern_Plot()
	elif technical == 'Inverted_Hammer':
	    tech=Inverted_Hammer_Plot()
	elif technical == 'Kicking':
	    tech=Kicking_Plot()
	elif technical == 'Kicking___bullbear':
	    tech=Kicking___bullbear_Plot()
	elif technical == 'Ladder_Bottom':
	    tech=Ladder_Bottom_Plot()
	elif technical == 'Long_Legged_Doji':
	    tech=Long_Legged_Doji_Plot()
	elif technical == 'Long_Line_Candle':
	    tech=Long_Line_Candle_Plot()
	elif technical == 'Marubozu':
	    tech=Marubozu_Plot()
	elif technical == 'Matching_Low':
	    tech=Matching_Low_Plot()
	elif technical == 'Mat_Hold':
	    tech=Mat_Hold_Plot()
	elif technical == 'Morning_Doji_Star':
	    tech=Morning_Doji_Star_Plot()
	elif technical == 'Morning_Star':
	    tech=Morning_Star_Plot()
	elif technical == 'On_Neck_Pattern':
	    tech=On_Neck_Pattern_Plot()
	elif technical == 'Piercing_Pattern':
	    tech=Piercing_Pattern_Plot()
	elif technical == 'Rickshaw_Man':
	    tech=Rickshaw_Man_Plot()
	elif technical == 'RisingFalling_Three_Methods':
	    tech=RisingFalling_Three_Methods_Plot()
	elif technical == 'Separating_Lines':
	    tech=Separating_Lines_Plot()
	elif technical == 'Shooting_Star':
	    tech=Shooting_Star_Plot()
	elif technical == 'Short_Line_Candle':
	    tech=Short_Line_Candle_Plot()
	elif technical == 'Spinning_Top':
	    tech=Spinning_Top_Plot()
	elif technical == 'Stalled_Pattern':
	    tech=Stalled_Pattern_Plot()
	elif technical == 'Stick_Sandwich':
	    tech=Stick_Sandwich_Plot()
	elif technical == 'Takuri':
	    tech=Takuri_Plot()
	elif technical == 'Tasuki_Gap':
	    tech=Tasuki_Gap_Plot()
	elif technical == 'Thrusting_Pattern':
	    tech=Thrusting_Pattern_Plot()
	elif technical == 'Tristar_Pattern':
	    tech=Tristar_Pattern_Plot()
	elif technical == 'Unique_3_River':
	    tech=Unique_3_River_Plot()
	elif technical == 'Upside_Gap_Two_Crows':
	    tech=Upside_Gap_Two_Crows_Plot()
	elif technical == 'UpsideDownside_Gap_Three_Methods':
	    tech=UpsideDownside_Gap_Three_Methods_Plot()
	elif technical == 'Aroon':
	    tech=Aroon_Plot()
	elif technical == 'MESA_Adaptive_Moving_Average':
	    tech=MESA_Adaptive_Moving_Average_Plot()
	elif technical == 'Stochastic':
	    tech=Stochastic_Plot()
	elif technical == 'Stochastic_Fast':
	    tech=Stochastic_Fast_Plot()
	elif technical == 'Stochastic_Relative_Strength_Index':
	    tech=Stochastic_Relative_Strength_Index_Plot()
	elif technical == 'Bollinger_Bands':
	    tech=Bollinger_Bands_Plot()
	elif technical == 'Moving_Average_Convergence_Divergence_Fix':
	    tech=Moving_Average_Convergence_Divergence_Fix_Plot()
	elif technical == 'Moving_Average_Convergence_Divergence':
	    tech=Moving_Average_Convergence_Divergence_Plot()
	return tech
'''

















'''
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = px.line(df, x='Date', y='AAPL.High')

# Use date string to set xaxis range
fig.update_layout(xaxis_range=['2016-07-01','2016-12-31'],
                  title_text="Manually Set Date Range")
fig.show()'''
'''
from technicalta import indicator_data_level_1
from plotly.subplots import make_subplots
names,df=indicator_data_level_1()
length=len(names)
fig=make_subplots(rows=length, cols=1,subplot_titles=names)
for i in length:
	fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),row=i, col=1)
'''
'''
def Morining_Star_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    names,df=indicator_data_level_1()
    df=df['Morining_Star']
    length=len(names)
    df=df.reset_index()
    #df['H-Line']=70
    #df['L-Line']=20
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Morining_Star'],name='Morining_Star'))
    #fig1.add_trace(go.Scatter(x=df['date'], y=df['H-Line'],name='H-Line'))
    #fig1.add_trace(go.Scatter(x=df['date'], y=df['L-Line'],name='L-Line'))
    fig1.update_layout(title='Morining_Star',xaxis_title='Time',yaxis_title='Morining_Star')
    return fig1
'''

'''
listof3=['Bollinger Bands','Moving Average Convergence-Divergence Fix','Moving Average Convergence-Divergence']

listof2=['Aroon','MESA Adaptive Moving Average','Stochastic','Stochastic Fast','Stochastic Relative Strength Index']

listof1=[
'Double Exponential Moving Average',
'Exponential Moving Average',
'Hilbert Transform - Instantaneous Trendline',
'Kaufman Adaptive Moving Average',
'Moving average',
'Moving average with variable period',
'MidPoint over period',
'Midpoint Price over period',
'Parabolic SAR',
'Parabolic SAR - Extended',
'Simple Moving Average',
'Triple Exponential Moving Average (T3)',
'Triple Exponential Moving Average',
'Triangular Moving Average',
'Weighted Moving Average',
'Average Directional Movement Index',
'Average Directional Movement Index Rating',
'Absolute Price Oscillator',
'Aroon Oscillator',
'Balance Of Power',
'Commodity Channel Index',
'Chande Momentum Oscillator',
'Directional Movement Index',
'MACD with controllable MA type',
'Money Flow Index',
'Minus Directional Indicator',
'Minus Directional Movement',
'Momentum',
'Plus Directional Indicator',
'Plus Directional Movement',
'Percentage Price Oscillator',
'Rate of change',
'Rate of change Percentage',
'Rate of change ratio',
'Rate of change ratio 100 scale',
'Relative Strength Index',
'one-day Rate-Of-Change ROC of a Triple Smooth EMA',
'Ultimate Oscillator',
'Williams',
'Chaikin A/D Line',
'Chaikin A/D Oscillator',
'On Balance Volume',
'Two Crows',
'Three Black Crows',
'Three Inside Up/Down',
'Three-Line Strike',
'Three Outside Up/Down',
'Three Stars In The South',
'Three Advancing White Soldiers',
'Abandoned Baby',
'Advance Block',
'Belt-hold',
'Breakaway',
'Closing Marubozu',
'Concealing Baby Swallow',
'Counterattack',
'Dark Cloud Cover',
'Doji',
'Doji Star',
'Dragonfly Doji',
'Engulfing Pattern',
'Evening Doji Star',
'Evening Star',
'Up/Down-gap side-by-side white lines',
'Gravestone Doji',
'Hammer',
'Hanging Man',
'Harami Pattern',
'Harami Cross Pattern',
'High-Wave Candle',
'Hikkake Pattern',
'Modified Hikkake Pattern',
'Homing Pigeon',
'Identical Three Crows',
'In-Neck Pattern',
'Inverted Hammer',
'Kicking',
'Kicking - bull/bear',
'Ladder Bottom',
'Long Legged Doji',
'Long Line Candle',
'Marubozu',
'Matching Low',
'Mat Hold',
'Morning Doji Star',
'Morning Star',
'On-Neck Pattern',
'Piercing Pattern',
'Rickshaw Man',
'Rising/Falling Three Methods',
'Separating Lines',
'Shooting Star',
'Short Line Candle',
'Spinning Top',
'Stalled Pattern',
'Stick Sandwich',
'Takuri',
'Tasuki Gap',
'Thrusting Pattern',
'Tristar Pattern',
'Unique 3 River',
'Upside Gap Two Crows',
'Upside/Downside Gap Three Methods'
]
function=['Aroon','MESA Adaptive Moving Average','Stochastic','Stochastic Fast','Stochastic Relative Strength Index']

from technicalta import indicator_data_level_1
from plotly.subplots import make_subplots
import plotly.graph_objects as go

'''



































'''

for k in listof1:
	i=texterconversion(k)
	print("def {}_Plot():".format(i))
	print("    from technicalta import indicator_data_level_1")
	print("    from plotly.subplots import make_subplots")
	print("    import plotly.graph_objects as go")
	print("    df=indicator_data_level_1()")
	print("    df=df['{}']".format(i))
	print("    df=df.reset_index()")
	print("    fig1=go.Figure()")
	print("    fig1.add_trace(go.Scatter(x=df['date'], y=df['{}'],name='{}'))".format(i,k))
	print("    fig1.update_layout(title='{}',xaxis_title='Time',yaxis_title='{}')".format(k,k))
	print("    return fig1")


for k in listof2:
	i=texterconversion(k)
	print("def {}_Plot():".format(i))
	print("    from technicalta import indicator_data_level_2")
	print("    from plotly.subplots import make_subplots")
	print("    import plotly.graph_objects as go")
	print("    df=indicator_data_level_2()")
	print("    df=df['{}_0']".format(i))
	print("    df=df['{}_1']".format(i))
	print("    df=df.reset_index()")
	print("    fig1=go.Figure()")
	print("    fig1.add_trace(go.Scatter(x=df['date'], y=df['{}_0'],name='{}_0'))".format(i,k))
	print("    fig1.add_trace(go.Scatter(x=df['date'], y=df['{}_1'],name='{}_1'))".format(i,k))
	print("    fig1.update_layout(title='{}',xaxis_title='Time',yaxis_title='{}')".format(k,k))
	print("    return fig1")
for k in listof3:
	i=texterconversion(k)
	print("def {}_Plot():".format(i))
	print("    from technicalta import indicator_data_level_3")
	print("    from plotly.subplots import make_subplots")
	print("    import plotly.graph_objects as go")
	print("    df=indicator_data_level_3()")
	print("    df=df['{}_0']".format(i))
	print("    df=df['{}_1']".format(i))
	print("    df=df['{}_2']".format(i))
	print("    df=df.reset_index()")
	print("    fig1=go.Figure()")
	print("    fig1.add_trace(go.Scatter(x=df['date'], y=df['{}_0'],name='{}_0'))".format(i,k))
	print("    fig1.add_trace(go.Scatter(x=df['date'], y=df['{}_1'],name='{}_1'))".format(i,k))
	print("    fig1.add_trace(go.Scatter(x=df['date'], y=df['{}_2'],name='{}_1'))".format(i,k))
	print("    fig1.update_layout(title='{}',xaxis_title='Time',yaxis_title='{}')".format(k,k))
	print("    return fig1")
'''