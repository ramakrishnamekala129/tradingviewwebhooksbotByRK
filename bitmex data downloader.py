# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 20:46:46 2019

@author: Ramakrishnamekala
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 19:31:56 2019

@author: Ramakrishnamekala
"""

import os
import sys
import csv
import pandas as pd
import ccxt  # noqa: E402

def retry_fetch_ohlcv(exchange, max_retries, symbol, timeframe, since, limit):
    num_retries = 0
    try:
        num_retries += 1
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since, limit)
        # print('Fetched', len(ohlcv), symbol, 'candles from', exchange.iso8601 (ohlcv[0][0]), 'to', exchange.iso8601 (ohlcv[-1][0]))
        return ohlcv
    except Exception:
        if num_retries > max_retries:
            raise  # Exception('Failed to fetch', timeframe, symbol, 'OHLCV in', max_retries, 'attempts')

def scrape_ohlcv(exchange, max_retries, symbol, timeframe, since, limit):
    earliest_timestamp = exchange.milliseconds()
    timeframe_duration_in_seconds = exchange.parse_timeframe(timeframe)
    timeframe_duration_in_ms = timeframe_duration_in_seconds * 1000
    timedelta = limit * timeframe_duration_in_ms
    all_ohlcv = []
    while True:
        fetch_since = earliest_timestamp - timedelta
        ohlcv = retry_fetch_ohlcv(exchange, max_retries, symbol, timeframe, fetch_since, limit)
        #print(earliest_timestamp)
        # if we have reached the beginning of history
        if ohlcv[0][0] >= earliest_timestamp:
            break
        earliest_timestamp = ohlcv[0][0]
        all_ohlcv = ohlcv + all_ohlcv
        print(len(all_ohlcv), 'candles in total from', exchange.iso8601(all_ohlcv[0][0]), 'to', exchange.iso8601(all_ohlcv[-1][0]))
        # if we have reached the checkpoint
        if fetch_since < since:
            break
    return all_ohlcv

def scrape_candles_to_csv(exchange_id, max_retries, symbol, timeframe, since, limit):
    # instantiate the exchange by id
    exchange = getattr(ccxt, exchange_id)({
        'enableRateLimit': True,  # required by the Manual
    })
    # convert since from string to milliseconds integer if needed
    if isinstance(since, str):
        since = exchange.parse8601(since)
    exchange.load_markets()
    ohlcv = scrape_ohlcv(exchange, max_retries, symbol, timeframe, since, limit)
    return ohlcv

# -----------------------------------------------------------------------------
#format to entry is 'ETH-USD'
saved=['ETH/USD','BTC/USD']
#saved=saved.replace('-','/')
print(saved)
tf='1m'
from pprint import pprint
'''
for save in saved: 
    dfe=scrape_candles_to_csv('bitmex', 5, save, tf, '2020-05-01T00:00:00Z', 1000)#[::-1]
    pprint(dfe)
    dfe = pd.DataFrame(dfe,columns=['date','open','high','low','close','volume'])
    save=save.replace('/','-')
    try:
        f = open("{}.csv".format(save))
        df = pd.read_csv('{}.csv'.format(save)).append(dfe)
        print(df.head())
        df.to_csv('{}_{}.csv'.format(save,tf), sep=',', index=False)

        # Do something with the file
    except IOError:
        print("File not accessible")
    finally:
        dfe.to_csv('{}_{}.csv'.format(save,tf), sep=',', index=False)
'''

    
