import ccxt
import ast
import requests
#import webhook_bot
import datetime
from database import db
import json
import time
import pymongo
import pandas as pd
from historicdownloader import historic,datamanagement,drop_data
from technical import qtpylib
import chart_studio.plotly as py
import plotly.graph_objs as go
from technicalta import *



account=list(db.account.find())[-1]
exchange = ccxt.bitmex({
# Inset your API key and secrets for exchange in question.

'apiKey': account['apikey'],
'secret': account['apisecret'],
'enableRateLimit': True,
})




'''
exchange = ccxt.bitmex({
# Inset your API key and secrets for exchange in question.
'apiKey': 'kYYW-m1v7wESbEWkiUKi9sSz',
'secret': 'YUpGzV9OeflUpxwkTbGabXpS-z1_rf1jIXtuw0BeM6Q8N95B',
'enableRateLimit': True,
})
'''
'''
exchange = ccxt.bitmex({
# Inset your API key and secrets for exchange in question.
'apiKey': 'zyJugo0S3vFPoz6GzN4K5d9g',
'secret': 'C0vaVa39aFNPMJ1RjXfdlrmZzu0aT7GO0rOHilOSqfHh8Cdn',
'enableRateLimit': True,
})
'''
from pprint import pprint
def parse_webhook(webhook_data):

    """
    This function takes the string from tradingview and turns it into a python dict.
    :param webhook_data: POST data from tradingview, as a string.
    :return: Dictionary version of string.
    """

    data = ast.literal_eval(webhook_data)
    return data


def calc_price(given_price):

    """
    Will use this function to calculate the price for limit orders.
    :return: calculated limit price
    """

    if given_price == None:
        price = given_price
    else:
        price = given_price
    return price


'''def send_order(data):

    """
    This function sends the order to the exchange using ccxt.
    :param data: python dict, with keys as the API parameters.
    :return: the response from the exchange.
    """

    # Replace kraken with your exchange of choice.
    exchange = ccxt.bitmex({
        # Inset your API key and secrets for exchange in question.
        'apiKey': 'kYYW-m1v7wESbEWkiUKi9sSz',
        'secret': 'YUpGzV9OeflUpxwkTbGabXpS-z1_rf1jIXtuw0BeM6Q8N95B',
        'enableRateLimit': True,
    })

    # Send the order to the exchange, using the values from the tradingview alert.
    print('Sending:', data['symbol'], data['type'], data['side'], data['amount'], calc_price(data['price']))
    order = exchange.create_order(data['symbol'], data['type'], data['side'], data['amount'], calc_price(data['price']))
    # This is the last step, the response from the exchange will tell us if it made it and what errors pop up if not.
    print('Exchange Response:', order)
'''
def send_order(data,exchange=exchange):
    #print('Sending:', data['symbol'], data['type'], data['side'], data['amount'], calc_price(data['price']))
    if data['type'] == 'limit':
        #print('Sending:', data['symbol'], data['type'], data['side'], data['amount'], calc_price(data['price']))
        order = exchange.create_order(data['symbol'], data['type'], data['side'], data['amount'], calc_price(data['price']))
        # This is the last step, the response from the exchange will tell us if it made it and what errors pop up if not.
        print('Exchange Response:', order)
    if data['type']=='market':
        lastprice=exchange.fetch_ticker(data['symbol'])
        #print('Sending:', data['symbol'], data['type'], data['side'], data['amount'], calc_price(lastprice['close']))
        order = exchange.create_order(data['symbol'], data['type'], data['side'], data['amount'])
        # This is the last step, the response from the exchange will tell us if it made it and what errors pop up if not.
        print('Exchange Response:', order)
    return order

def lastpositions(symbol):
    if symbol == ('BTCUSD' or 'XBTUSD' or 'BTC/USDT' or 'BTC/USD'):
        symbol ='XBTUSD'
    elif symbol == ('ETHUSD' or 'ETH/USDT' or 'ETH/USD'):
        symbol='ETHUSD'
    else:
        print('Enter Valid Coin')
        #break        
    data=db.position.find_one({'symbol':symbol},sort=[("_id", pymongo.DESCENDING)])
    #eth=list(db.position.find({'symbol':'ETHUSD'}))[-1]
    if data:
        post={
                'date':data['date'],
                'symbol':data['symbol'],
                'leverage':data['leverage'],
                'currentQty':data['currentQty'],
                'isOpen':data['isOpen'],
                'markPrice':data['markPrice'],
                'realisedPnl':round(actual_value(data['realisedPnl']),4),
                'unrealisedPnl':round(actual_value(data['unrealisedPnl']),4),
                'lastPrice':data['lastPrice']
        }
        return post
def balance(exchange=exchange):
    data=exchange.fetch_balance()
    info=data['info'][0]
    btc=data['BTC']
    return info ,btc
def last_order(exchange=exchange):
    orders = exchange.fetch_closed_orders()

    prevorders=orders[0]
    lastorders={'id': prevorders['id']
    , 'timestamp': prevorders['timestamp']
    ,'datetime': prevorders['datetime']
    ,'lastTradeTimestamp': prevorders['lastTradeTimestamp']
    , 'symbol': prevorders['symbol']
    , 'type': prevorders['type']
    , 'side': prevorders['side']
    , 'price': prevorders['price']
    , 'amount': prevorders['amount']
    , 'cost': prevorders['cost']
    , 'average': prevorders['average']
    , 'filled': prevorders['filled']
    , 'remaining': prevorders['remaining']
    , 'status': prevorders['status']
    , 'fee': prevorders['fee']}

    print(lastorders)
    return lastorders

def percentage(symbol,percent):
  from actions import balance
  balance=balance()
  balance=balance[1]['free']
  price=list(db.btcusdt.find().sort("_id", pymongo.DESCENDING).limit(1))[0]['close']
  capacity=price*balance
  if symbol == 'BTC/USD':
    price=list(db.btcusdt.find().sort("_id", pymongo.DESCENDING).limit(1))[0]['close']
  elif symbol == 'ETH/USD':
    price=list(db.ethusdt.find().sort("_id", pymongo.DESCENDING).limit(1))[0]['close']
  else:
    price=price
  print(price)
  percent=percent*0.01
  amount=int(round(capacity,1))*percent
  amount=int(amount)
  return amount

def percent(percent):
  from actions import balance
  balance=balance()
  balance=balance[1]['free']
  price=list(db.btcusdt.find().sort("_id", pymongo.DESCENDING).limit(1))[0]['close']
  capacity=price*balance
  percent=percent*0.01
  amount=int(round(capacity,1))*percent
  amount=int(amount)
  return amount


def signaltonumber(signal):
    if signal == 'BUY':
        signal = 1
    elif signal == 'SELL':
        signal =-1
    else:
        print('Error')
    return signal
def TradinviewSignals():
    #while True:
    symbol=["BINANCE:BTCUSDT","BINANCE:ETHUSDT"]
    url="https://scanner.tradingview.com/crypto/scan"
    s='{"symbols":{"tickers":["BINANCE:BTCUSDT","BINANCE:ETHUSDT"],"query":{"types":[]}},"columns":["Recommend.Other|1","Recommend.All|1","Recommend.MA|1","Recommend.Other|5","Recommend.All|5","Recommend.MA|5","Recommend.Other|15","Recommend.All|15","Recommend.MA|15","Recommend.Other|60","Recommend.All|60","Recommend.MA|60","Recommend.Other|120","Recommend.All|120","Recommend.MA|120","Recommend.Other|240","Recommend.All|240","Recommend.MA|240","Recommend.Other","Recommend.All","Recommend.MA","Recommend.Other|1W","Recommend.All|1W","Recommend.MA|1W","Recommend.Other|1M","Recommend.All|1M","Recommend.MA|1M","close","open","high","low","volume"]}'#.format(symbol)
    u=requests.post(url,s).json()
    for i in range(0,len(u)):
        d=u['data'][i]['s'].replace("BINANCE:","").lower()
        if d == 'btcusdt':
            k=db['btcusdt']
        if d=='ethusdt':
            k=db['ethusdt']
        else:
            k=db[d]
        post={"date":datetime.datetime.utcnow(),"symbol":u['data'][i]['s'],
                    'recommendother1':u['data'][i]['d'][0],
                    'recommendall1':u['data'][i]['d'][1],
                    'recommendma1':u['data'][i]['d'][2],
                    'recommendother5':u['data'][i]['d'][3],
                    'recommendall5':u['data'][i]['d'][4],
                    'recommendma5':u['data'][i]['d'][5],
                    'recommendother15':u['data'][i]['d'][6],
                    'recommendall15':u['data'][i]['d'][7],
                    'recommendma15':u['data'][i]['d'][8],
                    'recommendother60':u['data'][i]['d'][9],
                    'recommendall60':u['data'][i]['d'][10],
                    'recommendma60':u['data'][i]['d'][11],
                    'recommendother240':u['data'][i]['d'][15],
                    'recommendall240':u['data'][i]['d'][16],
                    'recommendma240':u['data'][i]['d'][17],
                    'recommendother':u['data'][i]['d'][18],
                    'recommendall':u['data'][i]['d'][19],
                    'recommendma':u['data'][i]['d'][20],
                    'recommendother1w':u['data'][i]['d'][21],
                    'recommendall1w':u['data'][i]['d'][22],
                    'recommendma1w':u['data'][i]['d'][23],
                    'recommendother1m':u['data'][i]['d'][24],
                    'recommendall1m':u['data'][i]['d'][25],
                    'recommendma1m':u['data'][i]['d'][26],
                    'close':u['data'][i]['d'][27],
                    'open':u['data'][i]['d'][28],
                    'high':u['data'][i]['d'][29],
                    'low':u['data'][i]['d'][30],
                    'volume':u['data'][i]['d'][31]}

        d=k.insert_one(post).inserted_id
        print(d)
        #time.sleep(60)    
    return print("TradingView Signal Fetched")
def signals(signal):
    if signal == 0:
        msg = 'NEUTRAL'
        return msg
    elif signal>0.5:
        msg= 'STRONG BUY'
        return msg  
    elif signal>0:
        msg= 'BUY'
        return msg
    elif signal>-0.5:
        msg= 'SELL'
        return msg
    else:
        msg= 'STRONG SELL'
        return msg
def actual_value(data):
    data1=data*0.00000001
    return data1
def TradingView():
    #pw=list(db.btcusdt.find().sort("_id", pymongo.DESCENDING).limit(1))[0]
    pw=db.btcusdt.find_one(sort=[('_id',pymongo.DESCENDING)])
    #pw1=list(db.ethusdt.find().sort("_id", pymongo.DESCENDING).limit(1))[0]
    pw1=db.ethusdt.find_one(sort=[('_id',pymongo.DESCENDING)])
    p=pw
    p1=pw1
    p={
        'date':(p['date']),
        'symbol':(p['symbol']),
        'close':(p['close']),
        'recommendother1':signals(p['recommendother1']),
        'recommendall1':signals(p['recommendall1']),
        'recommendma1':signals(p['recommendma1']),
        'recommendother5':signals(p['recommendother5']),
        'recommendall5':signals(p['recommendall5']),
        'recommendma5':signals(p['recommendma5']),
        'recommendother15':signals(p['recommendother15']),
        'recommendall15':signals(p['recommendall15']),
        'recommendma15':signals(p['recommendma15']),
        'recommendother60':signals(p['recommendother60']),
        'recommendall60':signals(p['recommendall60']),
        'recommendma60':signals(p['recommendma60']),
        'recommendother240':signals(p['recommendother240']),
        'recommendall240':signals(p['recommendall240']),
        'recommendma240':signals(p['recommendma240']),
        'recommendother':signals(p['recommendother']),
        'recommendall':signals(p['recommendall']),
        'recommendma':signals(p['recommendma']),
        'recommendother1w':signals(p['recommendother1w']),
        'recommendall1w':signals(p['recommendall1w']),
        'recommendma1w':signals(p['recommendma1w']),
        'recommendother1m':signals(p['recommendother1m']),
        'recommendall1m':signals(p['recommendall1m']),
        'recommendma1m':signals(p['recommendma1m'])

        }
    p1={
        'date':(p1['date']),
        'symbol':(p1['symbol']),
        'close':p1['close'],
        'recommendother1':signals(p1['recommendother1']),
        'recommendall1':signals(p1['recommendall1']),
        'recommendma1':signals(p1['recommendma1']),
        'recommendother5':signals(p1['recommendother5']),
        'recommendall5':signals(p1['recommendall5']),
        'recommendma5':signals(p1['recommendma5']),
        'recommendother15':signals(p1['recommendother15']),
        'recommendall15':signals(p1['recommendall15']),
        'recommendma15':signals(p1['recommendma15']),
        'recommendother60':signals(p1['recommendother60']),
        'recommendall60':signals(p1['recommendall60']),
        'recommendma60':signals(p1['recommendma60']),
        'recommendother240':signals(p1['recommendother240']),
        'recommendall240':signals(p1['recommendall240']),
        'recommendma240':signals(p1['recommendma240']),
        'recommendother':signals(p1['recommendother']),
        'recommendall':signals(p1['recommendall']),
        'recommendma':signals(p1['recommendma']),
        'recommendother1w':signals(p1['recommendother1w']),
        'recommendall1w':signals(p1['recommendall1w']),
        'recommendma1w':signals(p1['recommendma1w']),
        'recommendother1m':signals(p1['recommendother1m']),
        'recommendall1m':signals(p1['recommendall1m']),
        'recommendma1m':signals(p1['recommendma1m'])

        }

    return p,p1


def senti():
    news=list(db.news.find().sort("_id", pymongo.DESCENDING).limit(100))
    return news
def lasttrades(i):
    data=list(db.trading.find().sort("_id", pymongo.DESCENDING).limit(15))
    data=data[i]
    post={
    'date':data['date'],
    'symbol':data['symbol'],
    'strategy':str(data['strategy']).upper(),
    'tradingview1':signals(data['tradingview1']),
    'tradingview5':signals(data['tradingview5']),
    'tradingview15':signals(data['tradingview15'])
        }
    return post
def entry(symbol,type,side,amount,price):
    if type == 'Market':
        response=exchange.create_order(symbol,type.lower(),side,amount,None)
    elif type == 'Limit':
        price=btcusdt['close']
        response=exchange.create_order(symbol,type.lower(),side,amount,int(price))
    else:
        response='Error Ocurred'
    return response,print(response)

def exit(symbol,type,side,amount,price,params):
    if type == 'Market':
        response=exchange.create_order(symbol,type.lower(),side,amount,None,params)
    elif type == 'Limit':
        response=exchange.create_order(symbol,type.lower(),side,amount,int(price),params)
    else:
        response='Error Ocurred'
    return response,print(response)


