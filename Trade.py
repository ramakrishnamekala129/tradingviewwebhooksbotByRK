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
from sentiment import today_sentiment
from actions import *
import pymongo
from sentiment import *
from Exchangeside import *
import dateutil
from Strategy import Gann_Targets,Gann_Volality_Targets



order=list(db.order.find())
btcusdt=signals(list(db.btcusdt.find())[-1]['recommendall1'])
ethusdt=list(db.ethusdt.find())
order=pd.DataFrame(order)
#pprint(order)


def riskmanagement(riskmanagement,symbol,side,riskpercent,qty,price):
    symbol=str(symbol)
    side=str(side)
    riskpercent=int(riskpercent)
    qty=int(qty)
    price=int(price)
    if riskmanagement == 'Trailing Stop':
        trailingStoploss(symbol,side,riskpercent,qty)
    elif riskmanagement == 'Stop Loss':
        if type == 'Market':
            Stoploss(symbol,side,riskpercent,qty)
        elif type == 'Limit':
            Limit_Stoploss(symbol,side,riskpercent,qty,price)
        else:
            print('Error in riskmanagement')
    elif riskmanagement == 'Take Profit':
        if type == 'Market':
            take_profit(symbol,side,riskpercent,qty)
        elif type == 'Limit':
            Limit_take_profit(symbol,side,riskpercent,qty,price)
        else:
            print('Error in riskmanagement')
    else:
        print('None of Risk Management')



def Direct_riskmanagement(riskmanagement,type,symbol,side,riskpercent,qty,price):
    symbol=str(symbol)
    side=str(side)
    riskpercent=int(riskpercent)
    qty=int(qty)
    price=int(price)
    if riskmanagement == 'Trailing Stop':
        Direct_trailingStoploss(symbol,side,riskpercent,qty)
    elif riskmanagement == 'Stop Loss':
        if type == 'Market':
            Direct_Stoploss(symbol,side,riskpercent,qty)
        elif type == 'Limit':
            Direct_Limit_Stoploss(symbol,side,riskpercent,qty,price)
        else:
            print('Error Stoploss in Directriskmanagement')
    elif riskmanagement == 'Take Profit':
        if type == 'Market':
            Direct_take_profit(symbol,side,riskpercent,qty)
        elif type == 'Limit':
            Direct_Limit_take_profit(symbol,side,riskpercent,qty,price)
        else:
            print('Error take profit in Directriskmanagement')
    else:
        print('None of Risk Management')


def oldStrategyExecutor(btcusdt):
    strategy=list(db.strategy.find())[-1]
    signal1=StrategySelector(strategy['signal1'])
    signal2=StrategySelector(strategy['signal2'])
    signal3=StrategySelector(strategy['signal3'])
    signal4=strategy['signal4']
    signal5=strategy['strategy']
    qty=strategy['Qty']
    mode=strategy['mode']
    type=strategy['ordertype']
    riskmanagement=strategy['riskmanagement']
    signal1=btcusdt[signal1]
    signal2=btcusdt[signal2]
    signal3=btcusdt[signal3]
    price=btcusdt['close']
    symbol=btcusdt['symbol'].replace("BINANCE:","")
    if symbol == 'BTCUSDT':
        symbol='BTC/USD'
    elif symbol == 'ETHUSDT':
        symbol='ETH/USD'
    #print(signal4)

    if signal4 == 'Sentiment Analysis':
        signal4=todays_sentiment()
    else:
        signal4=signal2

    if signal5 == 'TradingView':
        signal5=signaltonumber(list(db.order.find({'symbol':symbol}))[-1]['side'].upper())
        print(signal5)
    else:
        signal5=signal3

    if mode == 'Percent':
        qty=percent(int(qty))
    else:
        qty=qty

    Trade_Management(exchange)


    if symbol == 'ETH/USD':
        d='ETHUSD'
    elif symbol == 'BTC/USD':
        d= 'XBTUSD'
    else:
        print(' ENTER A VALID COIN ')


    position=list(db.position.find({'symbol':d}))[-1]
    if position['isOpen'] == False:
        if signal1 > 0 and signal2 > 0 and signal3 > 0 and signal4 > 0 and signal5 > 0:
            print('Long Entry')
            side='buy'
            entry(symbol,type,side,qty,price)
        elif signal1 < 0 and signal2 < 0 and signal3 < 0 and signal4 < 0 and signal5 < 0:
            print('Short Entry')
            #params={'execInst': 'Close'}
            side='sell'
            entry(symbol,type,side,qty,price)
    elif position['isOpen'] == True:
        if position['currentQty'] < 0:
            if signal1 > 0 and signal2 > 0 and signal3 > 0 and signal4 > 0 and signal5 > 0:
                print('Short Exit')
                params={'execInst': 'Close'}
                side='buy'
                amount=abs(position['currentQty'])
                exit(symbol,type,side,amount,price,params=params)
        elif position['currentQty'] > 0:
            if signal1 < 0 and signal2 < 0 and signal3 < 0 and signal4 < 0 and signal5 < 0:
                print('Long Exit')
                params={'execInst': 'Close'}
                side='sell'
                amount=abs(position['currentQty'])
                exit(symbol,type,side,int(amount),price,params)
