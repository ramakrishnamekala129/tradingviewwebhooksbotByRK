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
from pprint import pprint
from database import db
import os
import sys
import csv
import pandas as pd
import ccxt  # noqa: E402
import json
from datetime import datetime
import dateutil
from datetime import timedelta
import pymongo
def retry_fetch_ohlcv(exchange, max_retries, symbol, timeframe, since, limited):
    num_retries = 0
    try:
        num_retries += 1
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since, limited)
        # print('Fetched', len(ohlcv), symbol, 'candles from', exchange.iso8601 (ohlcv[0][0]), 'to', exchange.iso8601 (ohlcv[-1][0]))
        return ohlcv
    except Exception:
        if num_retries > max_retries:
            raise  # Exception('Failed to fetch', timeframe, symbol, 'OHLCV in', max_retries, 'attempts')

def scrape_ohlcv(exchange, max_retries, symbol, timeframe, since, limited):
    earliest_timestamp = exchange.milliseconds()
    timeframe_duration_in_seconds = exchange.parse_timeframe(timeframe)
    timeframe_duration_in_ms = timeframe_duration_in_seconds * 1000
    timedelta = limited * timeframe_duration_in_ms
    all_ohlcv = []
    while True:
        fetch_since = earliest_timestamp - timedelta
        ohlcv = retry_fetch_ohlcv(exchange, max_retries, symbol, timeframe, fetch_since, limited)
        #print(earliest_timestamp)
        # if we have reached the beginning of history
        if ohlcv == None:
            print('Waiting for new OHLCV')
        elif ohlcv:
            if ohlcv[0][0] >= earliest_timestamp:
                break
            earliest_timestamp = ohlcv[0][0]
            all_ohlcv = ohlcv + all_ohlcv
            #print(len(all_ohlcv), 'candles in total from', exchange.iso8601(all_ohlcv[0][0]), 'to', exchange.iso8601(all_ohlcv[-1][0]))
            # if we have reached the checkpoint
            if fetch_since < since:
                break
        else:
            print('Waiting for new OHLCV')
    return all_ohlcv

def scrape_candles_to_csv(exchange_id, max_retries, symbol, timeframe, since, limited):
    # instantiate the exchange by id
    exchange = getattr(ccxt, exchange_id)({
        'enableRateLimit': True,  # required by the Manual
    })
    # convert since from string to milliseconds integer if needed
    if isinstance(since, str):
        since = exchange.parse8601(since)
    exchange.load_markets()
    ohlcv = scrape_ohlcv(exchange, max_retries, symbol, timeframe, since, limited)
    return ohlcv

# -----------------------------------------------------------------------------
#format to entry is 'ETH-USD'

#saved=saved.replace('-','/')

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
#from_start='2020-05-01T00:00:00Z'
exchange='binance'
def dataexchange():
    exchange = ccxt.binance({
    'rateLimit': 10000,
    'enableRateLimit': True,
    # 'verbose': True,
    })
    return exchange


#from_start=datetime.now()-timedelta(days=15)
#from_start=from_start.isoformat()
#for save in saved: 

def datadownload(exchange, retry, coin, tf,from_start , limited):
    dfe=scrape_candles_to_csv(exchange, retry, coin, tf,from_start , limited)
    coin=coin.replace('/','')
    dfe = pd.DataFrame(dfe,columns=['date','Open','High','Low','Close','Volume'])
    dfe['date'] =pd.DataFrame(dfe['date'].apply(dataexchange().iso8601))
    records = json.loads(dfe.T.to_json()).values()
    #pprint(dfe)
    #pprint(records)
    dba='{}_{}'.format(coin,tf).replace('/','_')
    for record in records:
        if dba in db.list_collection_names():
            
            check=db[dba].find_one({'date':dateutil.parser.isoparse(record['date'])})
            if check == None:
                post={
                'date':dateutil.parser.isoparse(record['date']),
                'Open':record['Open'],
                'High':record['High'],
                'Low':record['Low'],
                'Close':record['Close'],
                'Volume':record['Volume']
                }
            
                save_excel = db[dba].insert_one(post)
                #print(save_excel)

        elif not dba in db.list_collection_names():
            post={
            'date':dateutil.parser.isoparse(record['date']),
            'Open':record['Open'],
            'High':record['High'],
            'Low':record['Low'],
            'Close':record['Close'],
            'Volume':record['Volume']
            }
        
            save_excel = db[dba].insert_one(post)
            #print(save_excel)
        else:
            print('Error ocurred in datadownload module')


