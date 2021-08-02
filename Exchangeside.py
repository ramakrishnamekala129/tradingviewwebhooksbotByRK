from pprint import pprint
import json
import ccxt 
from actions import exchange
import datetime
import time
import numpy as np
import pandas as pd
from actions import signals
from database import db 
from sentiment import *
from actions import *
from actions import percentage
from Trade import *
import pymongo
'''
symbol='BTC/USD'
types='Stop'
side='buy'
'''
def symbolizer(symbol):
    if symbol == 'ETH/USD':
        symbol='ETHUSD'
    elif symbol == 'BTC/USD':
        symbol = 'XBTUSD'
    else:
        symbol='Error Ocurred'
    return symbol
def desymbolizer(symbol):
    if symbol == 'ETHUSD':
        symbol='ETH/USD'
    elif symbol == 'XBTUSD':
        symbol = 'BTC/USD'
    else:
        symbol='Error Ocurred'
    return symbol
def pricepercent(symbol,percent):
    if 'ETH/USD' == symbol:
        dba='ethusdt'
    elif 'BTC/USD' == symbol:
        dba='btcusdt'
    else:
        print('Error ocurred')
    price=db[dba].find_one(sort=[('_id', pymongo.DESCENDING)])['close']
    percent=percent/100
    price=int(price*percent)
    return price
def stoppricepercent(symbol,percent,side):
    if 'ETH/USD' == symbol:
        dba='ethusdt'
    elif 'BTC/USD' == symbol:
        dba='btcusdt'
    else:
        print('Error ocurred')
    price=db[dba].find_one(sort=[('_id', pymongo.DESCENDING)])['close']
    percent=percent/100
    price1=int(price*percent)
    if side == 'sell':
        price2=price-price1
    elif side == 'buy':
        price2=price+price1
    return int(price2)
def takeprofitpercent(symbol,percent,side):
    if 'ETH/USD' == symbol:
        dba='ethusdt'
    elif 'BTC/USD' == symbol:
        dba='btcusdt'
    else:
        print('Error ocurred')
    price=db[dba].find_one(sort=[('_id', pymongo.DESCENDING)])['close']
    percent=percent/100
    price1=int(price*percent)
    if side == 'sell':
        price2=price+price1
    elif side == 'buy':
        price2=price-price1
    return int(price2)
#params={'stopPx':pricepercent(symbol,5),'ordType': 'Stop','pegPriceType': 'TrailingStopPeg','pegOffsetValue': 50}
def trailoffset(value,side):
    if side == 'buy':
        value1=value
    elif side == 'sell':
        value1=-value
    else:
        print('Error ocurred')
    return value1



def Stoploss(symbol,side,percentage,amount):
    position=exchange.private_get_position({'filter': json.dumps({"isOpen": True})})
    data1=exchange.fetch_open_orders()
    if (not data1):
        if position:
            for check in position:

                if symbol == desymbolizer(check['symbol']):

                    types='Stop'
                    #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                    if side == 'buy':
                        side='sell'
                    elif side == 'sell':
                        side = 'buy'
                    else:
                        print('Error ocurred')
                    params={'stopPx':stoppricepercent(symbol,percentage,side),'execInst': 'Close','ordType':'Stop'}
                    p=exchange.create_order(symbol, types, side,amount,None,params=params)
                    return p
    if  data1:
        listing=[]
        for data in data1:
            listing.append(data['symbol'])
        for data in data1:
            #listing.append(data['symbol'])
            if symbol in listing:
                return print('Skip')
            if not symbol in listing:
                if position:
                    for check in position:

                        if symbol == desymbolizer(check['symbol']):

                            types='Stop'
                            #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                            if side == 'buy':
                                side='sell'
                            elif side == 'sell':
                                side = 'buy'
                            else:
                                print('Error ocurred')
                            params={'stopPx':stoppricepercent(symbol,percentage,side),'execInst': 'Close','ordType':'Stop'}
                            p=exchange.create_order(symbol, types, side,amount,None,params=params)
                            return p 