def StrategyExecutor(btcusdt):
    #strategy=list(db.strategy.find())[-1]
    strategy=db.strategy.find_one(sort=[('_id', pymongo.DESCENDING)])
    signal1=StrategySelector(strategy['signal1'])
    signal2=StrategySelector(strategy['signal2'])
    signal3=StrategySelector(strategy['signal3'])
    signal4=strategy['signal4']
    signal5=strategy['strategy']
    qty=strategy['Qty']
    mode=strategy['mode']
    type=strategy['ordertype']
    riskmanage=strategy['riskmanagement']
    riskmode=strategy['riskmode']
    riskpercent = strategy['riskquantity']
    signal1=btcusdt[signal1]
    signal2=btcusdt[signal2]
    signal3=btcusdt[signal3]
    price=btcusdt['close']
    symbol=btcusdt['symbol'].replace("BINANCE:","")
    if symbol == 'BTCUSDT':
        symbol='BTC/USD'
    elif symbol == 'ETHUSDT':
        symbol='ETH/USD'
    #print(signal4)

    if signal4 == 'Sentiment Analysis':
        signal4=todays_sentiment()
    else:
        signal4=signal2

    if signal5 == 'TradingView':
        signal5=signaltonumber(list(db.order.find({'symbol':symbol}))[-1]['side'].upper())
        print(signal5)
    else:
        signal5=signal3

    if mode == 'Percent':
        qty=percent(int(qty))
    else:
        qty=qty

    Trade_Management(exchange)


    if symbol == 'ETH/USD':
        d='ETHUSD'
    elif symbol == 'BTC/USD':
        d= 'XBTUSD'
    else:
        print(' ENTER A VALID COIN ')






    #position=list(db.position.find({'symbol':d}))[-1]
    position=db.position.find_one({'symbol':d},sort=[('_id', pymongo.DESCENDING)])
    if position:
        if position['isOpen'] == False:
            if signal1 > 0 and signal2 > 0 and signal3 > 0 and signal4 > 0 and signal5 > 0:
                print('Long Entry')
                side='buy'
                entry(symbol,type,side,qty,price)
                riskmanagement(riskmanage,symbol,side,riskpercent,qty,price)
            elif signal1 < 0 and signal2 < 0 and signal3 < 0 and signal4 < 0 and signal5 < 0:
                print('Short Entry')
                #params={'execInst': 'Close'}
                side='sell'
                entry(symbol,type,side,qty,price)
                riskmanagement(riskmanage,symbol,side,riskpercent,qty,price)
        elif position['isOpen'] == True:
            if position['currentQty'] < 0:
                if signal1 > 0 and signal2 > 0 and signal3 > 0 and signal4 > 0 and signal5 > 0:
                    print('Short Exit')
                    params={'execInst': 'Close'}
                    side='buy'
                    amount=abs(position['currentQty'])
                    exit(symbol,type,side,amount,price,params=params)
            elif position['currentQty'] > 0:
                if signal1 < 0 and signal2 < 0 and signal3 < 0 and signal4 < 0 and signal5 < 0:
                    print('Long Exit')
                    params={'execInst': 'Close'}
                    side='sell'
                    amount=abs(position['currentQty'])
                    exit(symbol,type,side,int(amount),price,params)
        riskmanager(symbol)