def timingdelta(tf):
    if tf== '1m':
        tf=timedelta(minutes=1)
    elif tf == '5m':
        tf=timedelta(minutes=5)
    elif tf == '15m':
        tf=timedelta(minutes=15)
    elif tf == '30m':
        tf=timedelta(minutes=30)
    elif tf == '45m':
        tf=timedelta(minutes=45)
    elif tf == '1h':
        tf=timedelta(hours=1)
    elif tf == '2h':
        tf=timedelta(hours=2)
    elif tf == '4h':
        tf=timedelta(hours=4)
    elif tf == '12h':
        tf=timedelta(hours=12)
    elif tf == '1d':
        tf=timedelta(days=1)
    else:
        print('Error ocurred in Timedelta function')
    return tf
    
def historydataduration(tf):
    if tf== '1m':
        tf=timedelta(days=2)
    elif tf == '5m':
        tf=timedelta(days=5)
    elif tf == '15m':
        tf=timedelta(days=15)
    elif tf == '30m':
        tf=timedelta(days=30)
    elif tf == '45m':
        tf=timedelta(days=45)
    elif tf == '1h':
        tf=timedelta(weeks=10)
    elif tf == '2h':
        tf=timedelta(weeks=15)
    elif tf == '4h':
        tf=timedelta(weeks=20)
    elif tf == '12h':
        tf=timedelta(weeks=54)
    elif tf == '1d':
        tf=timedelta(weeks=108)
    else:
        print('Error ocurred in Timedelta function')
    return tf

    
#limit=1000
ex='binance'
#tf=['5m','1m','15m','1h','2h','4h','12h','1d','30m']
#saved=['ETH/USDT','BTC/USDT']

def historic(symbol,timeframe,limited):
    coin = '{}_{}'.format(symbol,timeframe).replace('/','')
    #print(coin)#if 
    print(coin)
    if coin in db.list_collection_names():
        if db[coin]:
            data=list(db[coin].find().sort("_id", pymongo.DESCENDING).limit(1))[0]

            date=data['date']
            current_time=datetime.now().timestamp()
            timestamp=datetime.timestamp(data['date'])
            #if current_time < timestamp:
            date=datetime.fromtimestamp(timestamp)
            time=date+timingdelta(timeframe)
            time=time.isoformat()
            limited=limited
            datadownload(ex, 5, symbol, timeframe,time , limited)

            #print(time)
    elif not coin in db.list_collection_names():
        from_start=datetime.now()-historydataduration(timeframe)
        from_start=from_start.isoformat()
        datadownload(ex, 5, symbol, timeframe,from_start,limited)
        print(from_start)
    else:
        print('Error Ocurred in History Data Download')
def drop_data(symbol,timeframe):
    coin = '{}_{}'.format(symbol,timeframe).replace('/','')
    db[coin].drop()

def datamanagement(symbol,timeframe,len):
    coin = '{}_{}'.format(symbol,timeframe).replace('/','')
    #len=10000
    if coin in db.list_collection_names():
        if db[coin].estimated_document_count() > len:
            count=db[coin].estimated_document_count()-len
            listed=list(db[coin].find())[:count]
            for dele in listed:
                db[coin].delete_one({'_id':dele['_id']})



'''
for save in saved:
    for timeframe in tf:

'''
'''
for save in saved:
    for timeframe in tf:
        def datamanagement(symbol,timeframe):
            coin = '{}_{}'.format(symbol,timeframe).replace('/','')
            len=10000
            if coin in db.list_collection_names():
                if db[coin].estimated_document_count() > len:
                    count=db[coin].estimated_document_count()-len
                    listed=list(db[coin].find())[:count]
                    for dele in listed:
                        db[coin].delete_one({'_id':dele['_id']})
'''
'''
for save in saved:
    for timeframe in tf:
        def drop_data(symbol,timeframe):
            coin = '{}_{}'.format(symbol,timeframe).replace('/','')
            db[coin].drop()
'''

'''
k=db['ETH-USDT_1m'].find_one()
t=datetime.timestamp(k['date'])
q=datetime.fromtimestamp(t).isoformat()
print(q)
print(t)
d=datetime.fromtimestamp(t)
print(d)
'''