def StrategySelector(signal):
    if signal=='1_Min_ALL' :
        d='recommendall1'
        return d
    elif signal=='1_Min_MA' :
        d='recommendma1'
        return d
    elif signal=='1_Min_Osillator' :
        d='recommendother1'
        return d
    elif signal=='5_Min_ALL' :
        d='recommendall5'
        return d
    elif signal=='5_Min_MA' :
        d='recommendma5'
        return d
    elif signal=='5_Min_Osillator' :
        d='recommendother5'
        return d
    elif signal=='15_Min_ALL' :
        d='recommendall15'
        return d
    elif signal=='15_Min_MA' :
        d='recommendma15'
        return d
    elif signal=='15_Min_Osillator' :
        d='recommendother15'
        return d
    elif signal=='60_Min_ALL' :
        d='recommendall60'
        return d
    elif signal=='60_Min_MA' :
        d='recommendma60'
        return d
    elif signal=='60_Min_Osillator' :
        d='recommendother60'
        return d
    elif signal=='240_Min_ALL' :
        d='recommendall240'
        return d
    elif signal=='240_Min_MA' :
        d='recommendma240'
        return d
    elif signal=='240_Min_Osillator' :
        d='recommendother240'
        return d
    elif signal=='1_Day_ALL' :
        d='recommendall'
        return d
    elif signal=='1_Day_MA' :
        d='recommendma'
        return d
    elif signal=='1_Day_Osillator' :
        d='recommendother'
        return d
    elif signal=='1_Week_ALL' :
        d='recommendall1w'
        return d
    elif signal=='1_Week_MA' :
        d='recommendma1w'
        return d
    elif signal=='1_Week_Osillator' :
        d='recommendother1w'
        return d
    elif signal=='1_Month_ALL' :
        d='recommendall1m'
        return d
    elif signal=='1_Month_MA' :
        d='recommendma1m'
        return d
    elif signal=='1_Month_Osillator' :
        d='recommendother1m'
        return d
    else: 
        d=False
        print('Not Found Signal')
    return d


def historicaldatamanager():
    len=10000    
    limited=1000
    ex='binance'
    tf=['5m','1m','15m','1h','2h','4h','12h','1d','30m']
    symbols=['ETH/USDT','BTC/USDT']
    for timeframe in tf:
        for symbol in symbols:
            limit=limited
            historic(symbol,timeframe,limited)
            datamanagement(symbol,timeframe,len)
def deletehistoricaldatamanager():
    len=10000    
    limited=1000
    ex='binance'
    tf=['5m','1m','15m','1h','2h','4h','12h','1d','30m']
    symbols=['ETH/USDT','BTC/USDT']
    for timeframe in tf:
        for symbol in symbols:
            limit=limited
            drop_data(symbol,timeframe)



def Plotcandle(symbol,TimeFrame):
    coin='{}_{}'.format(symbol,TimeFrame).replace('/','')
    df=list(db[coin].find().sort('_id',pymongo.DESCENDING).limit(500))[::-1]
    print(df)
    df=pd.DataFrame(df)
    #df['date'] = pd.to_datetime(df['date'])
    df['open']=df['Open']
    df['close']=df['Close']
    df['high']=df['High']
    df['low']=df['Low']
    h=qtpylib.heikinashi(df)
    df['ha_open']=h['open']
    df['ha_high']=h['high']
    df['ha_low']=h['low']
    df['ha_close']=h['close']
    #df['date'] = pd.to_datetime(df["date"], format="%m/%d/%Y").dt.round("min")
    #df['date']=df['date'].drop_duplicates(keep='last')
    df=df.dropna()
    #df = pd.read_csv('Binance_BTCUSDT_1h.csv')
    # Create a trace
    data=[go.Candlestick(x=df['date'],
                open=df['ha_open'],
                high=df['ha_high'],
                low=df['ha_low'],
                close=df['ha_close'])]
    return data