def GannStrategyExecutor(btcusdt):
    #strategy=list(db.strategy.find())[-1]
    strategy=db.strategy.find_one(sort=[('_id', pymongo.DESCENDING)])
    signal1=StrategySelector(strategy['signal1'])
    signal2=StrategySelector(strategy['signal2'])
    signal3=StrategySelector(strategy['signal3'])
    signal4=strategy['signal4']
    signal5=strategy['strategy']
    qty=strategy['Qty']
    mode=strategy['mode']
    type=strategy['ordertype']
    riskmanage=strategy['riskmanagement']
    riskmode=strategy['riskmode']
    riskpercent = strategy['riskquantity']
    price=btcusdt['close']
    symbol=btcusdt['symbol'].replace("BINANCE:","")
    post=Gann_Targets(symbol)
    currentprice=db['{}_1m'.format(symbol)].find_one(sort=[('_id', pymongo.DESCENDING)])
    if symbol == 'BTCUSDT':
        symbol='BTC/USD'
    elif symbol == 'ETHUSDT':
        symbol='ETH/USD'
    #print(signal4)

    if signal4 == 'Sentiment Analysis':
        signal4=todays_sentiment()
    else:
        signal4=signal2

    if signal5 == 'TradingView':
        signal5=signaltonumber(list(db.order.find({'symbol':symbol}))[-1]['side'].upper())
        print(signal5)
    else:
        signal5=signal3

    if mode == 'Percent':
        qty=percent(int(qty))
    else:
        qty=qty

    Trade_Management(exchange)


    if symbol == 'ETH/USD':
        d='ETHUSD'
    elif symbol == 'BTC/USD':
        d= 'XBTUSD'
    else:
        print(' ENTER A VALID COIN ')






    #position=list(db.position.find({'symbol':d}))[-1]
    position=db.position.find_one({'symbol':d},sort=[('_id', pymongo.DESCENDING)])
    if position:
        if position['isOpen'] == False:
            if currentprice['Close'] > post['LongEntry']:
                print('Long Entry')
                side='buy'
                entry(symbol,type,side,qty,price)
                Direct_riskmanagement(riskmanage,symbol,side,RiskAssigner(riskmanage,post,side),qty,price)
            elif currentprice['Close'] < post['ShortEntry']:
                print('Short Entry')
                #params={'execInst': 'Close'}
                side='sell'
                entry(symbol,type,side,qty,price)
                Direct_riskmanagement(riskmanage,symbol,side,RiskAssigner(riskmanage,post,side),qty,price)
        elif position['isOpen'] == True:
            if position['currentQty'] < 0:
                if currentprice['Close'] < post['ShortSecondTarget']:
                    print('Short Exit')
                    params={'execInst': 'Close'}
                    side='buy'
                    amount=abs(position['currentQty'])
                    exit(symbol,type,side,amount,price,params=params)
            elif position['currentQty'] > 0:
                if currentprice['Close'] > post['LongSecondTarget']:
                    print('Long Exit')
                    params={'execInst': 'Close'}
                    side='sell'
                    amount=abs(position['currentQty'])
                    exit(symbol,type,side,int(amount),price,params)
        riskmanager(symbol)