def trailingStoploss(symbol,side,percentage,amount):
    position=exchange.private_get_position({'filter': json.dumps({"isOpen": True})})
    data1=exchange.fetch_open_orders()
    if (not data1):
        if position:
            for check in position:

                if symbol == desymbolizer(check['symbol']):
                    types='Stop'
                    #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                    if side == 'buy':
                        side='sell'
                    elif side == 'sell':
                        side = 'buy'
                    else:
                        print('Error ocurred')
                    params={'stopPx':stoppricepercent(symbol,percentage,side),'execInst': 'Close','ordType': 'Stop','pegPriceType': 'TrailingStopPeg','pegOffsetValue': trailoffset(pricepercent(symbol,percentage),side)}
                    p=exchange.create_order(symbol, types, side,amount,None,params=params)
                    return p
    if  data1:
        listing=[]
        for data in data1:
            listing.append(data['symbol'])
        for data in data1:
            #listing.append(data['symbol'])
            if symbol in listing:
                return print('Skip')
            if not symbol in listing:
                if position:
                    for check in position:
                        if symbol == desymbolizer(check['symbol']):
                            types='Stop'
                            #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                            if side == 'buy':
                                side='sell'
                            elif side == 'sell':
                                side = 'buy'
                            else:
                                print('Error ocurred')
                            params={'stopPx':stoppricepercent(symbol,percentage,side),'execInst': 'Close','ordType': 'Stop','pegPriceType': 'TrailingStopPeg','pegOffsetValue': trailoffset(pricepercent(symbol,percentage),side)}
                            p=exchange.create_order(symbol, types, side,amount,None,params=params)
                            return p
def take_profit(symbol,side,percentage,amount):
    position=exchange.private_get_position({'filter': json.dumps({"isOpen": True})})
    data1=exchange.fetch_open_orders()
    if (not data1):
        if position:
            for check in position:

                if symbol == desymbolizer(check['symbol']):

                    types='Stop'
                    #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                    if side == 'buy':
                        side='sell'
                    elif side == 'sell':
                        side = 'buy'
                    else:
                        print('Error ocurred')
                    params={'stopPx':takeprofitpercent(symbol,percentage,side),'execInst': 'Close','ordType': 'MarketIfTouched'}
                    p=exchange.create_order(symbol, types, side,amount,None,params=params)
                    return p
    if  data1:
        listing=[]
        for data in data1:
            listing.append(data['symbol'])
        for data in data1:
            #listing.append(data['symbol'])
            if symbol in listing:
                return print('Skip')
            if not symbol in listing:
                if position:
                    for check in position:

                        if symbol == desymbolizer(check['symbol']):

                            types='Stop'
                            #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                            if side == 'buy':
                                side='sell'
                            elif side == 'sell':
                                side = 'buy'
                            else:
                                print('Error ocurred')
                            params={'stopPx':takeprofitpercent(symbol,percentage,side),'execInst': 'Close','ordType': 'MarketIfTouched'}
                            p=exchange.create_order(symbol, types, side,amount,None,params=params)
                            return p

def Limit_Stoploss(symbol,side,percentage,amount,limit):
    position=exchange.private_get_position({'filter': json.dumps({"isOpen": True})})
    data1=exchange.fetch_open_orders()
    if (not data1):
        if position:
            for check in position:

                if symbol == desymbolizer(check['symbol']):

                    types='StopLimit'
                    #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                    if side == 'buy':
                        side='sell'
                    elif side == 'sell':
                        side = 'buy'
                    else:
                        print('Error ocurred')
                    params={'stopPx':stoppricepercent(symbol,percentage,side),'execInst': 'Close','ordType':'Stop'}
                    p=exchange.create_order(symbol, types, side,amount,limit,params=params)
                    return p
    if  data1:
        listing=[]
        for data in data1:
            listing.append(data['symbol'])
        for data in data1:
            #listing.append(data['symbol'])
            if symbol in listing:
                return print('Skip')
            if not symbol in listing:
                if position:
                    for check in position:

                        if symbol == desymbolizer(check['symbol']):

                            types='StopLimit'
                            #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                            if side == 'buy':
                                side='sell'
                            elif side == 'sell':
                                side = 'buy'
                            else:
                                print('Error ocurred')
                            params={'stopPx':stoppricepercent(symbol,percentage,side),'execInst': 'Close','ordType':'Stop'}
                            p=exchange.create_order(symbol, types, side,amount,limit,params=params)
                            return p 