def listed_technical():
    names=['BBANDS',
    'DEMA',
    'EMA',
    'HT_TRENDLINE',
    'KAMA',
    'MA',
    'MAMA',
    'MAVP',
    'MIDPOINT',
    'MIDPRICE',
    'SAR',
    'SAREXT',
    'SMA',
    'T3',
    'TEMA',
    'TRIMA',
    'WMA',
    'ADX',
    'ADXR',
    'APO',
    'AROON',
    'AROONOSC',
    'BOP',
    'CCI',
    'CMO',
    'DX',
    'MACD',
    'MACDEXT',
    'MACDFIX',
    'MFI',
    'MINUS_DI',
    'MINUS_DM',
    'MOM',
    'PLUS_DI',
    'PLUS_DM',
    'PPO',
    'ROC',
    'ROCP',
    'ROCR',
    'ROCR100',
    'RSI',
    'STOCH',
    'STOCHF',
    'STOCHRSI',
    'TRIX',
    'ULTOSC',
    'WILLR',
    'AD',
    'ADOSC',
    'OBV']
    function=[
    'Bollinger Bands',
    'Double Exponential Moving Average',
    'Exponential Moving Average',
    'Hilbert Transform - Instantaneous Trendline',
    'Kaufman Adaptive Moving Average',
    'Moving average',
    'MESA Adaptive Moving Average',
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
    'Aroon',
    'Aroon Oscillator',
    'Balance Of Power',
    'Commodity Channel Index',
    'Chande Momentum Oscillator',
    'Directional Movement Index',
    'Moving Average Convergence-Divergence',
    'MACD with controllable MA type',
    'Moving Average Convergence-Divergence Fix',
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
    'Stochastic',
    'Stochastic Fast',
    'Stochastic Relative Strength Index',
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
    return function,names



def technical_transform(technical):
    if technical == 'Bollinger Bands':
        technical='BBANDS'
    elif technical == 'Double Exponential Moving Average':
        technical='DEMA'
    elif technical == 'Exponential Moving Average':
        technical='EMA'
    elif technical == 'Hilbert Transform - Instantaneous Trendline':
        technical='HT_TRENDLINE'
    elif technical == 'Kaufman Adaptive Moving Average':
        technical='KAMA'
    elif technical == 'Moving average':
        technical='MA'
    elif technical == 'MESA Adaptive Moving Average':
        technical='MAMA'
    elif technical == 'Moving average with variable period':
        technical='MAVP'
    elif technical == 'MidPoint over period':
        technical='MIDPOINT'
    elif technical == 'Midpoint Price over period':
        technical='MIDPRICE'
    elif technical == 'Parabolic SAR':
        technical='SAR'
    elif technical == 'Parabolic SAR - Extended':
        technical='SAREXT'
    elif technical == 'Simple Moving Average':
        technical='SMA'
    elif technical == 'Triple Exponential Moving Average (T3)':
        technical='T3'
    elif technical == 'Triple Exponential Moving Average':
        technical='TEMA'
    elif technical == 'Triangular Moving Average':
        technical='TRIMA'
    elif technical == 'Weighted Moving Average':
        technical='WMA'
    elif technical == 'Average Directional Movement Index':
        technical='ADX'
    elif technical == 'Average Directional Movement Index Rating':
        technical='ADXR'
    elif technical == 'Absolute Price Oscillator':
        technical='APO'
    elif technical == 'Aroon':
        technical='AROON'
    elif technical == 'Aroon Oscillator':
        technical='AROONOSC'
    elif technical == 'Balance Of Power':
        technical='BOP'
    elif technical == 'Commodity Channel Index':
        technical='CCI'
    elif technical == 'Chande Momentum Oscillator':
        technical='CMO'
    elif technical == 'Directional Movement Index':
        technical='DX'
    elif technical == 'Moving Average Convergence-Divergence':
        technical='MACD'
    elif technical == 'MACD with controllable MA type':
        technical='MACDEXT'
    elif technical == 'Moving Average Convergence-Divergence Fix':
        technical='MACDFIX'
    elif technical == 'Money Flow Index':
        technical='MFI'
    elif technical == 'Minus Directional Indicator':
        technical='MINUS_DI'
    elif technical == 'Minus Directional Movement':
        technical='MINUS_DM'
    elif technical == 'Momentum':
        technical='MOM'
    elif technical == 'Plus Directional Indicator':
        technical='PLUS_DI'
    elif technical == 'Plus Directional Movement':
        technical='PLUS_DM'
    elif technical == 'Percentage Price Oscillator':
        technical='PPO'
    elif technical == 'Rate of change':
        technical='ROC'
    elif technical == 'Rate of change Percentage':
        technical='ROCP'
    elif technical == 'Rate of change ratio':
        technical='ROCR'
    elif technical == 'Rate of change ratio 100 scale':
        technical='ROCR100'
    elif technical == 'Relative Strength Index':
        technical='RSI'
    elif technical == 'Stochastic':
        technical='STOCH'
    elif technical == 'Stochastic Fast':
        technical='STOCHF'
    elif technical == 'Stochastic Relative Strength Index':
        technical='STOCHRSI'
    elif technical == 'one-day Rate-Of-Change ROC of a Triple Smooth EMA':
        technical='TRIX'
    elif technical == 'Ultimate Oscillator':
        technical='ULTOSC'
    elif technical == 'Williams':
        technical='WILLR'
    elif technical == 'Chaikin A/D Line':
        technical='AD'
    elif technical == 'Chaikin A/D Oscillator':
        technical='ADOSC'
    else:
        print('Error Ocurred in technical transformation')
    return technical

def NSE_TV():
    columns = ["open|1","open|5","open|15","open|60","open|240","open","open|1W","open|1M","high|1","high|5","high|15","high|60","high|240","high","high|1W","high|1M","low|1","low|5","low|15","low|60","low|240","low","low|1W","low|1M","close|1","close|5","close|15","close|60","close|240","close","close|1W","close|1M","volume|1","volume|5","volume|15","volume|60","volume|240","volume","volume|1W","volume|1M","Recommend.Other|1","Recommend.All|1","Recommend.MA|1","RSI|1","RSI[1]|1","Stoch.K|1","Stoch.D|1","Stoch.K[1]|1","Stoch.D[1]|1","CCI20|1","CCI20[1]|1","ADX|1","ADX+DI|1","ADX-DI|1","ADX+DI[1]|1","ADX-DI[1]|1","AO|1","AO[1]|1","Mom|1","Mom[1]|1","MACD.macd|1","MACD.signal|1","Rec.Stoch.RSI|1","Stoch.RSI.K|1","Rec.WR|1","W.R|1","Rec.BBPower|1","BBPower|1","Rec.UO|1","UO|1","EMA5|1","close|1","SMA5|1","EMA10|1","SMA10|1","EMA20|1","SMA20|1","EMA30|1","SMA30|1","EMA50|1","SMA50|1","EMA100|1","SMA100|1","EMA200|1","SMA200|1","Rec.Ichimoku|1","Ichimoku.BLine|1","Rec.VWMA|1","VWMA|1","Rec.HullMA9|1","HullMA9|1","Pivot.M.Classic.S3|1","Pivot.M.Classic.S2|1","Pivot.M.Classic.S1|1","Pivot.M.Classic.Middle|1","Pivot.M.Classic.R1|1","Pivot.M.Classic.R2|1","Pivot.M.Classic.R3|1","Pivot.M.Fibonacci.S3|1","Pivot.M.Fibonacci.S2|1","Pivot.M.Fibonacci.S1|1","Pivot.M.Fibonacci.Middle|1","Pivot.M.Fibonacci.R1|1","Pivot.M.Fibonacci.R2|1","Pivot.M.Fibonacci.R3|1","Pivot.M.Camarilla.S3|1","Pivot.M.Camarilla.S2|1","Pivot.M.Camarilla.S1|1","Pivot.M.Camarilla.Middle|1","Pivot.M.Camarilla.R1|1","Pivot.M.Camarilla.R2|1","Pivot.M.Camarilla.R3|1","Pivot.M.Woodie.S3|1","Pivot.M.Woodie.S2|1","Pivot.M.Woodie.S1|1","Pivot.M.Woodie.Middle|1","Pivot.M.Woodie.R1|1","Pivot.M.Woodie.R2|1","Pivot.M.Woodie.R3|1","Pivot.M.Demark.S1|1","Pivot.M.Demark.Middle|1","Pivot.M.Demark.R1|1","Recommend.Other|5","Recommend.All|5","Recommend.MA|5","RSI|5","RSI[1]|5","Stoch.K|5","Stoch.D|5","Stoch.K[1]|5","Stoch.D[1]|5","CCI20|5","CCI20[1]|5","ADX|5","ADX+DI|5","ADX-DI|5","ADX+DI[1]|5","ADX-DI[1]|5","AO|5","AO[1]|5","Mom|5","Mom[1]|5","MACD.macd|5","MACD.signal|5","Rec.Stoch.RSI|5","Stoch.RSI.K|5","Rec.WR|5","W.R|5","Rec.BBPower|5","BBPower|5","Rec.UO|5","UO|5","EMA5|5","close|5","SMA5|5","EMA10|5","SMA10|5","EMA20|5","SMA20|5","EMA30|5","SMA30|5","EMA50|5","SMA50|5","EMA100|5","SMA100|5","EMA200|5","SMA200|5","Rec.Ichimoku|5","Ichimoku.BLine|5","Rec.VWMA|5","VWMA|5","Rec.HullMA9|5","HullMA9|5","Pivot.M.Classic.S3|5","Pivot.M.Classic.S2|5","Pivot.M.Classic.S1|5","Pivot.M.Classic.Middle|5","Pivot.M.Classic.R1|5","Pivot.M.Classic.R2|5","Pivot.M.Classic.R3|5","Pivot.M.Fibonacci.S3|5","Pivot.M.Fibonacci.S2|5","Pivot.M.Fibonacci.S1|5","Pivot.M.Fibonacci.Middle|5","Pivot.M.Fibonacci.R1|5","Pivot.M.Fibonacci.R2|5","Pivot.M.Fibonacci.R3|5","Pivot.M.Camarilla.S3|5","Pivot.M.Camarilla.S2|5","Pivot.M.Camarilla.S1|5","Pivot.M.Camarilla.Middle|5","Pivot.M.Camarilla.R1|5","Pivot.M.Camarilla.R2|5","Pivot.M.Camarilla.R3|5","Pivot.M.Woodie.S3|5","Pivot.M.Woodie.S2|5","Pivot.M.Woodie.S1|5","Pivot.M.Woodie.Middle|5","Pivot.M.Woodie.R1|5","Pivot.M.Woodie.R2|5","Pivot.M.Woodie.R3|5","Pivot.M.Demark.S1|5","Pivot.M.Demark.Middle|5","Pivot.M.Demark.R1|5","Recommend.Other|15","Recommend.All|15","Recommend.MA|15","RSI|15","RSI[1]|15","Stoch.K|15","Stoch.D|15","Stoch.K[1]|15","Stoch.D[1]|15","CCI20|15","CCI20[1]|15","ADX|15","ADX+DI|15","ADX-DI|15","ADX+DI[1]|15","ADX-DI[1]|15","AO|15","AO[1]|15","Mom|15","Mom[1]|15","MACD.macd|15","MACD.signal|15","Rec.Stoch.RSI|15","Stoch.RSI.K|15","Rec.WR|15","W.R|15","Rec.BBPower|15","BBPower|15","Rec.UO|15","UO|15","EMA5|15","close|15","SMA5|15","EMA10|15","SMA10|15","EMA20|15","SMA20|15","EMA30|15","SMA30|15","EMA50|15","SMA50|15","EMA100|15","SMA100|15","EMA200|15","SMA200|15","Rec.Ichimoku|15","Ichimoku.BLine|15","Rec.VWMA|15","VWMA|15","Rec.HullMA9|15","HullMA9|15","Pivot.M.Classic.S3|15","Pivot.M.Classic.S2|15","Pivot.M.Classic.S1|15","Pivot.M.Classic.Middle|15","Pivot.M.Classic.R1|15","Pivot.M.Classic.R2|15","Pivot.M.Classic.R3|15","Pivot.M.Fibonacci.S3|15","Pivot.M.Fibonacci.S2|15","Pivot.M.Fibonacci.S1|15","Pivot.M.Fibonacci.Middle|15","Pivot.M.Fibonacci.R1|15","Pivot.M.Fibonacci.R2|15","Pivot.M.Fibonacci.R3|15","Pivot.M.Camarilla.S3|15","Pivot.M.Camarilla.S2|15","Pivot.M.Camarilla.S1|15","Pivot.M.Camarilla.Middle|15","Pivot.M.Camarilla.R1|15","Pivot.M.Camarilla.R2|15","Pivot.M.Camarilla.R3|15","Pivot.M.Woodie.S3|15","Pivot.M.Woodie.S2|15","Pivot.M.Woodie.S1|15","Pivot.M.Woodie.Middle|15","Pivot.M.Woodie.R1|15","Pivot.M.Woodie.R2|15","Pivot.M.Woodie.R3|15","Pivot.M.Demark.S1|15","Pivot.M.Demark.Middle|15","Pivot.M.Demark.R1|15","Recommend.Other|60","Recommend.All|60","Recommend.MA|60","RSI|60","RSI[1]|60","Stoch.K|60","Stoch.D|60","Stoch.K[1]|60","Stoch.D[1]|60","CCI20|60","CCI20[1]|60","ADX|60","ADX+DI|60","ADX-DI|60","ADX+DI[1]|60","ADX-DI[1]|60","AO|60","AO[1]|60","Mom|60","Mom[1]|60","MACD.macd|60","MACD.signal|60","Rec.Stoch.RSI|60","Stoch.RSI.K|60","Rec.WR|60","W.R|60","Rec.BBPower|60","BBPower|60","Rec.UO|60","UO|60","EMA5|60","close|60","SMA5|60","EMA10|60","SMA10|60","EMA20|60","SMA20|60","EMA30|60","SMA30|60","EMA50|60","SMA50|60","EMA100|60","SMA100|60","EMA200|60","SMA200|60","Rec.Ichimoku|60","Ichimoku.BLine|60","Rec.VWMA|60","VWMA|60","Rec.HullMA9|60","HullMA9|60","Pivot.M.Classic.S3|60","Pivot.M.Classic.S2|60","Pivot.M.Classic.S1|60","Pivot.M.Classic.Middle|60","Pivot.M.Classic.R1|60","Pivot.M.Classic.R2|60","Pivot.M.Classic.R3|60","Pivot.M.Fibonacci.S3|60","Pivot.M.Fibonacci.S2|60","Pivot.M.Fibonacci.S1|60","Pivot.M.Fibonacci.Middle|60","Pivot.M.Fibonacci.R1|60","Pivot.M.Fibonacci.R2|60","Pivot.M.Fibonacci.R3|60","Pivot.M.Camarilla.S3|60","Pivot.M.Camarilla.S2|60","Pivot.M.Camarilla.S1|60","Pivot.M.Camarilla.Middle|60","Pivot.M.Camarilla.R1|60","Pivot.M.Camarilla.R2|60","Pivot.M.Camarilla.R3|60","Pivot.M.Woodie.S3|60","Pivot.M.Woodie.S2|60","Pivot.M.Woodie.S1|60","Pivot.M.Woodie.Middle|60","Pivot.M.Woodie.R1|60","Pivot.M.Woodie.R2|60","Pivot.M.Woodie.R3|60","Pivot.M.Demark.S1|60","Pivot.M.Demark.Middle|60","Pivot.M.Demark.R1|60","Recommend.Other|240","Recommend.All|240","Recommend.MA|240","RSI|240","RSI[1]|240","Stoch.K|240","Stoch.D|240","Stoch.K[1]|240","Stoch.D[1]|240","CCI20|240","CCI20[1]|240","ADX|240","ADX+DI|240","ADX-DI|240","ADX+DI[1]|240","ADX-DI[1]|240","AO|240","AO[1]|240","Mom|240","Mom[1]|240","MACD.macd|240","MACD.signal|240","Rec.Stoch.RSI|240","Stoch.RSI.K|240","Rec.WR|240","W.R|240","Rec.BBPower|240","BBPower|240","Rec.UO|240","UO|240","EMA5|240","close|240","SMA5|240","EMA10|240","SMA10|240","EMA20|240","SMA20|240","EMA30|240","SMA30|240","EMA50|240","SMA50|240","EMA100|240","SMA100|240","EMA200|240","SMA200|240","Rec.Ichimoku|240","Ichimoku.BLine|240","Rec.VWMA|240","VWMA|240","Rec.HullMA9|240","HullMA9|240","Pivot.M.Classic.S3|240","Pivot.M.Classic.S2|240","Pivot.M.Classic.S1|240","Pivot.M.Classic.Middle|240","Pivot.M.Classic.R1|240","Pivot.M.Classic.R2|240","Pivot.M.Classic.R3|240","Pivot.M.Fibonacci.S3|240","Pivot.M.Fibonacci.S2|240","Pivot.M.Fibonacci.S1|240","Pivot.M.Fibonacci.Middle|240","Pivot.M.Fibonacci.R1|240","Pivot.M.Fibonacci.R2|240","Pivot.M.Fibonacci.R3|240","Pivot.M.Camarilla.S3|240","Pivot.M.Camarilla.S2|240","Pivot.M.Camarilla.S1|240","Pivot.M.Camarilla.Middle|240","Pivot.M.Camarilla.R1|240","Pivot.M.Camarilla.R2|240","Pivot.M.Camarilla.R3|240","Pivot.M.Woodie.S3|240","Pivot.M.Woodie.S2|240","Pivot.M.Woodie.S1|240","Pivot.M.Woodie.Middle|240","Pivot.M.Woodie.R1|240","Pivot.M.Woodie.R2|240","Pivot.M.Woodie.R3|240","Pivot.M.Demark.S1|240","Pivot.M.Demark.Middle|240","Pivot.M.Demark.R1|240","Recommend.Other","Recommend.All","Recommend.MA","RSI","RSI[1]","Stoch.K","Stoch.D","Stoch.K[1]","Stoch.D[1]","CCI20","CCI20[1]","ADX","ADX+DI","ADX-DI","ADX+DI[1]","ADX-DI[1]","AO","AO[1]","Mom","Mom[1]","MACD.macd","MACD.signal","Rec.Stoch.RSI","Stoch.RSI.K","Rec.WR","W.R","Rec.BBPower","BBPower","Rec.UO","UO","EMA5","close","SMA5","EMA10","SMA10","EMA20","SMA20","EMA30","SMA30","EMA50","SMA50","EMA100","SMA100","EMA200","SMA200","Rec.Ichimoku","Ichimoku.BLine","Rec.VWMA","VWMA","Rec.HullMA9","HullMA9","Pivot.M.Classic.S3","Pivot.M.Classic.S2","Pivot.M.Classic.S1","Pivot.M.Classic.Middle","Pivot.M.Classic.R1","Pivot.M.Classic.R2","Pivot.M.Classic.R3","Pivot.M.Fibonacci.S3","Pivot.M.Fibonacci.S2","Pivot.M.Fibonacci.S1","Pivot.M.Fibonacci.Middle","Pivot.M.Fibonacci.R1","Pivot.M.Fibonacci.R2","Pivot.M.Fibonacci.R3","Pivot.M.Camarilla.S3","Pivot.M.Camarilla.S2","Pivot.M.Camarilla.S1","Pivot.M.Camarilla.Middle","Pivot.M.Camarilla.R1","Pivot.M.Camarilla.R2","Pivot.M.Camarilla.R3","Pivot.M.Woodie.S3","Pivot.M.Woodie.S2","Pivot.M.Woodie.S1","Pivot.M.Woodie.Middle","Pivot.M.Woodie.R1","Pivot.M.Woodie.R2","Pivot.M.Woodie.R3","Pivot.M.Demark.S1","Pivot.M.Demark.Middle","Pivot.M.Demark.R1","Recommend.Other|1W","Recommend.All|1W","Recommend.MA|1W","RSI|1W","RSI[1]|1W","Stoch.K|1W","Stoch.D|1W","Stoch.K[1]|1W","Stoch.D[1]|1W","CCI20|1W","CCI20[1]|1W","ADX|1W","ADX+DI|1W","ADX-DI|1W","ADX+DI[1]|1W","ADX-DI[1]|1W","AO|1W","AO[1]|1W","Mom|1W","Mom[1]|1W","MACD.macd|1W","MACD.signal|1W","Rec.Stoch.RSI|1W","Stoch.RSI.K|1W","Rec.WR|1W","W.R|1W","Rec.BBPower|1W","BBPower|1W","Rec.UO|1W","UO|1W","EMA5|1W","close|1W","SMA5|1W","EMA10|1W","SMA10|1W","EMA20|1W","SMA20|1W","EMA30|1W","SMA30|1W","EMA50|1W","SMA50|1W","EMA100|1W","SMA100|1W","EMA200|1W","SMA200|1W","Rec.Ichimoku|1W","Ichimoku.BLine|1W","Rec.VWMA|1W","VWMA|1W","Rec.HullMA9|1W","HullMA9|1W","Pivot.M.Classic.S3|1W","Pivot.M.Classic.S2|1W","Pivot.M.Classic.S1|1W","Pivot.M.Classic.Middle|1W","Pivot.M.Classic.R1|1W","Pivot.M.Classic.R2|1W","Pivot.M.Classic.R3|1W","Pivot.M.Fibonacci.S3|1W","Pivot.M.Fibonacci.S2|1W","Pivot.M.Fibonacci.S1|1W","Pivot.M.Fibonacci.Middle|1W","Pivot.M.Fibonacci.R1|1W","Pivot.M.Fibonacci.R2|1W","Pivot.M.Fibonacci.R3|1W","Pivot.M.Camarilla.S3|1W","Pivot.M.Camarilla.S2|1W","Pivot.M.Camarilla.S1|1W","Pivot.M.Camarilla.Middle|1W","Pivot.M.Camarilla.R1|1W","Pivot.M.Camarilla.R2|1W","Pivot.M.Camarilla.R3|1W","Pivot.M.Woodie.S3|1W","Pivot.M.Woodie.S2|1W","Pivot.M.Woodie.S1|1W","Pivot.M.Woodie.Middle|1W","Pivot.M.Woodie.R1|1W","Pivot.M.Woodie.R2|1W","Pivot.M.Woodie.R3|1W","Pivot.M.Demark.S1|1W","Pivot.M.Demark.Middle|1W","Pivot.M.Demark.R1|1W","Recommend.Other|1M","Recommend.All|1M","Recommend.MA|1M","RSI|1M","RSI[1]|1M","Stoch.K|1M","Stoch.D|1M","Stoch.K[1]|1M","Stoch.D[1]|1M","CCI20|1M","CCI20[1]|1M","ADX|1M","ADX+DI|1M","ADX-DI|1M","ADX+DI[1]|1M","ADX-DI[1]|1M","AO|1M","AO[1]|1M","Mom|1M","Mom[1]|1M","MACD.macd|1M","MACD.signal|1M","Rec.Stoch.RSI|1M","Stoch.RSI.K|1M","Rec.WR|1M","W.R|1M","Rec.BBPower|1M","BBPower|1M","Rec.UO|1M","UO|1M","EMA5|1M","close|1M","SMA5|1M","EMA10|1M","SMA10|1M","EMA20|1M","SMA20|1M","EMA30|1M","SMA30|1M","EMA50|1M","SMA50|1M","EMA100|1M","SMA100|1M","EMA200|1M","SMA200|1M","Rec.Ichimoku|1M","Ichimoku.BLine|1M","Rec.VWMA|1M","VWMA|1M","Rec.HullMA9|1M","HullMA9|1M","Pivot.M.Classic.S3|1M","Pivot.M.Classic.S2|1M","Pivot.M.Classic.S1|1M","Pivot.M.Classic.Middle|1M","Pivot.M.Classic.R1|1M","Pivot.M.Classic.R2|1M","Pivot.M.Classic.R3|1M","Pivot.M.Fibonacci.S3|1M","Pivot.M.Fibonacci.S2|1M","Pivot.M.Fibonacci.S1|1M","Pivot.M.Fibonacci.Middle|1M","Pivot.M.Fibonacci.R1|1M","Pivot.M.Fibonacci.R2|1M","Pivot.M.Fibonacci.R3|1M","Pivot.M.Camarilla.S3|1M","Pivot.M.Camarilla.S2|1M","Pivot.M.Camarilla.S1|1M","Pivot.M.Camarilla.Middle|1M","Pivot.M.Camarilla.R1|1M","Pivot.M.Camarilla.R2|1M","Pivot.M.Camarilla.R3|1M","Pivot.M.Woodie.S3|1M","Pivot.M.Woodie.S2|1M","Pivot.M.Woodie.S1|1M","Pivot.M.Woodie.Middle|1M","Pivot.M.Woodie.R1|1M","Pivot.M.Woodie.R2|1M","Pivot.M.Woodie.R3|1M","Pivot.M.Demark.S1|1M","Pivot.M.Demark.Middle|1M","Pivot.M.Demark.R1|1M"]
    URL="https://scanner.tradingview.com/india/scan"
    HEADER='{"symbols":{"tickers":["NSE:ADANIPORTS","NSE:ASIANPAINT","NSE:AXISBANK","NSE:BAJAJ-AUTO","NSE:BAJFINANCE","NSE:BAJAJFINSV","NSE:BHARTIARTL","NSE:INFRATEL","NSE:BPCL","NSE:BRITANNIA","NSE:CIPLA","NSE:COALINDIA","NSE:DRREDDY","NSE:EICHERMOT","NSE:GAIL","NSE:GRASIM","NSE:HCLTECH","NSE:HDFC","NSE:HDFCBANK","NSE:HEROMOTOCO","NSE:HINDALCO","NSE:HINDUNILVR","NSE:ICICIBANK","NSE:INDUSINDBK","NSE:INFY","NSE:IOC","NSE:ITC","NSE:JSWSTEEL","NSE:KOTAKBANK","NSE:LT","NSE:M&M","NSE:MARUTI","NSE:NESTLEIND","NSE:NTPC","NSE:ONGC","NSE:POWERGRID","NSE:RELIANCE","NSE:SHREECEM","NSE:SBIN","NSE:SUNPHARMA","NSE:TCS","NSE:TATAMOTORS","NSE:TATASTEEL","NSE:TECHM","NSE:TITAN","NSE:ULTRACEMCO","NSE:UPL","NSE:VEDL","NSE:WIPRO","NSE:ZEEL"],"query":{"types":[]}},"columns":["open|1","open|5","open|15","open|60","open|240","open","open|1W","open|1M","high|1","high|5","high|15","high|60","high|240","high","high|1W","high|1M","low|1","low|5","low|15","low|60","low|240","low","low|1W","low|1M","close|1","close|5","close|15","close|60","close|240","close","close|1W","close|1M","volume|1","volume|5","volume|15","volume|60","volume|240","volume","volume|1W","volume|1M","Recommend.Other|1","Recommend.All|1","Recommend.MA|1","RSI|1","RSI[1]|1","Stoch.K|1","Stoch.D|1","Stoch.K[1]|1","Stoch.D[1]|1","CCI20|1","CCI20[1]|1","ADX|1","ADX+DI|1","ADX-DI|1","ADX+DI[1]|1","ADX-DI[1]|1","AO|1","AO[1]|1","Mom|1","Mom[1]|1","MACD.macd|1","MACD.signal|1","Rec.Stoch.RSI|1","Stoch.RSI.K|1","Rec.WR|1","W.R|1","Rec.BBPower|1","BBPower|1","Rec.UO|1","UO|1","EMA5|1","close|1","SMA5|1","EMA10|1","SMA10|1","EMA20|1","SMA20|1","EMA30|1","SMA30|1","EMA50|1","SMA50|1","EMA100|1","SMA100|1","EMA200|1","SMA200|1","Rec.Ichimoku|1","Ichimoku.BLine|1","Rec.VWMA|1","VWMA|1","Rec.HullMA9|1","HullMA9|1","Pivot.M.Classic.S3|1","Pivot.M.Classic.S2|1","Pivot.M.Classic.S1|1","Pivot.M.Classic.Middle|1","Pivot.M.Classic.R1|1","Pivot.M.Classic.R2|1","Pivot.M.Classic.R3|1","Pivot.M.Fibonacci.S3|1","Pivot.M.Fibonacci.S2|1","Pivot.M.Fibonacci.S1|1","Pivot.M.Fibonacci.Middle|1","Pivot.M.Fibonacci.R1|1","Pivot.M.Fibonacci.R2|1","Pivot.M.Fibonacci.R3|1","Pivot.M.Camarilla.S3|1","Pivot.M.Camarilla.S2|1","Pivot.M.Camarilla.S1|1","Pivot.M.Camarilla.Middle|1","Pivot.M.Camarilla.R1|1","Pivot.M.Camarilla.R2|1","Pivot.M.Camarilla.R3|1","Pivot.M.Woodie.S3|1","Pivot.M.Woodie.S2|1","Pivot.M.Woodie.S1|1","Pivot.M.Woodie.Middle|1","Pivot.M.Woodie.R1|1","Pivot.M.Woodie.R2|1","Pivot.M.Woodie.R3|1","Pivot.M.Demark.S1|1","Pivot.M.Demark.Middle|1","Pivot.M.Demark.R1|1","Recommend.Other|5","Recommend.All|5","Recommend.MA|5","RSI|5","RSI[1]|5","Stoch.K|5","Stoch.D|5","Stoch.K[1]|5","Stoch.D[1]|5","CCI20|5","CCI20[1]|5","ADX|5","ADX+DI|5","ADX-DI|5","ADX+DI[1]|5","ADX-DI[1]|5","AO|5","AO[1]|5","Mom|5","Mom[1]|5","MACD.macd|5","MACD.signal|5","Rec.Stoch.RSI|5","Stoch.RSI.K|5","Rec.WR|5","W.R|5","Rec.BBPower|5","BBPower|5","Rec.UO|5","UO|5","EMA5|5","close|5","SMA5|5","EMA10|5","SMA10|5","EMA20|5","SMA20|5","EMA30|5","SMA30|5","EMA50|5","SMA50|5","EMA100|5","SMA100|5","EMA200|5","SMA200|5","Rec.Ichimoku|5","Ichimoku.BLine|5","Rec.VWMA|5","VWMA|5","Rec.HullMA9|5","HullMA9|5","Pivot.M.Classic.S3|5","Pivot.M.Classic.S2|5","Pivot.M.Classic.S1|5","Pivot.M.Classic.Middle|5","Pivot.M.Classic.R1|5","Pivot.M.Classic.R2|5","Pivot.M.Classic.R3|5","Pivot.M.Fibonacci.S3|5","Pivot.M.Fibonacci.S2|5","Pivot.M.Fibonacci.S1|5","Pivot.M.Fibonacci.Middle|5","Pivot.M.Fibonacci.R1|5","Pivot.M.Fibonacci.R2|5","Pivot.M.Fibonacci.R3|5","Pivot.M.Camarilla.S3|5","Pivot.M.Camarilla.S2|5","Pivot.M.Camarilla.S1|5","Pivot.M.Camarilla.Middle|5","Pivot.M.Camarilla.R1|5","Pivot.M.Camarilla.R2|5","Pivot.M.Camarilla.R3|5","Pivot.M.Woodie.S3|5","Pivot.M.Woodie.S2|5","Pivot.M.Woodie.S1|5","Pivot.M.Woodie.Middle|5","Pivot.M.Woodie.R1|5","Pivot.M.Woodie.R2|5","Pivot.M.Woodie.R3|5","Pivot.M.Demark.S1|5","Pivot.M.Demark.Middle|5","Pivot.M.Demark.R1|5","Recommend.Other|15","Recommend.All|15","Recommend.MA|15","RSI|15","RSI[1]|15","Stoch.K|15","Stoch.D|15","Stoch.K[1]|15","Stoch.D[1]|15","CCI20|15","CCI20[1]|15","ADX|15","ADX+DI|15","ADX-DI|15","ADX+DI[1]|15","ADX-DI[1]|15","AO|15","AO[1]|15","Mom|15","Mom[1]|15","MACD.macd|15","MACD.signal|15","Rec.Stoch.RSI|15","Stoch.RSI.K|15","Rec.WR|15","W.R|15","Rec.BBPower|15","BBPower|15","Rec.UO|15","UO|15","EMA5|15","close|15","SMA5|15","EMA10|15","SMA10|15","EMA20|15","SMA20|15","EMA30|15","SMA30|15","EMA50|15","SMA50|15","EMA100|15","SMA100|15","EMA200|15","SMA200|15","Rec.Ichimoku|15","Ichimoku.BLine|15","Rec.VWMA|15","VWMA|15","Rec.HullMA9|15","HullMA9|15","Pivot.M.Classic.S3|15","Pivot.M.Classic.S2|15","Pivot.M.Classic.S1|15","Pivot.M.Classic.Middle|15","Pivot.M.Classic.R1|15","Pivot.M.Classic.R2|15","Pivot.M.Classic.R3|15","Pivot.M.Fibonacci.S3|15","Pivot.M.Fibonacci.S2|15","Pivot.M.Fibonacci.S1|15","Pivot.M.Fibonacci.Middle|15","Pivot.M.Fibonacci.R1|15","Pivot.M.Fibonacci.R2|15","Pivot.M.Fibonacci.R3|15","Pivot.M.Camarilla.S3|15","Pivot.M.Camarilla.S2|15","Pivot.M.Camarilla.S1|15","Pivot.M.Camarilla.Middle|15","Pivot.M.Camarilla.R1|15","Pivot.M.Camarilla.R2|15","Pivot.M.Camarilla.R3|15","Pivot.M.Woodie.S3|15","Pivot.M.Woodie.S2|15","Pivot.M.Woodie.S1|15","Pivot.M.Woodie.Middle|15","Pivot.M.Woodie.R1|15","Pivot.M.Woodie.R2|15","Pivot.M.Woodie.R3|15","Pivot.M.Demark.S1|15","Pivot.M.Demark.Middle|15","Pivot.M.Demark.R1|15","Recommend.Other|60","Recommend.All|60","Recommend.MA|60","RSI|60","RSI[1]|60","Stoch.K|60","Stoch.D|60","Stoch.K[1]|60","Stoch.D[1]|60","CCI20|60","CCI20[1]|60","ADX|60","ADX+DI|60","ADX-DI|60","ADX+DI[1]|60","ADX-DI[1]|60","AO|60","AO[1]|60","Mom|60","Mom[1]|60","MACD.macd|60","MACD.signal|60","Rec.Stoch.RSI|60","Stoch.RSI.K|60","Rec.WR|60","W.R|60","Rec.BBPower|60","BBPower|60","Rec.UO|60","UO|60","EMA5|60","close|60","SMA5|60","EMA10|60","SMA10|60","EMA20|60","SMA20|60","EMA30|60","SMA30|60","EMA50|60","SMA50|60","EMA100|60","SMA100|60","EMA200|60","SMA200|60","Rec.Ichimoku|60","Ichimoku.BLine|60","Rec.VWMA|60","VWMA|60","Rec.HullMA9|60","HullMA9|60","Pivot.M.Classic.S3|60","Pivot.M.Classic.S2|60","Pivot.M.Classic.S1|60","Pivot.M.Classic.Middle|60","Pivot.M.Classic.R1|60","Pivot.M.Classic.R2|60","Pivot.M.Classic.R3|60","Pivot.M.Fibonacci.S3|60","Pivot.M.Fibonacci.S2|60","Pivot.M.Fibonacci.S1|60","Pivot.M.Fibonacci.Middle|60","Pivot.M.Fibonacci.R1|60","Pivot.M.Fibonacci.R2|60","Pivot.M.Fibonacci.R3|60","Pivot.M.Camarilla.S3|60","Pivot.M.Camarilla.S2|60","Pivot.M.Camarilla.S1|60","Pivot.M.Camarilla.Middle|60","Pivot.M.Camarilla.R1|60","Pivot.M.Camarilla.R2|60","Pivot.M.Camarilla.R3|60","Pivot.M.Woodie.S3|60","Pivot.M.Woodie.S2|60","Pivot.M.Woodie.S1|60","Pivot.M.Woodie.Middle|60","Pivot.M.Woodie.R1|60","Pivot.M.Woodie.R2|60","Pivot.M.Woodie.R3|60","Pivot.M.Demark.S1|60","Pivot.M.Demark.Middle|60","Pivot.M.Demark.R1|60","Recommend.Other|240","Recommend.All|240","Recommend.MA|240","RSI|240","RSI[1]|240","Stoch.K|240","Stoch.D|240","Stoch.K[1]|240","Stoch.D[1]|240","CCI20|240","CCI20[1]|240","ADX|240","ADX+DI|240","ADX-DI|240","ADX+DI[1]|240","ADX-DI[1]|240","AO|240","AO[1]|240","Mom|240","Mom[1]|240","MACD.macd|240","MACD.signal|240","Rec.Stoch.RSI|240","Stoch.RSI.K|240","Rec.WR|240","W.R|240","Rec.BBPower|240","BBPower|240","Rec.UO|240","UO|240","EMA5|240","close|240","SMA5|240","EMA10|240","SMA10|240","EMA20|240","SMA20|240","EMA30|240","SMA30|240","EMA50|240","SMA50|240","EMA100|240","SMA100|240","EMA200|240","SMA200|240","Rec.Ichimoku|240","Ichimoku.BLine|240","Rec.VWMA|240","VWMA|240","Rec.HullMA9|240","HullMA9|240","Pivot.M.Classic.S3|240","Pivot.M.Classic.S2|240","Pivot.M.Classic.S1|240","Pivot.M.Classic.Middle|240","Pivot.M.Classic.R1|240","Pivot.M.Classic.R2|240","Pivot.M.Classic.R3|240","Pivot.M.Fibonacci.S3|240","Pivot.M.Fibonacci.S2|240","Pivot.M.Fibonacci.S1|240","Pivot.M.Fibonacci.Middle|240","Pivot.M.Fibonacci.R1|240","Pivot.M.Fibonacci.R2|240","Pivot.M.Fibonacci.R3|240","Pivot.M.Camarilla.S3|240","Pivot.M.Camarilla.S2|240","Pivot.M.Camarilla.S1|240","Pivot.M.Camarilla.Middle|240","Pivot.M.Camarilla.R1|240","Pivot.M.Camarilla.R2|240","Pivot.M.Camarilla.R3|240","Pivot.M.Woodie.S3|240","Pivot.M.Woodie.S2|240","Pivot.M.Woodie.S1|240","Pivot.M.Woodie.Middle|240","Pivot.M.Woodie.R1|240","Pivot.M.Woodie.R2|240","Pivot.M.Woodie.R3|240","Pivot.M.Demark.S1|240","Pivot.M.Demark.Middle|240","Pivot.M.Demark.R1|240","Recommend.Other","Recommend.All","Recommend.MA","RSI","RSI[1]","Stoch.K","Stoch.D","Stoch.K[1]","Stoch.D[1]","CCI20","CCI20[1]","ADX","ADX+DI","ADX-DI","ADX+DI[1]","ADX-DI[1]","AO","AO[1]","Mom","Mom[1]","MACD.macd","MACD.signal","Rec.Stoch.RSI","Stoch.RSI.K","Rec.WR","W.R","Rec.BBPower","BBPower","Rec.UO","UO","EMA5","close","SMA5","EMA10","SMA10","EMA20","SMA20","EMA30","SMA30","EMA50","SMA50","EMA100","SMA100","EMA200","SMA200","Rec.Ichimoku","Ichimoku.BLine","Rec.VWMA","VWMA","Rec.HullMA9","HullMA9","Pivot.M.Classic.S3","Pivot.M.Classic.S2","Pivot.M.Classic.S1","Pivot.M.Classic.Middle","Pivot.M.Classic.R1","Pivot.M.Classic.R2","Pivot.M.Classic.R3","Pivot.M.Fibonacci.S3","Pivot.M.Fibonacci.S2","Pivot.M.Fibonacci.S1","Pivot.M.Fibonacci.Middle","Pivot.M.Fibonacci.R1","Pivot.M.Fibonacci.R2","Pivot.M.Fibonacci.R3","Pivot.M.Camarilla.S3","Pivot.M.Camarilla.S2","Pivot.M.Camarilla.S1","Pivot.M.Camarilla.Middle","Pivot.M.Camarilla.R1","Pivot.M.Camarilla.R2","Pivot.M.Camarilla.R3","Pivot.M.Woodie.S3","Pivot.M.Woodie.S2","Pivot.M.Woodie.S1","Pivot.M.Woodie.Middle","Pivot.M.Woodie.R1","Pivot.M.Woodie.R2","Pivot.M.Woodie.R3","Pivot.M.Demark.S1","Pivot.M.Demark.Middle","Pivot.M.Demark.R1","Recommend.Other|1W","Recommend.All|1W","Recommend.MA|1W","RSI|1W","RSI[1]|1W","Stoch.K|1W","Stoch.D|1W","Stoch.K[1]|1W","Stoch.D[1]|1W","CCI20|1W","CCI20[1]|1W","ADX|1W","ADX+DI|1W","ADX-DI|1W","ADX+DI[1]|1W","ADX-DI[1]|1W","AO|1W","AO[1]|1W","Mom|1W","Mom[1]|1W","MACD.macd|1W","MACD.signal|1W","Rec.Stoch.RSI|1W","Stoch.RSI.K|1W","Rec.WR|1W","W.R|1W","Rec.BBPower|1W","BBPower|1W","Rec.UO|1W","UO|1W","EMA5|1W","close|1W","SMA5|1W","EMA10|1W","SMA10|1W","EMA20|1W","SMA20|1W","EMA30|1W","SMA30|1W","EMA50|1W","SMA50|1W","EMA100|1W","SMA100|1W","EMA200|1W","SMA200|1W","Rec.Ichimoku|1W","Ichimoku.BLine|1W","Rec.VWMA|1W","VWMA|1W","Rec.HullMA9|1W","HullMA9|1W","Pivot.M.Classic.S3|1W","Pivot.M.Classic.S2|1W","Pivot.M.Classic.S1|1W","Pivot.M.Classic.Middle|1W","Pivot.M.Classic.R1|1W","Pivot.M.Classic.R2|1W","Pivot.M.Classic.R3|1W","Pivot.M.Fibonacci.S3|1W","Pivot.M.Fibonacci.S2|1W","Pivot.M.Fibonacci.S1|1W","Pivot.M.Fibonacci.Middle|1W","Pivot.M.Fibonacci.R1|1W","Pivot.M.Fibonacci.R2|1W","Pivot.M.Fibonacci.R3|1W","Pivot.M.Camarilla.S3|1W","Pivot.M.Camarilla.S2|1W","Pivot.M.Camarilla.S1|1W","Pivot.M.Camarilla.Middle|1W","Pivot.M.Camarilla.R1|1W","Pivot.M.Camarilla.R2|1W","Pivot.M.Camarilla.R3|1W","Pivot.M.Woodie.S3|1W","Pivot.M.Woodie.S2|1W","Pivot.M.Woodie.S1|1W","Pivot.M.Woodie.Middle|1W","Pivot.M.Woodie.R1|1W","Pivot.M.Woodie.R2|1W","Pivot.M.Woodie.R3|1W","Pivot.M.Demark.S1|1W","Pivot.M.Demark.Middle|1W","Pivot.M.Demark.R1|1W","Recommend.Other|1M","Recommend.All|1M","Recommend.MA|1M","RSI|1M","RSI[1]|1M","Stoch.K|1M","Stoch.D|1M","Stoch.K[1]|1M","Stoch.D[1]|1M","CCI20|1M","CCI20[1]|1M","ADX|1M","ADX+DI|1M","ADX-DI|1M","ADX+DI[1]|1M","ADX-DI[1]|1M","AO|1M","AO[1]|1M","Mom|1M","Mom[1]|1M","MACD.macd|1M","MACD.signal|1M","Rec.Stoch.RSI|1M","Stoch.RSI.K|1M","Rec.WR|1M","W.R|1M","Rec.BBPower|1M","BBPower|1M","Rec.UO|1M","UO|1M","EMA5|1M","close|1M","SMA5|1M","EMA10|1M","SMA10|1M","EMA20|1M","SMA20|1M","EMA30|1M","SMA30|1M","EMA50|1M","SMA50|1M","EMA100|1M","SMA100|1M","EMA200|1M","SMA200|1M","Rec.Ichimoku|1M","Ichimoku.BLine|1M","Rec.VWMA|1M","VWMA|1M","Rec.HullMA9|1M","HullMA9|1M","Pivot.M.Classic.S3|1M","Pivot.M.Classic.S2|1M","Pivot.M.Classic.S1|1M","Pivot.M.Classic.Middle|1M","Pivot.M.Classic.R1|1M","Pivot.M.Classic.R2|1M","Pivot.M.Classic.R3|1M","Pivot.M.Fibonacci.S3|1M","Pivot.M.Fibonacci.S2|1M","Pivot.M.Fibonacci.S1|1M","Pivot.M.Fibonacci.Middle|1M","Pivot.M.Fibonacci.R1|1M","Pivot.M.Fibonacci.R2|1M","Pivot.M.Fibonacci.R3|1M","Pivot.M.Camarilla.S3|1M","Pivot.M.Camarilla.S2|1M","Pivot.M.Camarilla.S1|1M","Pivot.M.Camarilla.Middle|1M","Pivot.M.Camarilla.R1|1M","Pivot.M.Camarilla.R2|1M","Pivot.M.Camarilla.R3|1M","Pivot.M.Woodie.S3|1M","Pivot.M.Woodie.S2|1M","Pivot.M.Woodie.S1|1M","Pivot.M.Woodie.Middle|1M","Pivot.M.Woodie.R1|1M","Pivot.M.Woodie.R2|1M","Pivot.M.Woodie.R3|1M","Pivot.M.Demark.S1|1M","Pivot.M.Demark.Middle|1M","Pivot.M.Demark.R1|1M"]}'
    Data_all=requests.post(URL,HEADER).json()['data']
    columns=["open_1","open_5","open_15","open_60","open_240","open","open_1W","open_1M","high_1","high_5","high_15","high_60","high_240","high","high_1W","high_1M","low_1","low_5","low_15","low_60","low_240","low","low_1W","low_1M","close_1","close_5","close_15","close_60","close_240","close","close_1W","close_1M","volume_1","volume_5","volume_15","volume_60","volume_240","volume","volume_1W","volume_1M","Recommend_Other_1","Recommend_All_1","Recommend_MA_1","RSI_1","RSI_1__1","Stoch_K_1","Stoch_D_1","Stoch_K_1__1","Stoch_D_1__1","CCI20_1","CCI20_1__1","ADX_1","ADX+DI_1","ADX-DI_1","ADX+DI_1__1","ADX-DI_1__1","AO_1","AO_1__1","Mom_1","Mom_1__1","MACD_macd_1","MACD_signal_1","Rec_Stoch_RSI_1","Stoch_RSI_K_1","Rec_WR_1","W_R_1","Rec_BBPower_1","BBPower_1","Rec_UO_1","UO_1","EMA5_1","close_1","SMA5_1","EMA10_1","SMA10_1","EMA20_1","SMA20_1","EMA30_1","SMA30_1","EMA50_1","SMA50_1","EMA100_1","SMA100_1","EMA200_1","SMA200_1","Rec_Ichimoku_1","Ichimoku_BLine_1","Rec_VWMA_1","VWMA_1","Rec_HullMA9_1","HullMA9_1","Pivot_M_Classic_S3_1","Pivot_M_Classic_S2_1","Pivot_M_Classic_S1_1","Pivot_M_Classic_Middle_1","Pivot_M_Classic_R1_1","Pivot_M_Classic_R2_1","Pivot_M_Classic_R3_1","Pivot_M_Fibonacci_S3_1","Pivot_M_Fibonacci_S2_1","Pivot_M_Fibonacci_S1_1","Pivot_M_Fibonacci_Middle_1","Pivot_M_Fibonacci_R1_1","Pivot_M_Fibonacci_R2_1","Pivot_M_Fibonacci_R3_1","Pivot_M_Camarilla_S3_1","Pivot_M_Camarilla_S2_1","Pivot_M_Camarilla_S1_1","Pivot_M_Camarilla_Middle_1","Pivot_M_Camarilla_R1_1","Pivot_M_Camarilla_R2_1","Pivot_M_Camarilla_R3_1","Pivot_M_Woodie_S3_1","Pivot_M_Woodie_S2_1","Pivot_M_Woodie_S1_1","Pivot_M_Woodie_Middle_1","Pivot_M_Woodie_R1_1","Pivot_M_Woodie_R2_1","Pivot_M_Woodie_R3_1","Pivot_M_Demark_S1_1","Pivot_M_Demark_Middle_1","Pivot_M_Demark_R1_1","Recommend_Other_5","Recommend_All_5","Recommend_MA_5","RSI_5","RSI_1__5","Stoch_K_5","Stoch_D_5","Stoch_K_1__5","Stoch_D_1__5","CCI20_5","CCI20_1__5","ADX_5","ADX+DI_5","ADX-DI_5","ADX+DI_1__5","ADX-DI_1__5","AO_5","AO_1__5","Mom_5","Mom_1__5","MACD_macd_5","MACD_signal_5","Rec_Stoch_RSI_5","Stoch_RSI_K_5","Rec_WR_5","W_R_5","Rec_BBPower_5","BBPower_5","Rec_UO_5","UO_5","EMA5_5","close_5","SMA5_5","EMA10_5","SMA10_5","EMA20_5","SMA20_5","EMA30_5","SMA30_5","EMA50_5","SMA50_5","EMA100_5","SMA100_5","EMA200_5","SMA200_5","Rec_Ichimoku_5","Ichimoku_BLine_5","Rec_VWMA_5","VWMA_5","Rec_HullMA9_5","HullMA9_5","Pivot_M_Classic_S3_5","Pivot_M_Classic_S2_5","Pivot_M_Classic_S1_5","Pivot_M_Classic_Middle_5","Pivot_M_Classic_R1_5","Pivot_M_Classic_R2_5","Pivot_M_Classic_R3_5","Pivot_M_Fibonacci_S3_5","Pivot_M_Fibonacci_S2_5","Pivot_M_Fibonacci_S1_5","Pivot_M_Fibonacci_Middle_5","Pivot_M_Fibonacci_R1_5","Pivot_M_Fibonacci_R2_5","Pivot_M_Fibonacci_R3_5","Pivot_M_Camarilla_S3_5","Pivot_M_Camarilla_S2_5","Pivot_M_Camarilla_S1_5","Pivot_M_Camarilla_Middle_5","Pivot_M_Camarilla_R1_5","Pivot_M_Camarilla_R2_5","Pivot_M_Camarilla_R3_5","Pivot_M_Woodie_S3_5","Pivot_M_Woodie_S2_5","Pivot_M_Woodie_S1_5","Pivot_M_Woodie_Middle_5","Pivot_M_Woodie_R1_5","Pivot_M_Woodie_R2_5","Pivot_M_Woodie_R3_5","Pivot_M_Demark_S1_5","Pivot_M_Demark_Middle_5","Pivot_M_Demark_R1_5","Recommend_Other_15","Recommend_All_15","Recommend_MA_15","RSI_15","RSI_1__15","Stoch_K_15","Stoch_D_15","Stoch_K_1__15","Stoch_D_1__15","CCI20_15","CCI20_1__15","ADX_15","ADX+DI_15","ADX-DI_15","ADX+DI_1__15","ADX-DI_1__15","AO_15","AO_1__15","Mom_15","Mom_1__15","MACD_macd_15","MACD_signal_15","Rec_Stoch_RSI_15","Stoch_RSI_K_15","Rec_WR_15","W_R_15","Rec_BBPower_15","BBPower_15","Rec_UO_15","UO_15","EMA5_15","close_15","SMA5_15","EMA10_15","SMA10_15","EMA20_15","SMA20_15","EMA30_15","SMA30_15","EMA50_15","SMA50_15","EMA100_15","SMA100_15","EMA200_15","SMA200_15","Rec_Ichimoku_15","Ichimoku_BLine_15","Rec_VWMA_15","VWMA_15","Rec_HullMA9_15","HullMA9_15","Pivot_M_Classic_S3_15","Pivot_M_Classic_S2_15","Pivot_M_Classic_S1_15","Pivot_M_Classic_Middle_15","Pivot_M_Classic_R1_15","Pivot_M_Classic_R2_15","Pivot_M_Classic_R3_15","Pivot_M_Fibonacci_S3_15","Pivot_M_Fibonacci_S2_15","Pivot_M_Fibonacci_S1_15","Pivot_M_Fibonacci_Middle_15","Pivot_M_Fibonacci_R1_15","Pivot_M_Fibonacci_R2_15","Pivot_M_Fibonacci_R3_15","Pivot_M_Camarilla_S3_15","Pivot_M_Camarilla_S2_15","Pivot_M_Camarilla_S1_15","Pivot_M_Camarilla_Middle_15","Pivot_M_Camarilla_R1_15","Pivot_M_Camarilla_R2_15","Pivot_M_Camarilla_R3_15","Pivot_M_Woodie_S3_15","Pivot_M_Woodie_S2_15","Pivot_M_Woodie_S1_15","Pivot_M_Woodie_Middle_15","Pivot_M_Woodie_R1_15","Pivot_M_Woodie_R2_15","Pivot_M_Woodie_R3_15","Pivot_M_Demark_S1_15","Pivot_M_Demark_Middle_15","Pivot_M_Demark_R1_15","Recommend_Other_60","Recommend_All_60","Recommend_MA_60","RSI_60","RSI_1__60","Stoch_K_60","Stoch_D_60","Stoch_K_1__60","Stoch_D_1__60","CCI20_60","CCI20_1__60","ADX_60","ADX+DI_60","ADX-DI_60","ADX+DI_1__60","ADX-DI_1__60","AO_60","AO_1__60","Mom_60","Mom_1__60","MACD_macd_60","MACD_signal_60","Rec_Stoch_RSI_60","Stoch_RSI_K_60","Rec_WR_60","W_R_60","Rec_BBPower_60","BBPower_60","Rec_UO_60","UO_60","EMA5_60","close_60","SMA5_60","EMA10_60","SMA10_60","EMA20_60","SMA20_60","EMA30_60","SMA30_60","EMA50_60","SMA50_60","EMA100_60","SMA100_60","EMA200_60","SMA200_60","Rec_Ichimoku_60","Ichimoku_BLine_60","Rec_VWMA_60","VWMA_60","Rec_HullMA9_60","HullMA9_60","Pivot_M_Classic_S3_60","Pivot_M_Classic_S2_60","Pivot_M_Classic_S1_60","Pivot_M_Classic_Middle_60","Pivot_M_Classic_R1_60","Pivot_M_Classic_R2_60","Pivot_M_Classic_R3_60","Pivot_M_Fibonacci_S3_60","Pivot_M_Fibonacci_S2_60","Pivot_M_Fibonacci_S1_60","Pivot_M_Fibonacci_Middle_60","Pivot_M_Fibonacci_R1_60","Pivot_M_Fibonacci_R2_60","Pivot_M_Fibonacci_R3_60","Pivot_M_Camarilla_S3_60","Pivot_M_Camarilla_S2_60","Pivot_M_Camarilla_S1_60","Pivot_M_Camarilla_Middle_60","Pivot_M_Camarilla_R1_60","Pivot_M_Camarilla_R2_60","Pivot_M_Camarilla_R3_60","Pivot_M_Woodie_S3_60","Pivot_M_Woodie_S2_60","Pivot_M_Woodie_S1_60","Pivot_M_Woodie_Middle_60","Pivot_M_Woodie_R1_60","Pivot_M_Woodie_R2_60","Pivot_M_Woodie_R3_60","Pivot_M_Demark_S1_60","Pivot_M_Demark_Middle_60","Pivot_M_Demark_R1_60","Recommend_Other_240","Recommend_All_240","Recommend_MA_240","RSI_240","RSI_1__240","Stoch_K_240","Stoch_D_240","Stoch_K_1__240","Stoch_D_1__240","CCI20_240","CCI20_1__240","ADX_240","ADX+DI_240","ADX-DI_240","ADX+DI_1__240","ADX-DI_1__240","AO_240","AO_1__240","Mom_240","Mom_1__240","MACD_macd_240","MACD_signal_240","Rec_Stoch_RSI_240","Stoch_RSI_K_240","Rec_WR_240","W_R_240","Rec_BBPower_240","BBPower_240","Rec_UO_240","UO_240","EMA5_240","close_240","SMA5_240","EMA10_240","SMA10_240","EMA20_240","SMA20_240","EMA30_240","SMA30_240","EMA50_240","SMA50_240","EMA100_240","SMA100_240","EMA200_240","SMA200_240","Rec_Ichimoku_240","Ichimoku_BLine_240","Rec_VWMA_240","VWMA_240","Rec_HullMA9_240","HullMA9_240","Pivot_M_Classic_S3_240","Pivot_M_Classic_S2_240","Pivot_M_Classic_S1_240","Pivot_M_Classic_Middle_240","Pivot_M_Classic_R1_240","Pivot_M_Classic_R2_240","Pivot_M_Classic_R3_240","Pivot_M_Fibonacci_S3_240","Pivot_M_Fibonacci_S2_240","Pivot_M_Fibonacci_S1_240","Pivot_M_Fibonacci_Middle_240","Pivot_M_Fibonacci_R1_240","Pivot_M_Fibonacci_R2_240","Pivot_M_Fibonacci_R3_240","Pivot_M_Camarilla_S3_240","Pivot_M_Camarilla_S2_240","Pivot_M_Camarilla_S1_240","Pivot_M_Camarilla_Middle_240","Pivot_M_Camarilla_R1_240","Pivot_M_Camarilla_R2_240","Pivot_M_Camarilla_R3_240","Pivot_M_Woodie_S3_240","Pivot_M_Woodie_S2_240","Pivot_M_Woodie_S1_240","Pivot_M_Woodie_Middle_240","Pivot_M_Woodie_R1_240","Pivot_M_Woodie_R2_240","Pivot_M_Woodie_R3_240","Pivot_M_Demark_S1_240","Pivot_M_Demark_Middle_240","Pivot_M_Demark_R1_240","Recommend_Other","Recommend_All","Recommend_MA","RSI","RSI_1_","Stoch_K","Stoch_D","Stoch_K_1_","Stoch_D_1_","CCI20","CCI20_1_","ADX","ADX+DI","ADX-DI","ADX+DI_1_","ADX-DI_1_","AO","AO_1_","Mom","Mom_1_","MACD_macd","MACD_signal","Rec_Stoch_RSI","Stoch_RSI_K","Rec_WR","W_R","Rec_BBPower","BBPower","Rec_UO","UO","EMA5","close","SMA5","EMA10","SMA10","EMA20","SMA20","EMA30","SMA30","EMA50","SMA50","EMA100","SMA100","EMA200","SMA200","Rec_Ichimoku","Ichimoku_BLine","Rec_VWMA","VWMA","Rec_HullMA9","HullMA9","Pivot_M_Classic_S3","Pivot_M_Classic_S2","Pivot_M_Classic_S1","Pivot_M_Classic_Middle","Pivot_M_Classic_R1","Pivot_M_Classic_R2","Pivot_M_Classic_R3","Pivot_M_Fibonacci_S3","Pivot_M_Fibonacci_S2","Pivot_M_Fibonacci_S1","Pivot_M_Fibonacci_Middle","Pivot_M_Fibonacci_R1","Pivot_M_Fibonacci_R2","Pivot_M_Fibonacci_R3","Pivot_M_Camarilla_S3","Pivot_M_Camarilla_S2","Pivot_M_Camarilla_S1","Pivot_M_Camarilla_Middle","Pivot_M_Camarilla_R1","Pivot_M_Camarilla_R2","Pivot_M_Camarilla_R3","Pivot_M_Woodie_S3","Pivot_M_Woodie_S2","Pivot_M_Woodie_S1","Pivot_M_Woodie_Middle","Pivot_M_Woodie_R1","Pivot_M_Woodie_R2","Pivot_M_Woodie_R3","Pivot_M_Demark_S1","Pivot_M_Demark_Middle","Pivot_M_Demark_R1","Recommend_Other_1W","Recommend_All_1W","Recommend_MA_1W","RSI_1W","RSI_1__1W","Stoch_K_1W","Stoch_D_1W","Stoch_K_1__1W","Stoch_D_1__1W","CCI20_1W","CCI20_1__1W","ADX_1W","ADX+DI_1W","ADX-DI_1W","ADX+DI_1__1W","ADX-DI_1__1W","AO_1W","AO_1__1W","Mom_1W","Mom_1__1W","MACD_macd_1W","MACD_signal_1W","Rec_Stoch_RSI_1W","Stoch_RSI_K_1W","Rec_WR_1W","W_R_1W","Rec_BBPower_1W","BBPower_1W","Rec_UO_1W","UO_1W","EMA5_1W","close_1W","SMA5_1W","EMA10_1W","SMA10_1W","EMA20_1W","SMA20_1W","EMA30_1W","SMA30_1W","EMA50_1W","SMA50_1W","EMA100_1W","SMA100_1W","EMA200_1W","SMA200_1W","Rec_Ichimoku_1W","Ichimoku_BLine_1W","Rec_VWMA_1W","VWMA_1W","Rec_HullMA9_1W","HullMA9_1W","Pivot_M_Classic_S3_1W","Pivot_M_Classic_S2_1W","Pivot_M_Classic_S1_1W","Pivot_M_Classic_Middle_1W","Pivot_M_Classic_R1_1W","Pivot_M_Classic_R2_1W","Pivot_M_Classic_R3_1W","Pivot_M_Fibonacci_S3_1W","Pivot_M_Fibonacci_S2_1W","Pivot_M_Fibonacci_S1_1W","Pivot_M_Fibonacci_Middle_1W","Pivot_M_Fibonacci_R1_1W","Pivot_M_Fibonacci_R2_1W","Pivot_M_Fibonacci_R3_1W","Pivot_M_Camarilla_S3_1W","Pivot_M_Camarilla_S2_1W","Pivot_M_Camarilla_S1_1W","Pivot_M_Camarilla_Middle_1W","Pivot_M_Camarilla_R1_1W","Pivot_M_Camarilla_R2_1W","Pivot_M_Camarilla_R3_1W","Pivot_M_Woodie_S3_1W","Pivot_M_Woodie_S2_1W","Pivot_M_Woodie_S1_1W","Pivot_M_Woodie_Middle_1W","Pivot_M_Woodie_R1_1W","Pivot_M_Woodie_R2_1W","Pivot_M_Woodie_R3_1W","Pivot_M_Demark_S1_1W","Pivot_M_Demark_Middle_1W","Pivot_M_Demark_R1_1W","Recommend_Other_1M","Recommend_All_1M","Recommend_MA_1M","RSI_1M","RSI_1__1M","Stoch_K_1M","Stoch_D_1M","Stoch_K_1__1M","Stoch_D_1__1M","CCI20_1M","CCI20_1__1M","ADX_1M","ADX+DI_1M","ADX-DI_1M","ADX+DI_1__1M","ADX-DI_1__1M","AO_1M","AO_1__1M","Mom_1M","Mom_1__1M","MACD_macd_1M","MACD_signal_1M","Rec_Stoch_RSI_1M","Stoch_RSI_K_1M","Rec_WR_1M","W_R_1M","Rec_BBPower_1M","BBPower_1M","Rec_UO_1M","UO_1M","EMA5_1M","close_1M","SMA5_1M","EMA10_1M","SMA10_1M","EMA20_1M","SMA20_1M","EMA30_1M","SMA30_1M","EMA50_1M","SMA50_1M","EMA100_1M","SMA100_1M","EMA200_1M","SMA200_1M","Rec_Ichimoku_1M","Ichimoku_BLine_1M","Rec_VWMA_1M","VWMA_1M","Rec_HullMA9_1M","HullMA9_1M","Pivot_M_Classic_S3_1M","Pivot_M_Classic_S2_1M","Pivot_M_Classic_S1_1M","Pivot_M_Classic_Middle_1M","Pivot_M_Classic_R1_1M","Pivot_M_Classic_R2_1M","Pivot_M_Classic_R3_1M","Pivot_M_Fibonacci_S3_1M","Pivot_M_Fibonacci_S2_1M","Pivot_M_Fibonacci_S1_1M","Pivot_M_Fibonacci_Middle_1M","Pivot_M_Fibonacci_R1_1M","Pivot_M_Fibonacci_R2_1M","Pivot_M_Fibonacci_R3_1M","Pivot_M_Camarilla_S3_1M","Pivot_M_Camarilla_S2_1M","Pivot_M_Camarilla_S1_1M","Pivot_M_Camarilla_Middle_1M","Pivot_M_Camarilla_R1_1M","Pivot_M_Camarilla_R2_1M","Pivot_M_Camarilla_R3_1M","Pivot_M_Woodie_S3_1M","Pivot_M_Woodie_S2_1M","Pivot_M_Woodie_S1_1M","Pivot_M_Woodie_Middle_1M","Pivot_M_Woodie_R1_1M","Pivot_M_Woodie_R2_1M","Pivot_M_Woodie_R3_1M","Pivot_M_Demark_S1_1M","Pivot_M_Demark_Middle_1M","Pivot_M_Demark_R1_1M"]
    #pprint(len(columns))
    for data in Data_all:
        symbol=data['s'].replace('NSE:','').replace("'","")
        print(symbol)
        post={
        "date":datetime.datetime.now(),
        "symbol":symbol,
        "open_1" : data["d"][0],
        "open_5" : data["d"][1],
        "open_15" : data["d"][2],
        "open_60" : data["d"][3],
        "open_240" : data["d"][4],
        "open" : data["d"][5],
        "open_1W" : data["d"][6],
        "open_1M" : data["d"][7],
        "high_1" : data["d"][8],
        "high_5" : data["d"][9],
        "high_15" : data["d"][10],
        "high_60" : data["d"][11],
        "high_240" : data["d"][12],
        "high" : data["d"][13],
        "high_1W" : data["d"][14],
        "high_1M" : data["d"][15],
        "low_1" : data["d"][16],
        "low_5" : data["d"][17],
        "low_15" : data["d"][18],
        "low_60" : data["d"][19],
        "low_240" : data["d"][20],
        "low" : data["d"][21],
        "low_1W" : data["d"][22],
        "low_1M" : data["d"][23],
        "close_1" : data["d"][24],
        "close_5" : data["d"][25],
        "close_15" : data["d"][26],
        "close_60" : data["d"][27],
        "close_240" : data["d"][28],
        "close" : data["d"][29],
        "close_1W" : data["d"][30],
        "close_1M" : data["d"][31],
        "volume_1" : data["d"][32],
        "volume_5" : data["d"][33],
        "volume_15" : data["d"][34],
        "volume_60" : data["d"][35],
        "volume_240" : data["d"][36],
        "volume" : data["d"][37],
        "volume_1W" : data["d"][38],
        "volume_1M" : data["d"][39],
        "Recommend_Other_1" : data["d"][40],
        "Recommend_All_1" : data["d"][41],
        "Recommend_MA_1" : data["d"][42],
        "RSI_1" : data["d"][43],
        "RSI_1__1" : data["d"][44],
        "Stoch_K_1" : data["d"][45],
        "Stoch_D_1" : data["d"][46],
        "Stoch_K_1__1" : data["d"][47],
        "Stoch_D_1__1" : data["d"][48],
        "CCI20_1" : data["d"][49],
        "CCI20_1__1" : data["d"][50],
        "ADX_1" : data["d"][51],
        "ADX+DI_1" : data["d"][52],
        "ADX-DI_1" : data["d"][53],
        "ADX+DI_1__1" : data["d"][54],
        "ADX-DI_1__1" : data["d"][55],
        "AO_1" : data["d"][56],
        "AO_1__1" : data["d"][57],
        "Mom_1" : data["d"][58],
        "Mom_1__1" : data["d"][59],
        "MACD_macd_1" : data["d"][60],
        "MACD_signal_1" : data["d"][61],
        "Rec_Stoch_RSI_1" : data["d"][62],
        "Stoch_RSI_K_1" : data["d"][63],
        "Rec_WR_1" : data["d"][64],
        "W_R_1" : data["d"][65],
        "Rec_BBPower_1" : data["d"][66],
        "BBPower_1" : data["d"][67],
        "Rec_UO_1" : data["d"][68],
        "UO_1" : data["d"][69],
        "EMA5_1" : data["d"][70],
        "close_1" : data["d"][71],
        "SMA5_1" : data["d"][72],
        "EMA10_1" : data["d"][73],
        "SMA10_1" : data["d"][74],
        "EMA20_1" : data["d"][75],
        "SMA20_1" : data["d"][76],
        "EMA30_1" : data["d"][77],
        "SMA30_1" : data["d"][78],
        "EMA50_1" : data["d"][79],
        "SMA50_1" : data["d"][80],
        "EMA100_1" : data["d"][81],
        "SMA100_1" : data["d"][82],
        "EMA200_1" : data["d"][83],
        "SMA200_1" : data["d"][84],
        "Rec_Ichimoku_1" : data["d"][85],
        "Ichimoku_BLine_1" : data["d"][86],
        "Rec_VWMA_1" : data["d"][87],
        "VWMA_1" : data["d"][88],
        "Rec_HullMA9_1" : data["d"][89],
        "HullMA9_1" : data["d"][90],
        "Pivot_M_Classic_S3_1" : data["d"][91],
        "Pivot_M_Classic_S2_1" : data["d"][92],
        "Pivot_M_Classic_S1_1" : data["d"][93],
        "Pivot_M_Classic_Middle_1" : data["d"][94],
        "Pivot_M_Classic_R1_1" : data["d"][95],
        "Pivot_M_Classic_R2_1" : data["d"][96],
        "Pivot_M_Classic_R3_1" : data["d"][97],
        "Pivot_M_Fibonacci_S3_1" : data["d"][98],
        "Pivot_M_Fibonacci_S2_1" : data["d"][99],
        "Pivot_M_Fibonacci_S1_1" : data["d"][100],
        "Pivot_M_Fibonacci_Middle_1" : data["d"][101],
        "Pivot_M_Fibonacci_R1_1" : data["d"][102],
        "Pivot_M_Fibonacci_R2_1" : data["d"][103],
        "Pivot_M_Fibonacci_R3_1" : data["d"][104],
        "Pivot_M_Camarilla_S3_1" : data["d"][105],
        "Pivot_M_Camarilla_S2_1" : data["d"][106],
        "Pivot_M_Camarilla_S1_1" : data["d"][107],
        "Pivot_M_Camarilla_Middle_1" : data["d"][108],
        "Pivot_M_Camarilla_R1_1" : data["d"][109],
        "Pivot_M_Camarilla_R2_1" : data["d"][110],
        "Pivot_M_Camarilla_R3_1" : data["d"][111],
        "Pivot_M_Woodie_S3_1" : data["d"][112],
        "Pivot_M_Woodie_S2_1" : data["d"][113],
        "Pivot_M_Woodie_S1_1" : data["d"][114],
        "Pivot_M_Woodie_Middle_1" : data["d"][115],
        "Pivot_M_Woodie_R1_1" : data["d"][116],
        "Pivot_M_Woodie_R2_1" : data["d"][117],
        "Pivot_M_Woodie_R3_1" : data["d"][118],
        "Pivot_M_Demark_S1_1" : data["d"][119],
        "Pivot_M_Demark_Middle_1" : data["d"][120],
        "Pivot_M_Demark_R1_1" : data["d"][121],
        "Recommend_Other_5" : data["d"][122],
        "Recommend_All_5" : data["d"][123],
        "Recommend_MA_5" : data["d"][124],
        "RSI_5" : data["d"][125],
        "RSI_1__5" : data["d"][126],
        "Stoch_K_5" : data["d"][127],
        "Stoch_D_5" : data["d"][128],
        "Stoch_K_1__5" : data["d"][129],
        "Stoch_D_1__5" : data["d"][130],
        "CCI20_5" : data["d"][131],
        "CCI20_1__5" : data["d"][132],
        "ADX_5" : data["d"][133],
        "ADX+DI_5" : data["d"][134],
        "ADX-DI_5" : data["d"][135],
        "ADX+DI_1__5" : data["d"][136],
        "ADX-DI_1__5" : data["d"][137],
        "AO_5" : data["d"][138],
        "AO_1__5" : data["d"][139],
        "Mom_5" : data["d"][140],
        "Mom_1__5" : data["d"][141],
        "MACD_macd_5" : data["d"][142],
        "MACD_signal_5" : data["d"][143],
        "Rec_Stoch_RSI_5" : data["d"][144],
        "Stoch_RSI_K_5" : data["d"][145],
        "Rec_WR_5" : data["d"][146],
        "W_R_5" : data["d"][147],
        "Rec_BBPower_5" : data["d"][148],
        "BBPower_5" : data["d"][149],
        "Rec_UO_5" : data["d"][150],
        "UO_5" : data["d"][151],
        "EMA5_5" : data["d"][152],
        "close_5" : data["d"][153],
        "SMA5_5" : data["d"][154],
        "EMA10_5" : data["d"][155],
        "SMA10_5" : data["d"][156],
        "EMA20_5" : data["d"][157],
        "SMA20_5" : data["d"][158],
        "EMA30_5" : data["d"][159],
        "SMA30_5" : data["d"][160],
        "EMA50_5" : data["d"][161],
        "SMA50_5" : data["d"][162],
        "EMA100_5" : data["d"][163],
        "SMA100_5" : data["d"][164],
        "EMA200_5" : data["d"][165],
        "SMA200_5" : data["d"][166],
        "Rec_Ichimoku_5" : data["d"][167],
        "Ichimoku_BLine_5" : data["d"][168],
        "Rec_VWMA_5" : data["d"][169],
        "VWMA_5" : data["d"][170],
        "Rec_HullMA9_5" : data["d"][171],
        "HullMA9_5" : data["d"][172],
        "Pivot_M_Classic_S3_5" : data["d"][173],
        "Pivot_M_Classic_S2_5" : data["d"][174],
        "Pivot_M_Classic_S1_5" : data["d"][175],
        "Pivot_M_Classic_Middle_5" : data["d"][176],
        "Pivot_M_Classic_R1_5" : data["d"][177],
        "Pivot_M_Classic_R2_5" : data["d"][178],
        "Pivot_M_Classic_R3_5" : data["d"][179],
        "Pivot_M_Fibonacci_S3_5" : data["d"][180],
        "Pivot_M_Fibonacci_S2_5" : data["d"][181],
        "Pivot_M_Fibonacci_S1_5" : data["d"][182],
        "Pivot_M_Fibonacci_Middle_5" : data["d"][183],
        "Pivot_M_Fibonacci_R1_5" : data["d"][184],
        "Pivot_M_Fibonacci_R2_5" : data["d"][185],
        "Pivot_M_Fibonacci_R3_5" : data["d"][186],
        "Pivot_M_Camarilla_S3_5" : data["d"][187],
        "Pivot_M_Camarilla_S2_5" : data["d"][188],
        "Pivot_M_Camarilla_S1_5" : data["d"][189],
        "Pivot_M_Camarilla_Middle_5" : data["d"][190],
        "Pivot_M_Camarilla_R1_5" : data["d"][191],
        "Pivot_M_Camarilla_R2_5" : data["d"][192],
        "Pivot_M_Camarilla_R3_5" : data["d"][193],
        "Pivot_M_Woodie_S3_5" : data["d"][194],
        "Pivot_M_Woodie_S2_5" : data["d"][195],
        "Pivot_M_Woodie_S1_5" : data["d"][196],
        "Pivot_M_Woodie_Middle_5" : data["d"][197],
        "Pivot_M_Woodie_R1_5" : data["d"][198],
        "Pivot_M_Woodie_R2_5" : data["d"][199],
        "Pivot_M_Woodie_R3_5" : data["d"][200],
        "Pivot_M_Demark_S1_5" : data["d"][201],
        "Pivot_M_Demark_Middle_5" : data["d"][202],
        "Pivot_M_Demark_R1_5" : data["d"][203],
        "Recommend_Other_15" : data["d"][204],
        "Recommend_All_15" : data["d"][205],
        "Recommend_MA_15" : data["d"][206],
        "RSI_15" : data["d"][207],
        "RSI_1__15" : data["d"][208],
        "Stoch_K_15" : data["d"][209],
        "Stoch_D_15" : data["d"][210],
        "Stoch_K_1__15" : data["d"][211],
        "Stoch_D_1__15" : data["d"][212],
        "CCI20_15" : data["d"][213],
        "CCI20_1__15" : data["d"][214],
        "ADX_15" : data["d"][215],
        "ADX+DI_15" : data["d"][216],
        "ADX-DI_15" : data["d"][217],
        "ADX+DI_1__15" : data["d"][218],
        "ADX-DI_1__15" : data["d"][219],
        "AO_15" : data["d"][220],
        "AO_1__15" : data["d"][221],
        "Mom_15" : data["d"][222],
        "Mom_1__15" : data["d"][223],
        "MACD_macd_15" : data["d"][224],
        "MACD_signal_15" : data["d"][225],
        "Rec_Stoch_RSI_15" : data["d"][226],
        "Stoch_RSI_K_15" : data["d"][227],
        "Rec_WR_15" : data["d"][228],
        "W_R_15" : data["d"][229],
        "Rec_BBPower_15" : data["d"][230],
        "BBPower_15" : data["d"][231],
        "Rec_UO_15" : data["d"][232],
        "UO_15" : data["d"][233],
        "EMA5_15" : data["d"][234],
        "close_15" : data["d"][235],
        "SMA5_15" : data["d"][236],
        "EMA10_15" : data["d"][237],
        "SMA10_15" : data["d"][238],
        "EMA20_15" : data["d"][239],
        "SMA20_15" : data["d"][240],
        "EMA30_15" : data["d"][241],
        "SMA30_15" : data["d"][242],
        "EMA50_15" : data["d"][243],
        "SMA50_15" : data["d"][244],
        "EMA100_15" : data["d"][245],
        "SMA100_15" : data["d"][246],
        "EMA200_15" : data["d"][247],
        "SMA200_15" : data["d"][248],
        "Rec_Ichimoku_15" : data["d"][249],
        "Ichimoku_BLine_15" : data["d"][250],
        "Rec_VWMA_15" : data["d"][251],
        "VWMA_15" : data["d"][252],
        "Rec_HullMA9_15" : data["d"][253],
        "HullMA9_15" : data["d"][254],
        "Pivot_M_Classic_S3_15" : data["d"][255],
        "Pivot_M_Classic_S2_15" : data["d"][256],
        "Pivot_M_Classic_S1_15" : data["d"][257],
        "Pivot_M_Classic_Middle_15" : data["d"][258],
        "Pivot_M_Classic_R1_15" : data["d"][259],
        "Pivot_M_Classic_R2_15" : data["d"][260],
        "Pivot_M_Classic_R3_15" : data["d"][261],
        "Pivot_M_Fibonacci_S3_15" : data["d"][262],
        "Pivot_M_Fibonacci_S2_15" : data["d"][263],
        "Pivot_M_Fibonacci_S1_15" : data["d"][264],
        "Pivot_M_Fibonacci_Middle_15" : data["d"][265],
        "Pivot_M_Fibonacci_R1_15" : data["d"][266],
        "Pivot_M_Fibonacci_R2_15" : data["d"][267],
        "Pivot_M_Fibonacci_R3_15" : data["d"][268],
        "Pivot_M_Camarilla_S3_15" : data["d"][269],
        "Pivot_M_Camarilla_S2_15" : data["d"][270],
        "Pivot_M_Camarilla_S1_15" : data["d"][271],
        "Pivot_M_Camarilla_Middle_15" : data["d"][272],
        "Pivot_M_Camarilla_R1_15" : data["d"][273],
        "Pivot_M_Camarilla_R2_15" : data["d"][274],
        "Pivot_M_Camarilla_R3_15" : data["d"][275],
        "Pivot_M_Woodie_S3_15" : data["d"][276],
        "Pivot_M_Woodie_S2_15" : data["d"][277],
        "Pivot_M_Woodie_S1_15" : data["d"][278],
        "Pivot_M_Woodie_Middle_15" : data["d"][279],
        "Pivot_M_Woodie_R1_15" : data["d"][280],
        "Pivot_M_Woodie_R2_15" : data["d"][281],
        "Pivot_M_Woodie_R3_15" : data["d"][282],
        "Pivot_M_Demark_S1_15" : data["d"][283],
        "Pivot_M_Demark_Middle_15" : data["d"][284],
        "Pivot_M_Demark_R1_15" : data["d"][285],
        "Recommend_Other_60" : data["d"][286],
        "Recommend_All_60" : data["d"][287],
        "Recommend_MA_60" : data["d"][288],
        "RSI_60" : data["d"][289],
        "RSI_1__60" : data["d"][290],
        "Stoch_K_60" : data["d"][291],
        "Stoch_D_60" : data["d"][292],
        "Stoch_K_1__60" : data["d"][293],
        "Stoch_D_1__60" : data["d"][294],
        "CCI20_60" : data["d"][295],
        "CCI20_1__60" : data["d"][296],
        "ADX_60" : data["d"][297],
        "ADX+DI_60" : data["d"][298],
        "ADX-DI_60" : data["d"][299],
        "ADX+DI_1__60" : data["d"][300],
        "ADX-DI_1__60" : data["d"][301],
        "AO_60" : data["d"][302],
        "AO_1__60" : data["d"][303],
        "Mom_60" : data["d"][304],
        "Mom_1__60" : data["d"][305],
        "MACD_macd_60" : data["d"][306],
        "MACD_signal_60" : data["d"][307],
        "Rec_Stoch_RSI_60" : data["d"][308],
        "Stoch_RSI_K_60" : data["d"][309],
        "Rec_WR_60" : data["d"][310],
        "W_R_60" : data["d"][311],
        "Rec_BBPower_60" : data["d"][312],
        "BBPower_60" : data["d"][313],
        "Rec_UO_60" : data["d"][314],
        "UO_60" : data["d"][315],
        "EMA5_60" : data["d"][316],
        "close_60" : data["d"][317],
        "SMA5_60" : data["d"][318],
        "EMA10_60" : data["d"][319],
        "SMA10_60" : data["d"][320],
        "EMA20_60" : data["d"][321],
        "SMA20_60" : data["d"][322],
        "EMA30_60" : data["d"][323],
        "SMA30_60" : data["d"][324],
        "EMA50_60" : data["d"][325],
        "SMA50_60" : data["d"][326],
        "EMA100_60" : data["d"][327],
        "SMA100_60" : data["d"][328],
        "EMA200_60" : data["d"][329],
        "SMA200_60" : data["d"][330],
        "Rec_Ichimoku_60" : data["d"][331],
        "Ichimoku_BLine_60" : data["d"][332],
        "Rec_VWMA_60" : data["d"][333],
        "VWMA_60" : data["d"][334],
        "Rec_HullMA9_60" : data["d"][335],
        "HullMA9_60" : data["d"][336],
        "Pivot_M_Classic_S3_60" : data["d"][337],
        "Pivot_M_Classic_S2_60" : data["d"][338],
        "Pivot_M_Classic_S1_60" : data["d"][339],
        "Pivot_M_Classic_Middle_60" : data["d"][340],
        "Pivot_M_Classic_R1_60" : data["d"][341],
        "Pivot_M_Classic_R2_60" : data["d"][342],
        "Pivot_M_Classic_R3_60" : data["d"][343],
        "Pivot_M_Fibonacci_S3_60" : data["d"][344],
        "Pivot_M_Fibonacci_S2_60" : data["d"][345],
        "Pivot_M_Fibonacci_S1_60" : data["d"][346],
        "Pivot_M_Fibonacci_Middle_60" : data["d"][347],
        "Pivot_M_Fibonacci_R1_60" : data["d"][348],
        "Pivot_M_Fibonacci_R2_60" : data["d"][349],
        "Pivot_M_Fibonacci_R3_60" : data["d"][350],
        "Pivot_M_Camarilla_S3_60" : data["d"][351],
        "Pivot_M_Camarilla_S2_60" : data["d"][352],
        "Pivot_M_Camarilla_S1_60" : data["d"][353],
        "Pivot_M_Camarilla_Middle_60" : data["d"][354],
        "Pivot_M_Camarilla_R1_60" : data["d"][355],
        "Pivot_M_Camarilla_R2_60" : data["d"][356],
        "Pivot_M_Camarilla_R3_60" : data["d"][357],
        "Pivot_M_Woodie_S3_60" : data["d"][358],
        "Pivot_M_Woodie_S2_60" : data["d"][359],
        "Pivot_M_Woodie_S1_60" : data["d"][360],
        "Pivot_M_Woodie_Middle_60" : data["d"][361],
        "Pivot_M_Woodie_R1_60" : data["d"][362],
        "Pivot_M_Woodie_R2_60" : data["d"][363],
        "Pivot_M_Woodie_R3_60" : data["d"][364],
        "Pivot_M_Demark_S1_60" : data["d"][365],
        "Pivot_M_Demark_Middle_60" : data["d"][366],
        "Pivot_M_Demark_R1_60" : data["d"][367],
        "Recommend_Other_240" : data["d"][368],
        "Recommend_All_240" : data["d"][369],
        "Recommend_MA_240" : data["d"][370],
        "RSI_240" : data["d"][371],
        "RSI_1__240" : data["d"][372],
        "Stoch_K_240" : data["d"][373],
        "Stoch_D_240" : data["d"][374],
        "Stoch_K_1__240" : data["d"][375],
        "Stoch_D_1__240" : data["d"][376],
        "CCI20_240" : data["d"][377],
        "CCI20_1__240" : data["d"][378],
        "ADX_240" : data["d"][379],
        "ADX+DI_240" : data["d"][380],
        "ADX-DI_240" : data["d"][381],
        "ADX+DI_1__240" : data["d"][382],
        "ADX-DI_1__240" : data["d"][383],
        "AO_240" : data["d"][384],
        "AO_1__240" : data["d"][385],
        "Mom_240" : data["d"][386],
        "Mom_1__240" : data["d"][387],
        "MACD_macd_240" : data["d"][388],
        "MACD_signal_240" : data["d"][389],
        "Rec_Stoch_RSI_240" : data["d"][390],
        "Stoch_RSI_K_240" : data["d"][391],
        "Rec_WR_240" : data["d"][392],
        "W_R_240" : data["d"][393],
        "Rec_BBPower_240" : data["d"][394],
        "BBPower_240" : data["d"][395],
        "Rec_UO_240" : data["d"][396],
        "UO_240" : data["d"][397],
        "EMA5_240" : data["d"][398],
        "close_240" : data["d"][399],
        "SMA5_240" : data["d"][400],
        "EMA10_240" : data["d"][401],
        "SMA10_240" : data["d"][402],
        "EMA20_240" : data["d"][403],
        "SMA20_240" : data["d"][404],
        "EMA30_240" : data["d"][405],
        "SMA30_240" : data["d"][406],
        "EMA50_240" : data["d"][407],
        "SMA50_240" : data["d"][408],
        "EMA100_240" : data["d"][409],
        "SMA100_240" : data["d"][410],
        "EMA200_240" : data["d"][411],
        "SMA200_240" : data["d"][412],
        "Rec_Ichimoku_240" : data["d"][413],
        "Ichimoku_BLine_240" : data["d"][414],
        "Rec_VWMA_240" : data["d"][415],
        "VWMA_240" : data["d"][416],
        "Rec_HullMA9_240" : data["d"][417],
        "HullMA9_240" : data["d"][418],
        "Pivot_M_Classic_S3_240" : data["d"][419],
        "Pivot_M_Classic_S2_240" : data["d"][420],
        "Pivot_M_Classic_S1_240" : data["d"][421],
        "Pivot_M_Classic_Middle_240" : data["d"][422],
        "Pivot_M_Classic_R1_240" : data["d"][423],
        "Pivot_M_Classic_R2_240" : data["d"][424],
        "Pivot_M_Classic_R3_240" : data["d"][425],
        "Pivot_M_Fibonacci_S3_240" : data["d"][426],
        "Pivot_M_Fibonacci_S2_240" : data["d"][427],
        "Pivot_M_Fibonacci_S1_240" : data["d"][428],
        "Pivot_M_Fibonacci_Middle_240" : data["d"][429],
        "Pivot_M_Fibonacci_R1_240" : data["d"][430],
        "Pivot_M_Fibonacci_R2_240" : data["d"][431],
        "Pivot_M_Fibonacci_R3_240" : data["d"][432],
        "Pivot_M_Camarilla_S3_240" : data["d"][433],
        "Pivot_M_Camarilla_S2_240" : data["d"][434],
        "Pivot_M_Camarilla_S1_240" : data["d"][435],
        "Pivot_M_Camarilla_Middle_240" : data["d"][436],
        "Pivot_M_Camarilla_R1_240" : data["d"][437],
        "Pivot_M_Camarilla_R2_240" : data["d"][438],
        "Pivot_M_Camarilla_R3_240" : data["d"][439],
        "Pivot_M_Woodie_S3_240" : data["d"][440],
        "Pivot_M_Woodie_S2_240" : data["d"][441],
        "Pivot_M_Woodie_S1_240" : data["d"][442],
        "Pivot_M_Woodie_Middle_240" : data["d"][443],
        "Pivot_M_Woodie_R1_240" : data["d"][444],
        "Pivot_M_Woodie_R2_240" : data["d"][445],
        "Pivot_M_Woodie_R3_240" : data["d"][446],
        "Pivot_M_Demark_S1_240" : data["d"][447],
        "Pivot_M_Demark_Middle_240" : data["d"][448],
        "Pivot_M_Demark_R1_240" : data["d"][449],
        "Recommend_Other" : data["d"][450],
        "Recommend_All" : data["d"][451],
        "Recommend_MA" : data["d"][452],
        "RSI" : data["d"][453],
        "RSI_1_" : data["d"][454],
        "Stoch_K" : data["d"][455],
        "Stoch_D" : data["d"][456],
        "Stoch_K_1_" : data["d"][457],
        "Stoch_D_1_" : data["d"][458],
        "CCI20" : data["d"][459],
        "CCI20_1_" : data["d"][460],
        "ADX" : data["d"][461],
        "ADX+DI" : data["d"][462],
        "ADX-DI" : data["d"][463],
        "ADX+DI_1_" : data["d"][464],
        "ADX-DI_1_" : data["d"][465],
        "AO" : data["d"][466],
        "AO_1_" : data["d"][467],
        "Mom" : data["d"][468],
        "Mom_1_" : data["d"][469],
        "MACD_macd" : data["d"][470],
        "MACD_signal" : data["d"][471],
        "Rec_Stoch_RSI" : data["d"][472],
        "Stoch_RSI_K" : data["d"][473],
        "Rec_WR" : data["d"][474],
        "W_R" : data["d"][475],
        "Rec_BBPower" : data["d"][476],
        "BBPower" : data["d"][477],
        "Rec_UO" : data["d"][478],
        "UO" : data["d"][479],
        "EMA5" : data["d"][480],
        "close" : data["d"][481],
        "SMA5" : data["d"][482],
        "EMA10" : data["d"][483],
        "SMA10" : data["d"][484],
        "EMA20" : data["d"][485],
        "SMA20" : data["d"][486],
        "EMA30" : data["d"][487],
        "SMA30" : data["d"][488],
        "EMA50" : data["d"][489],
        "SMA50" : data["d"][490],
        "EMA100" : data["d"][491],
        "SMA100" : data["d"][492],
        "EMA200" : data["d"][493],
        "SMA200" : data["d"][494],
        "Rec_Ichimoku" : data["d"][495],
        "Ichimoku_BLine" : data["d"][496],
        "Rec_VWMA" : data["d"][497],
        "VWMA" : data["d"][498],
        "Rec_HullMA9" : data["d"][499],
        "HullMA9" : data["d"][500],
        "Pivot_M_Classic_S3" : data["d"][501],
        "Pivot_M_Classic_S2" : data["d"][502],
        "Pivot_M_Classic_S1" : data["d"][503],
        "Pivot_M_Classic_Middle" : data["d"][504],
        "Pivot_M_Classic_R1" : data["d"][505],
        "Pivot_M_Classic_R2" : data["d"][506],
        "Pivot_M_Classic_R3" : data["d"][507],
        "Pivot_M_Fibonacci_S3" : data["d"][508],
        "Pivot_M_Fibonacci_S2" : data["d"][509],
        "Pivot_M_Fibonacci_S1" : data["d"][510],
        "Pivot_M_Fibonacci_Middle" : data["d"][511],
        "Pivot_M_Fibonacci_R1" : data["d"][512],
        "Pivot_M_Fibonacci_R2" : data["d"][513],
        "Pivot_M_Fibonacci_R3" : data["d"][514],
        "Pivot_M_Camarilla_S3" : data["d"][515],
        "Pivot_M_Camarilla_S2" : data["d"][516],
        "Pivot_M_Camarilla_S1" : data["d"][517],
        "Pivot_M_Camarilla_Middle" : data["d"][518],
        "Pivot_M_Camarilla_R1" : data["d"][519],
        "Pivot_M_Camarilla_R2" : data["d"][520],
        "Pivot_M_Camarilla_R3" : data["d"][521],
        "Pivot_M_Woodie_S3" : data["d"][522],
        "Pivot_M_Woodie_S2" : data["d"][523],
        "Pivot_M_Woodie_S1" : data["d"][524],
        "Pivot_M_Woodie_Middle" : data["d"][525],
        "Pivot_M_Woodie_R1" : data["d"][526],
        "Pivot_M_Woodie_R2" : data["d"][527],
        "Pivot_M_Woodie_R3" : data["d"][528],
        "Pivot_M_Demark_S1" : data["d"][529],
        "Pivot_M_Demark_Middle" : data["d"][530],
        "Pivot_M_Demark_R1" : data["d"][531],
        "Recommend_Other_1W" : data["d"][532],
        "Recommend_All_1W" : data["d"][533],
        "Recommend_MA_1W" : data["d"][534],
        "RSI_1W" : data["d"][535],
        "RSI_1__1W" : data["d"][536],
        "Stoch_K_1W" : data["d"][537],
        "Stoch_D_1W" : data["d"][538],
        "Stoch_K_1__1W" : data["d"][539],
        "Stoch_D_1__1W" : data["d"][540],
        "CCI20_1W" : data["d"][541],
        "CCI20_1__1W" : data["d"][542],
        "ADX_1W" : data["d"][543],
        "ADX+DI_1W" : data["d"][544],
        "ADX-DI_1W" : data["d"][545],
        "ADX+DI_1__1W" : data["d"][546],
        "ADX-DI_1__1W" : data["d"][547],
        "AO_1W" : data["d"][548],
        "AO_1__1W" : data["d"][549],
        "Mom_1W" : data["d"][550],
        "Mom_1__1W" : data["d"][551],
        "MACD_macd_1W" : data["d"][552],
        "MACD_signal_1W" : data["d"][553],
        "Rec_Stoch_RSI_1W" : data["d"][554],
        "Stoch_RSI_K_1W" : data["d"][555],
        "Rec_WR_1W" : data["d"][556],
        "W_R_1W" : data["d"][557],
        "Rec_BBPower_1W" : data["d"][558],
        "BBPower_1W" : data["d"][559],
        "Rec_UO_1W" : data["d"][560],
        "UO_1W" : data["d"][561],
        "EMA5_1W" : data["d"][562],
        "close_1W" : data["d"][563],
        "SMA5_1W" : data["d"][564],
        "EMA10_1W" : data["d"][565],
        "SMA10_1W" : data["d"][566],
        "EMA20_1W" : data["d"][567],
        "SMA20_1W" : data["d"][568],
        "EMA30_1W" : data["d"][569],
        "SMA30_1W" : data["d"][570],
        "EMA50_1W" : data["d"][571],
        "SMA50_1W" : data["d"][572],
        "EMA100_1W" : data["d"][573],
        "SMA100_1W" : data["d"][574],
        "EMA200_1W" : data["d"][575],
        "SMA200_1W" : data["d"][576],
        "Rec_Ichimoku_1W" : data["d"][577],
        "Ichimoku_BLine_1W" : data["d"][578],
        "Rec_VWMA_1W" : data["d"][579],
        "VWMA_1W" : data["d"][580],
        "Rec_HullMA9_1W" : data["d"][581],
        "HullMA9_1W" : data["d"][582],
        "Pivot_M_Classic_S3_1W" : data["d"][583],
        "Pivot_M_Classic_S2_1W" : data["d"][584],
        "Pivot_M_Classic_S1_1W" : data["d"][585],
        "Pivot_M_Classic_Middle_1W" : data["d"][586],
        "Pivot_M_Classic_R1_1W" : data["d"][587],
        "Pivot_M_Classic_R2_1W" : data["d"][588],
        "Pivot_M_Classic_R3_1W" : data["d"][589],
        "Pivot_M_Fibonacci_S3_1W" : data["d"][590],
        "Pivot_M_Fibonacci_S2_1W" : data["d"][591],
        "Pivot_M_Fibonacci_S1_1W" : data["d"][592],
        "Pivot_M_Fibonacci_Middle_1W" : data["d"][593],
        "Pivot_M_Fibonacci_R1_1W" : data["d"][594],
        "Pivot_M_Fibonacci_R2_1W" : data["d"][595],
        "Pivot_M_Fibonacci_R3_1W" : data["d"][596],
        "Pivot_M_Camarilla_S3_1W" : data["d"][597],
        "Pivot_M_Camarilla_S2_1W" : data["d"][598],
        "Pivot_M_Camarilla_S1_1W" : data["d"][599],
        "Pivot_M_Camarilla_Middle_1W" : data["d"][600],
        "Pivot_M_Camarilla_R1_1W" : data["d"][601],
        "Pivot_M_Camarilla_R2_1W" : data["d"][602],
        "Pivot_M_Camarilla_R3_1W" : data["d"][603],
        "Pivot_M_Woodie_S3_1W" : data["d"][604],
        "Pivot_M_Woodie_S2_1W" : data["d"][605],
        "Pivot_M_Woodie_S1_1W" : data["d"][606],
        "Pivot_M_Woodie_Middle_1W" : data["d"][607],
        "Pivot_M_Woodie_R1_1W" : data["d"][608],
        "Pivot_M_Woodie_R2_1W" : data["d"][609],
        "Pivot_M_Woodie_R3_1W" : data["d"][610],
        "Pivot_M_Demark_S1_1W" : data["d"][611],
        "Pivot_M_Demark_Middle_1W" : data["d"][612],
        "Pivot_M_Demark_R1_1W" : data["d"][613],
        "Recommend_Other_1M" : data["d"][614],
        "Recommend_All_1M" : data["d"][615],
        "Recommend_MA_1M" : data["d"][616],
        "RSI_1M" : data["d"][617],
        "RSI_1__1M" : data["d"][618],
        "Stoch_K_1M" : data["d"][619],
        "Stoch_D_1M" : data["d"][620],
        "Stoch_K_1__1M" : data["d"][621],
        "Stoch_D_1__1M" : data["d"][622],
        "CCI20_1M" : data["d"][623],
        "CCI20_1__1M" : data["d"][624],
        "ADX_1M" : data["d"][625],
        "ADX+DI_1M" : data["d"][626],
        "ADX-DI_1M" : data["d"][627],
        "ADX+DI_1__1M" : data["d"][628],
        "ADX-DI_1__1M" : data["d"][629],
        "AO_1M" : data["d"][630],
        "AO_1__1M" : data["d"][631],
        "Mom_1M" : data["d"][632],
        "Mom_1__1M" : data["d"][633],
        "MACD_macd_1M" : data["d"][634],
        "MACD_signal_1M" : data["d"][635],
        "Rec_Stoch_RSI_1M" : data["d"][636],
        "Stoch_RSI_K_1M" : data["d"][637],
        "Rec_WR_1M" : data["d"][638],
        "W_R_1M" : data["d"][639],
        "Rec_BBPower_1M" : data["d"][640],
        "BBPower_1M" : data["d"][641],
        "Rec_UO_1M" : data["d"][642],
        "UO_1M" : data["d"][643],
        "EMA5_1M" : data["d"][644],
        "close_1M" : data["d"][645],
        "SMA5_1M" : data["d"][646],
        "EMA10_1M" : data["d"][647],
        "SMA10_1M" : data["d"][648],
        "EMA20_1M" : data["d"][649],
        "SMA20_1M" : data["d"][650],
        "EMA30_1M" : data["d"][651],
        "SMA30_1M" : data["d"][652],
        "EMA50_1M" : data["d"][653],
        "SMA50_1M" : data["d"][654],
        "EMA100_1M" : data["d"][655],
        "SMA100_1M" : data["d"][656],
        "EMA200_1M" : data["d"][657],
        "SMA200_1M" : data["d"][658],
        "Rec_Ichimoku_1M" : data["d"][659],
        "Ichimoku_BLine_1M" : data["d"][660],
        "Rec_VWMA_1M" : data["d"][661],
        "VWMA_1M" : data["d"][662],
        "Rec_HullMA9_1M" : data["d"][663],
        "HullMA9_1M" : data["d"][664],
        "Pivot_M_Classic_S3_1M" : data["d"][665],
        "Pivot_M_Classic_S2_1M" : data["d"][666],
        "Pivot_M_Classic_S1_1M" : data["d"][667],
        "Pivot_M_Classic_Middle_1M" : data["d"][668],
        "Pivot_M_Classic_R1_1M" : data["d"][669],
        "Pivot_M_Classic_R2_1M" : data["d"][670],
        "Pivot_M_Classic_R3_1M" : data["d"][671],
        "Pivot_M_Fibonacci_S3_1M" : data["d"][672],
        "Pivot_M_Fibonacci_S2_1M" : data["d"][673],
        "Pivot_M_Fibonacci_S1_1M" : data["d"][674],
        "Pivot_M_Fibonacci_Middle_1M" : data["d"][675],
        "Pivot_M_Fibonacci_R1_1M" : data["d"][676],
        "Pivot_M_Fibonacci_R2_1M" : data["d"][677],
        "Pivot_M_Fibonacci_R3_1M" : data["d"][678],
        "Pivot_M_Camarilla_S3_1M" : data["d"][679],
        "Pivot_M_Camarilla_S2_1M" : data["d"][680],
        "Pivot_M_Camarilla_S1_1M" : data["d"][681],
        "Pivot_M_Camarilla_Middle_1M" : data["d"][682],
        "Pivot_M_Camarilla_R1_1M" : data["d"][683],
        "Pivot_M_Camarilla_R2_1M" : data["d"][684],
        "Pivot_M_Camarilla_R3_1M" : data["d"][685],
        "Pivot_M_Woodie_S3_1M" : data["d"][686],
        "Pivot_M_Woodie_S2_1M" : data["d"][687],
        "Pivot_M_Woodie_S1_1M" : data["d"][688],
        "Pivot_M_Woodie_Middle_1M" : data["d"][689],
        "Pivot_M_Woodie_R1_1M" : data["d"][690],
        "Pivot_M_Woodie_R2_1M" : data["d"][691],
        "Pivot_M_Woodie_R3_1M" : data["d"][692],
        "Pivot_M_Demark_S1_1M" : data["d"][693],
        "Pivot_M_Demark_Middle_1M" : data["d"][694],
        "Pivot_M_Demark_R1_1M" : data["d"][695]
        }
        save=dbnse['{}_TV'.format(symbol)].insert_one(post).inserted_id
        print(save)


def Plotindicator():
    #df=pd.DataFrame(df)
    chart=db.chart.find_one(sort=[('_id', pymongo.DESCENDING)])
    indicator=chart['technical']
    length=len(indicator)

    return length,indicator