def GannStrategyExecutor1(btcusdt):
    #strategy=list(db.strategy.find())[-1]
    strategy=db.strategy.find_one(sort=[('_id', pymongo.DESCENDING)])
    signal1=StrategySelector(strategy['signal1'])
    signal2=StrategySelector(strategy['signal2'])
    signal3=StrategySelector(strategy['signal3'])
    signal4=strategy['signal4']
    signal5=strategy['strategy']
    qty=strategy['Qty']
    mode=strategy['mode']
    type=strategy['ordertype']
    riskmanage=strategy['riskmanagement']
    riskmode=strategy['riskmode']
    riskpercent = strategy['riskquantity']
    price=btcusdt['close']
    symbol=btcusdt['symbol'].replace("BINANCE:","")
    #post=Gann_Targets(symbol)
    post=Gann_Volality_Targets(symbol)
    currentprice=db['{}_1m'.format(symbol)].find_one(sort=[('_id', pymongo.DESCENDING)])
    if symbol == 'BTCUSDT':
        symbol='BTC/USD'
    elif symbol == 'ETHUSDT':
        symbol='ETH/USD'
    #print(signal4)

    if signal4 == 'Sentiment Analysis':
        signal4=todays_sentiment()
    else:
        signal4=signal2

    if signal5 == 'TradingView':
        signal5=signaltonumber(list(db.order.find({'symbol':symbol}))[-1]['side'].upper())
        print(signal5)
    else:
        signal5=signal3

    if mode == 'Percent':
        qty=percent(int(qty))
    else:
        qty=qty

    Trade_Management(exchange)


    if symbol == 'ETH/USD':
        d='ETHUSD'
    elif symbol == 'BTC/USD':
        d= 'XBTUSD'
    else:
        print(' ENTER A VALID COIN ')





    #position=list(db.position.find({'symbol':d}))[-1]
    position=db.position.find_one({'symbol':d},sort=[('_id', pymongo.DESCENDING)])
    if position:
        if position['isOpen'] == False:
            if currentprice['Close'] > post['LongEntry']:
                print('Long Entry')
                side='buy'
                entry(symbol,type,side,qty,price)
                #Direct_Stoploss(symbol,side,post['LongStoploss'],qty)
                '''params = {
                        'stopPx': int(post['LongStoploss'])  # if needed
                    }

                order = exchange.create_order(symbol, 'Stop', 'sell', qty, None, params)'''
                Direct_riskmanagement(riskmanage,type,symbol,side,RiskAssigner(riskmanage,post,side),qty,price)
            elif currentprice['Close'] < post['ShortEntry']:
                print('Short Entry')
                #params={'execInst': 'Close'}
                side='sell'
                entry(symbol,type,side,qty,price)
                #Direct_Stoploss(symbol,side,post['ShortStoploss'],qty)
                Direct_riskmanagement(riskmanage,type,symbol,side,RiskAssigner(riskmanage,post,side),qty,price)
                '''params = {
                        'stopPx': int(post['ShortStoploss'])  # if needed
                    }

                order = exchange.create_order(symbol, 'Stop', 'buy', qty, None, params)'''
                
        elif position['isOpen'] == True:
            if position['currentQty'] < 0:
                if currentprice['Close'] < post['ShortSecondTarget']:
                    print('Short Exit')
                    params={'execInst': 'Close'}
                    side='buy'
                    amount=abs(position['currentQty'])
                    exit(symbol,type,side,amount,price,params=params)
            elif position['currentQty'] > 0:
                if currentprice['Close'] > post['LongSecondTarget']:
                    print('Long Exit')
                    params={'execInst': 'Close'}
                    side='sell'
                    amount=abs(position['currentQty'])
                    exit(symbol,type,side,int(amount),price,params)
        riskmanager(symbol)


def strategyexecutor():
    ethusdt=db.ethusdt.find_one(sort=[('_id', pymongo.DESCENDING)])
    #StrategyExecutor(ethusdt)
    GannStrategyExecutor1(ethusdt)

def side(data):
    if data['currentQty'] > 0:
        side='Long'
    else:
        side='Short'
    return side




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
                #'openingTimestamp':dateutil.parser.isoparse(data['openingTimestamp']),
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
        if k:
            k=k['_id']
            myquery = { "_id": k }
            d=False
            newvalues = { "$set": { 'isOpen': d } }
            k=position.update_one(myquery, newvalues)
        else:
            print('')
        position=db.position
        k=db.position.find_one({'symbol':'ETHUSD'},sort=[('_id', pymongo.DESCENDING)])
        if k:
            k=k['_id']
            #print(k)
            myquery = { "_id": k }
            d=False
            newvalues = { "$set": { 'isOpen': d } }
            k=position.update_one(myquery, newvalues)
        else:
            print('')