def Limit_take_profit(symbol,side,percentage,amount,limit):
    position=exchange.private_get_position({'filter': json.dumps({"isOpen": True})})
    data1=exchange.fetch_open_orders()
    if (not data1):
        if position:
            for check in position:

                if symbol == desymbolizer(check['symbol']):

                    types='LimitIfTouched'
                    #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                    if side == 'buy':
                        side='sell'
                    elif side == 'sell':
                        side = 'buy'
                    else:
                        print('Error ocurred')
                    params={'stopPx':takeprofitpercent(symbol,percentage,side),'execInst': 'Close','ordType': 'MarketIfTouched'}
                    p=exchange.create_order(symbol, types, side,amount,limit,params=params)
                    return p
    if  data1:
        listing=[]
        for data in data1:
            listing.append(data['symbol'])
        for data in data1:
            #listing.append(data['symbol'])
            if symbol in listing:
                return print('Skip')
            if not symbol in listing:
                if position:
                    for check in position:

                        if symbol == desymbolizer(check['symbol']):

                            types='LimitIfTouched'
                            #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                            if side == 'buy':
                                side='sell'
                            elif side == 'sell':
                                side = 'buy'
                            else:
                                print('Error ocurred')
                            params={'stopPx':takeprofitpercent(symbol,percentage,side),'execInst': 'Close','ordType': 'MarketIfTouched'}
                            p=exchange.create_order(symbol, types, side,amount,limit,params=params)
                            return p

def Direct_Stoploss(symbol,side,percentage,amount):
    position=exchange.private_get_position({'filter': json.dumps({"isOpen": True})})
    data1=exchange.fetch_open_orders()
    if (not data1):
        if position:
            for check in position:

                if symbol == desymbolizer(check['symbol']):

                    types='Stop'
                    #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                    if side == 'buy':
                        side='sell'
                    elif side == 'sell':
                        side = 'buy'
                    else:
                        print('Error ocurred')
                    params={'stopPx':percentage,'execInst': 'Close','ordType':'Stop'}
                    p=exchange.create_order(symbol, types, side,amount,None,params=params)
                    return p
    if  data1:
        listing=[]
        for data in data1:
            listing.append(data['symbol'])
        for data in data1:
            #listing.append(data['symbol'])
            if symbol in listing:
                return print('Skip')
            if not symbol in listing:
                if position:
                    for check in position:

                        if symbol == desymbolizer(check['symbol']):

                            types='Stop'
                            #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                            if side == 'buy':
                                side='sell'
                            elif side == 'sell':
                                side = 'buy'
                            else:
                                print('Error ocurred')
                            params={'stopPx':percentage,'execInst': 'Close','ordType':'Stop'}
                            p=exchange.create_order(symbol, types, side,amount,None,params=params)
                            return p 
def Direct_trailingStoploss(symbol,side,percentage,amount):
    position=exchange.private_get_position({'filter': json.dumps({"isOpen": True})})
    data1=exchange.fetch_open_orders()
    if (not data1):
        if position:
            for check in position:

                if symbol == desymbolizer(check['symbol']):
                    types='Stop'
                    #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                    if side == 'buy':
                        side='sell'
                    elif side == 'sell':
                        side = 'buy'
                    else:
                        print('Error ocurred')
                    params={'stopPx':percentage,'execInst': 'Close','ordType': 'Stop','pegPriceType': 'TrailingStopPeg','pegOffsetValue': trailoffset(pricepercent(symbol,percentage),side)}
                    p=exchange.create_order(symbol, types, side,amount,None,params=params)
                    return p
    if  data1:
        listing=[]
        for data in data1:
            listing.append(data['symbol'])
        for data in data1:
            #listing.append(data['symbol'])
            if symbol in listing:
                return print('Skip')
            if not symbol in listing:
                if position:
                    for check in position:
                        if symbol == desymbolizer(check['symbol']):
                            types='Stop'
                            #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                            if side == 'buy':
                                side='sell'
                            elif side == 'sell':
                                side = 'buy'
                            else:
                                print('Error ocurred')
                            params={'stopPx':percentage,'execInst': 'Close','ordType': 'Stop','pegPriceType': 'TrailingStopPeg','pegOffsetValue': trailoffset(pricepercent(symbol,percentage),side)}
                            p=exchange.create_order(symbol, types, side,amount,None,params=params)
                            return p