def oldTrade_Management2(exchange):
    data1=exchange.private_get_position({'filter': json.dumps({"isOpen": True})})
    #data=data[0]
    if data1 :
        for data in data1:
            position=db.position
            p=list(db.position.find({'symbol':data['symbol']}).sort("_id", pymongo.DESCENDING).limit(1))
            p=p[0]
            if p['isOpen'] == False:    
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
                'openingTimestamp':data['openingTimestamp'],
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
                'currentTimestamp':data['currentTimestamp'],
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
                'timestamp':data['timestamp'],
                'lastPrice':data['lastPrice'],
                'lastValue':data['lastValue'],
                'Side':side(data)}

                #print(data)

                position=db.position
                position_id=position.insert_one(post).inserted_id
                print(position_id)
            else:
                position=db.position
                k=list(position.find({'symbol':data['symbol']}).sort("_id", pymongo.DESCENDING).limit(1))
                k=k[0]['_id']
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
                'openingTimestamp':data['openingTimestamp'],
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
                'currentTimestamp':data['currentTimestamp'],
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
                'timestamp':data['timestamp'],
                'lastPrice':data['lastPrice'],
                'lastValue':data['lastValue'],
                'Side':side(data)} }
        
                k=position.update_one(myquery, newvalues)
                print('Updated Position Data')
                #checking=list(position.find({'symbol':'XBTUSD'}))[-1]
                #print(checking)


    else:

        position=db.position
        k=list(position.find({'symbol':'XBTUSD'}).sort("_id", pymongo.DESCENDING).limit(1))
        k=k[0]['_id']
        #print(k)
        myquery = { "_id": k }
        d=False
        newvalues = { "$set": { 'isOpen': d } }
        
        k=position.update_one(myquery, newvalues)
        #print(k.matched_count)
        #print("hi")
        position=db.position
        k=list(position.find({'symbol':'ETHUSD'}).sort("_id", pymongo.DESCENDING).limit(1))
        k=k[0]['_id']
        #print(k)
        myquery = { "_id": k }
        d=False
        newvalues = { "$set": { 'isOpen': d } }
        
        k=position.update_one(myquery, newvalues)




def oldTrade_Management1(exchange):
	data1=exchange.private_get_position({'filter': json.dumps({"isOpen": True})})
	#data=data[0]
	if data1 :
		for data in data1:
			position=db.position
			p=list(position.find({'symbol':data['symbol']}))
			p=p[-1]
			if p['isOpen'] == False:	
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
				'openingTimestamp':data['openingTimestamp'],
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
				'currentTimestamp':data['currentTimestamp'],
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
				'timestamp':data['timestamp'],
				'lastPrice':data['lastPrice'],
				'lastValue':data['lastValue'],
                'Side':side(data)}

				#print(data)

				position=db.position
				position_id=position.insert_one(post).inserted_id
				print(position_id)
			else:
				position=db.position
				k=list(position.find({'symbol':data['symbol']}))
				k=k[-1]['_id']
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
				'openingTimestamp':data['openingTimestamp'],
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
				'currentTimestamp':data['currentTimestamp'],
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
				'timestamp':data['timestamp'],
				'lastPrice':data['lastPrice'],
				'lastValue':data['lastValue'],
                'Side':side(data)} }
		
				k=position.update_one(myquery, newvalues)
				print('Updated Position Data')
				checking=list(position.find({'symbol':'XBTUSD'}))[-1]
				#print(checking)


	else:

		position=db.position
		k=list(position.find({'symbol':'XBTUSD'}))
		k=k[-1]['_id']
		#print(k)
		myquery = { "_id": k }
		d=False
		newvalues = { "$set": { 'isOpen': d } }
		
		k=position.update_one(myquery, newvalues)
		#print(k.matched_count)
		#print("hi")
		position=db.position
		k=list(position.find({'symbol':'ETHUSD'}))
		k=k[-1]['_id']
		#print(k)
		myquery = { "_id": k }
		d=False
		newvalues = { "$set": { 'isOpen': d } }
		
		k=position.update_one(myquery, newvalues)

def convert(e):
	if e == 'buy':
		e='BUY'
		#print(e)
	elif e == 'sell':
		e='SELL'
		#print(e)
	else:
		print('q')
	return e


def DecisionMaker(btcusdt,amount,symbol):
	post1={'type': 'market', 'side': 'buy', 'amount': amount, 'symbol': symbol, 'price': None, 'key': '99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319'}
	post2={'type': 'market', 'side': 'sell', 'amount': amount, 'symbol': symbol, 'price': None, 'key': '99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319'}
	if symbol == 'ETH/USD':
		d='ETHUSD'
	elif symbol == 'BTC/USD':
		d= 'XBTUSD'
	else:
		print(' ENTER A VALID COIN ')
	Trade_Management(exchange)
	check=list(db.position.find({'symbol':d}))
	check=check[-1]['isOpen']
	btctvsignal1=btcusdt['recommendall1']
	btctvsignal5=btcusdt['recommendall5']
	btctvsignal15=btcusdt['recommendall15']
	check=check == False
	if check:
		if btctvsignal1 > 0 and btctvsignal5 > 0 and btctvsignal15 > 0 :
			if today_sentiment() == 'POSITIVE':
				#if convert(e) == 'BUY':
				Decision="Long Entry"
				send_order(post1)
				time.sleep(3)
				Trade_Management(exchange)
			#break
		elif  btctvsignal1 < 0 and btctvsignal5 < 0 and btctvsignal15 < 0 :
			if today_sentiment() == 'POSITIVE':
				#if convert(e) == 'SELL':
				Decision="Short Entry"
				send_order(post2)
				time.sleep(3)
				Trade_Management(exchange)
		else:
			print("NO actions")
		return print('{} {} Entry {}'.format(symbol,post1['type'],Decision))
		
	else:	
		Trade_Management(exchange)
		check=list(db.position.find({'symbol':d}))
		isopen=check[-1]['isOpen']
		check_currentqty=check[-1]['currentQty']
		currentqty=check[-1]['currentQty']
		
		if isopen:
			Decision='NO'
			Trade_Management(exchange)
			if check_currentqty > 0:
				#print('no sell signal yet')
				if btctvsignal1 < 0 and btctvsignal5 < 0 and btctvsignal15 < 0 :
					if today_sentiment() == 'POSITIVE':
						#if convert(e) == 'SELL':
						Decision="Long Exit"
						post2={'type': 'market', 'side': 'sell', 'amount': abs(currentqty), 'symbol': symbol, 'price': None, 'key': '99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319'}
	
						send_order(post2)
						time.sleep(3)
						Trade_Management(exchange)
				#break
			elif check_currentqty < 0:
				if btctvsignal1 > 0 and btctvsignal5 > 0 and btctvsignal15 > 0 :
					if today_sentiment() == 'POSITIVE':
						#if convert(e) == 'BUY':
						Decision="Short Exit"
						post1={'type': 'market', 'side': 'buy', 'amount': abs(currentqty), 'symbol': symbol, 'price': None, 'key': '99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319'}
	
						send_order(post1)
						time.sleep(3)
						Trade_Management(exchange)
			Trade_Management(exchange)
			return print('{} {} {}'.format(symbol,post1['type'],Decision))	
	#time.sleep(5)
	return print('OK')
def Decision():
	btcusdt=list(db.btcusdt.find())[-1]
	ethusdt=list(db.ethusdt.find())[-1]
	DecisionMaker(ethusdt,percentage('ETH/USD',10),'ETH/USD')
	DecisionMaker(btcusdt,percentage('BTC/USD',10),'BTC/USD')