def Direct_take_profit(symbol,side,percentage,amount):
    position=exchange.private_get_position({'filter': json.dumps({"isOpen": True})})
    data1=exchange.fetch_open_orders()
    if (not data1):
        if position:
            for check in position:

                if symbol == desymbolizer(check['symbol']):

                    types='Stop'
                    #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                    if side == 'buy':
                        side='sell'
                    elif side == 'sell':
                        side = 'buy'
                    else:
                        print('Error ocurred')
                    params={'stopPx':percentage,'execInst': 'Close','ordType': 'MarketIfTouched'}
                    p=exchange.create_order(symbol, types, side,amount,None,params=params)
                    return p
    if  data1:
        listing=[]
        for data in data1:
            listing.append(data['symbol'])
        for data in data1:
            #listing.append(data['symbol'])
            if symbol in listing:
                return print('Skip')
            if not symbol in listing:
                if position:
                    for check in position:

                        if symbol == desymbolizer(check['symbol']):

                            types='Stop'
                            #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                            if side == 'buy':
                                side='sell'
                            elif side == 'sell':
                                side = 'buy'
                            else:
                                print('Error ocurred')
                            params={'stopPx':percentage,'execInst': 'Close','ordType': 'MarketIfTouched'}
                            p=exchange.create_order(symbol, types, side,amount,None,params=params)
                            return p

def Direct_Limit_Stoploss(symbol,side,percentage,amount,limit):
    position=exchange.private_get_position({'filter': json.dumps({"isOpen": True})})
    data1=exchange.fetch_open_orders()
    if (not data1):
        if position:
            for check in position:

                if symbol == desymbolizer(check['symbol']):

                    types='StopLimit'
                    #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                    if side == 'buy':
                        side='sell'
                    elif side == 'sell':
                        side = 'buy'
                    else:
                        print('Error ocurred')
                    params={'stopPx':percentage,'execInst': 'Close','ordType':'Stop'}
                    p=exchange.create_order(symbol, types, side,amount,limit,params=params)
                    return p
    if  data1:
        listing=[]
        for data in data1:
            listing.append(data['symbol'])
        for data in data1:
            #listing.append(data['symbol'])
            if symbol in listing:
                return print('Skip')
            if not symbol in listing:
                if position:
                    for check in position:

                        if symbol == desymbolizer(check['symbol']):

                            types='StopLimit'
                            #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                            if side == 'buy':
                                side='sell'
                            elif side == 'sell':
                                side = 'buy'
                            else:
                                print('Error ocurred')
                            params={'stopPx':percentage,'execInst': 'Close','ordType':'Stop'}
                            p=exchange.create_order(symbol, types, side,amount,limit,params=params)
                            return p 


def Direct_Limit_take_profit(symbol,side,percentage,amount,limit):
    position=exchange.private_get_position({'filter': json.dumps({"isOpen": True})})
    data1=exchange.fetch_open_orders()
    if (not data1):
        if position:
            for check in position:

                if symbol == desymbolizer(check['symbol']):

                    types='LimitIfTouched'
                    #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                    if side == 'buy':
                        side='sell'
                    elif side == 'sell':
                        side = 'buy'
                    else:
                        print('Error ocurred')
                    params={'stopPx':percentage,'execInst': 'Close','ordType': 'MarketIfTouched'}
                    p=exchange.create_order(symbol, types, side,amount,limit,params=params)
                    return p
    if  data1:
        listing=[]
        for data in data1:
            listing.append(data['symbol'])
        for data in data1:
            #listing.append(data['symbol'])
            if symbol in listing:
                return print('Skip')
            if not symbol in listing:
                if position:
                    for check in position:

                        if symbol == desymbolizer(check['symbol']):

                            types='LimitIfTouched'
                            #params={'stopPx':stoppricepercent(symbol,5,side),'execInst': 'Close','ordType':'Stop'}
                            if side == 'buy':
                                side='sell'
                            elif side == 'sell':
                                side = 'buy'
                            else:
                                print('Error ocurred')
                            params={'stopPx':percentage,'execInst': 'Close','ordType': 'MarketIfTouched'}
                            p=exchange.create_order(symbol, types, side,amount,limit,params=params)
                            return p



def riskmanager(symbol):
    position=exchange.private_get_position({'filter': json.dumps({"isOpen": True})})
    print(position)
    data1=exchange.fetch_open_orders()
    print(data1)
    if not position:
            for data in data1:
                print(data['info']['symbol'])
                if symbol == desymbolizer(data['info']['symbol']):
                    #order = list(db.riskmanager.find({'symbol':symbol}).sort("_id", pymongo.DESCENDING).limit(1))
                    #orderid=order[0]['orderID']
                    orderid=data['info']['orderID']
                    data=exchange.cancel_order(orderid)
                    #print(p)
                    print(data['symbol'])
                    post={
                            'date':datetime.datetime.now(),
                            'orderID':data['info']['orderID'],
                            'clOrdID':data['info']['clOrdID'],
                            'clOrdLinkID':data['info']['clOrdLinkID'],
                            'account':data['info']['account'],
                            'symbol1':data['info']['symbol'],
                            'side':data['info']['side'],
                            'simpleOrderQty':data['info']['simpleOrderQty'],
                            'orderQty':data['info']['orderQty'],
                            'price':data['info']['price'],
                            'displayQty':data['info']['displayQty'],
                            'stopPx':data['info']['stopPx'],
                            'pegOffsetValue':data['info']['pegOffsetValue'],
                            'pegPriceType':data['info']['pegPriceType'],
                            'currency':data['info']['currency'],
                            'settlCurrency':data['info']['settlCurrency'],
                            'ordType':data['info']['ordType'],
                            'timeInForce':data['info']['timeInForce'],
                            'execInst':data['info']['execInst'],
                            'contingencyType':data['info']['contingencyType'],
                            'exDestination':data['info']['exDestination'],
                            'ordStatus':data['info']['ordStatus'],
                            'triggered':data['info']['triggered'],
                            'workingIndicator':data['info']['workingIndicator'],
                            'ordRejReason':data['info']['ordRejReason'],
                            'simpleLeavesQty':data['info']['simpleLeavesQty'],
                            'leavesQty':data['info']['leavesQty'],
                            'simpleCumQty':data['info']['simpleCumQty'],
                            'cumQty':data['info']['cumQty'],
                            'avgPx':data['info']['avgPx'],
                            'multiLegReportingType':data['info']['multiLegReportingType'],
                            'text':data['info']['text'],
                            'transactTime':data['info']['transactTime'],
                            'timestamp':data['info']['timestamp'],
                            'id':data['id'],
                            'timestamp':data['timestamp'],
                            'datetime':data['datetime'],
                            'lastTradeTimestamp':data['lastTradeTimestamp'],
                            'symbol':data['symbol'],
                            'type':data['type'],
                            'side':data['side'],
                            'price':data['price'],
                            'amount':data['amount'],
                            'cost':data['cost'],
                            'average':data['average'],
                            'filled':data['filled'],
                            'remaining':data['remaining'],
                            'status':data['status'],
                            'fee':data['fee']

                            }


                    print(post)



def RiskAssigner(riskmanage,post,side):
    if side == 'buy':

        if riskmanage == 'Stop Loss':
            riskpercent=int(post['LongStoploss'])
        if riskmanage == 'Trailing Stop':
            riskpercent=int(post['LongStoploss'])
        if riskmanage == 'Take Profit':
            riskpercent=int(post['LongSecondTarget'])
    if side == 'sell':
        
        if riskmanage == 'Stop Loss':
            riskpercent=int(post['ShortStoploss'])
        if riskmanage == 'Trailing Stop':
            riskpercent=int(post['ShortStoploss'])
        if riskmanage == 'Take Profit':
            riskpercent=int(post['ShortSecondTarget'])

    return riskpercent