def MultiDecisionMaker(btcusdt,amount,symbol):
    post1={'type': 'market', 'side': 'buy', 'amount': amount, 'symbol': symbol, 'price': None, 'key': '99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319'}
    post2={'type': 'market', 'side': 'sell', 'amount': amount, 'symbol': symbol, 'price': None, 'key': '99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319'}
    if symbol == 'ETH/USD':
        d='ETHUSD'
    elif symbol == 'BTC/USD':
        d= 'XBTUSD'
    else:
        print(' ENTER A VALID COIN ')
    Trade_Management(exchange)
    check=list(db.position.find({'symbol':d}))
    webhook=list(db.order.find({'symbol':symbol}))[-1]
    check=check[-1]['isOpen']
    btctvsignal1=btcusdt['recommendall1']
    btctvsignal5=btcusdt['recommendall5']
    btctvsignal15=btcusdt['recommendall15']
    check=check == False
    db.trading
    Decision="Searching"
    if check:
        if btctvsignal1 > 0 and btctvsignal5 > 0 and btctvsignal15 > 0 :
            if today_sentiment() == 'POSITIVE':
                if webhook['side'] == 'buy' :#and webhook['auto'] == True:
                    post={'date':datetime.datetime.now(),'symbol':symbol,'strategy':webhook['side'],'tradingview1':btctvsignal1,'tradingview5':btctvsignal5,'tradingview15':btctvsignal15}
                    Decision="Long Entry"
                    send_order(post1)
                    post=db.trading.insert_one(post)
                    print(post)
                    time.sleep(3)

                    Trade_Management(exchange)
                #break
        elif  btctvsignal1 < 0 and btctvsignal5 < 0 and btctvsignal15 < 0 :
            if today_sentiment() == 'POSITIVE':
                if webhook['side'] == 'sell' :#and webhook['auto'] == True:
                    Decision="Short Entry"
                    send_order(post2)
                    post={
                    'date':datetime.datetime.now(),'symbol':symbol,'strategy':webhook['side'],'tradingview1':btctvsignal1,'tradingview5':btctvsignal5,'tradingview15':btctvsignal15
                    }
                    post=db.trading.insert_one(post).inserted_id
                    print(post)
                    time.sleep(3)
                    Trade_Management(exchange)
        else:
            print("NO actions")
        return print('{} {} Entry {}'.format(symbol,post1['type'],Decision))
        
    else:   
        Trade_Management(exchange)
        check=list(db.position.find({'symbol':d}))
        isopen=check[-1]['isOpen']
        check_currentqty=check[-1]['currentQty']
        currentqty=check[-1]['currentQty']
        Decision='NO'
        if isopen:
            Decision='NO'
            Trade_Management(exchange)
            if check_currentqty > 0:
                #print('no sell signal yet')
                if btctvsignal1 < 0 and btctvsignal5 < 0 and btctvsignal15 < 0 :
                    if today_sentiment() == 'POSITIVE':
                        if webhook['side'] == 'sell' :#and webhook['auto'] == True:
                            Decision="Long Exit"
                            post2={'type': 'market', 'side': 'sell', 'amount': abs(currentqty), 'symbol': symbol, 'price': None, 'key': '99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319'}
                            send_order(post2)
                            post={'date':datetime.datetime.now(),'symbol':symbol,'strategy':webhook['side'],'tradingview1':btctvsignal1,'tradingview5':btctvsignal5,'tradingview15':btctvsignal15}
                            post1=db.trading.insert_one(post)
                            print(post1)
                            time.sleep(3)
                            Trade_Management(exchange)
                #break
            elif check_currentqty < 0:
                if btctvsignal1 > 0 and btctvsignal5 > 0 and btctvsignal15 > 0 :
                    if today_sentiment() == 'POSITIVE':
                        if webhook['side'] == 'buy':# and webhook['auto'] == True:
                            Decision="Short Exit"
                            post1={'type': 'market', 'side': 'buy', 'amount': abs(currentqty), 'symbol': symbol, 'price': None, 'key': '99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319'}
        					
                            send_order(post1)
                            time.sleep(3)
                            post={'date':datetime.datetime.now(),'symbol':symbol,'strategy':webhook['side'],'tradingview1':btctvsignal1,'tradingview5':btctvsignal5,'tradingview15':btctvsignal15}
                            post1=db.trading.insert_one(post)
                            print(post1)
                            Trade_Management(exchange)
            Trade_Management(exchange)
            return print('{} {} {}'.format(symbol,post1['type'],Decision))  
    #time.sleep(5)
    return print('OK')
def MultiDecision():
	btcusdt=list(db.btcusdt.find())[-1]
	ethusdt=list(db.ethusdt.find())[-1]
	MultiDecisionMaker(ethusdt,percentage('ETH/USD',50),'ETH/USD')
	MultiDecisionMaker(btcusdt,percentage('BTC/USD',50),'BTC/USD')


