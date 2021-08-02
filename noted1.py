from database import db
from datetime import datetime
print("balance" in db.list_collection_names())   
import dateutil
import os
import sys
import time
import pandas as pd
from pandas import ExcelWriter
from database import db
import pymongo
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

import ccxt  # noqa: E402
import json


msec = 1000
minute = 60 * msec
hold = 30
#datetime.utcfromtimestamp(timestamp)
exchange = ccxt.binance({
    'rateLimit': 10000,
    'enableRateLimit': True,
    # 'verbose': True,
})
def lasttimestoredata(dba,data,tf):
    try:
    	if not dba in db.list_collection_names():
	    	from_timestamp=data
	    	print('not in data')
	    	return data
    	if dba in db.list_collection_names():
	        #from_timestamp=list(db[dba].find().sort("date", pymongo.DESCENDING).limit(10))[1]['Timestamp']
	        from_timestamp1=db[dba].find_one(sort=[('_id', pymongo.DESCENDING)])['date']
	        from_timestamp2=dateutil.parser.parse(from_timestamp1).timestamp()#exchange.parse8601(from_timestamp1)
	        from_timestamp=from_timestamp2+delaytimeframe(tf)
	        print(from_timestamp,from_timestamp1)
	        print('not in data1')
	        return from_timestamp
    except:
	        print('Error During Historic data')
	        return data
	#return data
def delaytimeframe(tf):
	if tf == '1m':
		tf=60*1000
	elif tf == '5m':
		tf=60*5*1000
	return tf
def run(symbol,dba,timeframe):
    from database import db
    from_datetime = '2018-01-01 00:00:00'
    timestamp = exchange.parse8601(from_datetime)
    data = []
    now = exchange.milliseconds()
    #db[dba]
    from_timestamp=lasttimestoredata(dba,timestamp,timeframe)

        #print("i")

    while from_timestamp < now:
        writer = db[dba]
        try:
            print(from_timestamp)
            print(exchange.milliseconds(), 'Fetching candles starting from', exchange.iso8601(from_timestamp), from_timestamp)
            candles = exchange.fetch_ohlcv(symbol, timeframe, from_timestamp)
            print(from_timestamp)
            #print(candles, from_timestamp)
            
            if candles:     
                print(exchange.milliseconds(), 'Fetched', len(candles), 'candles')
                first = candles[0][0]
                last = candles[-1][0]
                print('First candle epoch', first, exchange.iso8601(first))
                print('Last candle epoch', last, exchange.iso8601(last))
                from_timestamp = candles[-1][0] + minute
                data += candles


                df = pd.DataFrame(data, columns=['Timestamp','Open','High','Low','Close', 'Volume'])
                df['Timestamp'] =pd.DataFrame(df['Timestamp'].apply(exchange.iso8601))
                #df.drop(['Timestamp'],axis=1)
                records = json.loads(df.T.to_json()).values()
                #db[dba].create_index([('Timestamp',pymongo.ASCENDING)],unique=True)
                for record in records:
                	print(record['Timestamp'])
                	post={
                	'Timestamp':record['Timestamp'],
                	'date':dateutil.parser.isoparse(record['Timestamp']),
                	'Open':record['Open'],
                	'High':record['High'],
                	'Low':record['Low'],
                	'Close':record['Close'],
                	'Volume':record['Volume']
                	}
                	save_excel = db[dba].insert_one(post)
                	print(save_excel)
    			#from_timestamp=from_timestamp+delaytimeframe(tf)
                print('{} {} candles saved'.format(symbol,timeframe))
            elif not candles:
                break
        except (ccxt.ExchangeError, ccxt.AuthenticationError, ccxt.ExchangeNotAvailable, ccxt.RequestTimeout) as error:

            print('Got an error', type(error).__name__, error.args, ', retrying in', hold, 'seconds...')
            time.sleep(hold)
if __name__ == "__main__":
    timeframe=['1d','30m','12h','15m','2h','4h','1h']#,'1m','5m']
    symbols=['ETH/USDT','BTC/USDT']
    for tf in timeframe:
        print(tf)
        for symbol in symbols:
            print(symbol)
            run(symbol,'{}{}'.format(symbol,tf).replace('/',''),tf)      
    #run('BTC/USD','btcusdmin1','1m')

#dateutil.parser.parse(record['Timestamp'])
'''try:
	for record in records:
		try:
			save_excel = db[dba].insert_one(record)
        except pymongo.errors.DuplicateKeyError as e:
        	return e
except pymongo.errors.DuplicateKeyError as e:
	return e
'''
#writer.save()















'''from database import db
import pandas as pd
from technical import qtpylib
e=list(db.btcusdt.find())[-500:]
df=pd.DataFrame(e)
#df['date'] = pd.to_datetime(df['date'])
h=qtpylib.heikinashi(df)
df['ha_open']=h['open']
df['ha_high']=h['high']
df['ha_low']=h['low']
df['ha_close']=h['close']
df['date'] = pd.to_datetime(df["date"], format="%m/%d/%Y").dt.round("min")

df['date']=df['date'].drop_duplicates(keep='last')
df=df.dropna()

#df=df.append(h)



print(df)


'''

'''from actions import TradingView
from database import db 
d=list(db.btcusdt.find())
import pandas as pd
d=pd.DataFrame(d)
d.to_csv('r.csv')
'''

'''
import ccxt
import json
exchange = ccxt.bitmex({
# Inset your API key and secrets for exchange in question.
'apiKey': 'kYYW-m1v7wESbEWkiUKi9sSz',
'secret': 'YUpGzV9OeflUpxwkTbGabXpS-z1_rf1jIXtuw0BeM6Q8N95B',
'enableRateLimit': True,
})


orders = exchange.fetch_closed_orders()
print(orders[0])
with open("data_file.json", "w") as write_file:
    json.dump(orders, write_file)'''
'''
import pymongo
from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client.test_database
collection=db.test_collection
import datetime
post={"date":datetime.datetime.utcnow(),"type": "limit", "side": "sell", "amount": "1000", "symbol": "XBT/USD", "price": "6300", "key": "99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319"}
posts=db.posts
post_id=posts.insert_one(post).inserted_id
print(post_id)
import json
import requests
url="https://scanner.tradingview.com/crypto/scan"
s='{"symbols":{"tickers":["BINANCE:BTCUSDT","BINANCE:ETHUSDT"],"query":{"types":[]}},"columns":["Recommend.Other|1","Recommend.All|1","Recommend.MA|1","Recommend.Other|5","Recommend.All|5","Recommend.MA|5","Recommend.Other|15","Recommend.All|15","Recommend.MA|15","Recommend.Other|60","Recommend.All|60","Recommend.MA|60","Recommend.Other|120","Recommend.All|120","Recommend.MA|120","Recommend.Other|240","Recommend.All|240","Recommend.MA|240","Recommend.Other","Recommend.All","Recommend.MA","Recommend.Other|1W","Recommend.All|1W","Recommend.MA|1W","Recommend.Other|1M","Recommend.All|1M","Recommend.MA|1M"]}'
u=requests.post(url,s).json()
for i in range(0,len(u)):
	print(u['data'][i]['s'].replace("BINANCE:","").lower())
'''
#Tradinview()
#print(u)

'''d=["Recommend.Other|1","Recommend.All|1","Recommend.MA|1","Recommend.Other|5","Recommend.All|5","Recommend.MA|5","Recommend.Other|15","Recommend.All|15","Recommend.MA|15","Recommend.Other|60","Recommend.All|60","Recommend.MA|60","Recommend.Other|120","Recommend.All|120","Recommend.MA|120","Recommend.Other|240","Recommend.All|240","Recommend.MA|240","Recommend.Other","Recommend.All","Recommend.MA","Recommend.Other|1W","Recommend.All|1W","Recommend.MA|1W","Recommend.Other|1M","Recommend.All|1M","Recommend.MA|1M"]
#print(len(d))
for r in range(0,27):
	t=d[r]
	print(("'{}':u['data'][i]['d'][{}],".format(t,r)).replace(".","").replace("|","").lower())
'''
'''d=["Recommend.Other|1","Recommend.All|1","Recommend.MA|1","Recommend.Other|5","Recommend.All|5","Recommend.MA|5","Recommend.Other|15","Recommend.All|15","Recommend.MA|15","Recommend.Other|60","Recommend.All|60","Recommend.MA|60","Recommend.Other|120","Recommend.All|120","Recommend.MA|120","Recommend.Other|240","Recommend.All|240","Recommend.MA|240","Recommend.Other","Recommend.All","Recommend.MA","Recommend.Other|1W","Recommend.All|1W","Recommend.MA|1W","Recommend.Other|1M","Recommend.All|1M","Recommend.MA|1M"]

for r in range(0,27):
	#t=d[r].replace(".","").replace("|","").lower()
	#btcusdt="btcusdt"
	k="<th scope=""col"">{}</th>".format(d[r])
	#k=("<td>{{ ['{}'] }}</td>").format(t)
	print(k)
'''
'''
TradinviewSignal=Tradinview()
import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler


def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
    return print("hi")


scheduler = BackgroundScheduler()
scheduler.add_job(func=Tradinview, trigger="interval", seconds=35)
scheduler.start()

# Shut down the scheduler when exiting the app
#atexit.register(lambda: scheduler.shutdown())'''
#import datetime 
#print(datetime.datetime())
'''import threading.Timer as t

def myApiCall():
	print("hi")# your request lib here making an http call ...
    # call myApi() again in 600 seconds/10min
threading.Timer(600, myApiCall).start()
'''

'''
from database import db 
p=list(db.btcusdt.find())
#print(p)
p=p[-1]
print(p)
#for i,j in p.items():
#	print("'{}':(p['{}'])".format(i,i))
def (signal):
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
print((-0.9))

p={
'date':(p['date']),
'symbol':(p['symbol']),
'recommendother1':(p['recommendother1']),
'recommendall1':(p['recommendall1']),
'recommendma1':(p['recommendma1']),
'recommendother5':(p['recommendother5']),
'recommendall5':(p['recommendall5']),
'recommendma5':(p['recommendma5']),
'recommendother15':(p['recommendother15']),
'recommendall15':(p['recommendall15']),
'recommendma15':(p['recommendma15']),
'recommendother60':(p['recommendother60']),
'recommendall60':(p['recommendall60']),
'recommendma60':(p['recommendma60']),
'recommendother240':(p['recommendother240']),
'recommendall240':(p['recommendall240']),
'recommendma240':(p['recommendma240']),
'recommendother':(p['recommendother']),
'recommendall':(p['recommendall']),
'recommendma':(p['recommendma']),
'recommendother1w':(p['recommendother1w']),
'recommendall1w':(p['recommendall1w']),
'recommendma1w':(p['recommendma1w']),
'recommendother1m':(p['recommendother1m']),
'recommendall1m':(p['recommendall1m']),
'recommendma1m':(p['recommendma1m'])

}
print(p)
'''
from database import db 
#p=list(db.btcusdt.find())
#print(p)
'''p=p[-1]
print(p)
for i,j in p.items():
#	print("'{}':(p['{}'])".format(i,i))
	print("$('#e_{}').text(data.e.{});,".format(i,i))
'''
'''
data=list(db.order.find({'symbol':'BTC/USD'}))
data=data[-1]
p,ethusdt=TradingView()
post = {
        'date':(p['date']),
        'symbol':(p['symbol']),
        'close':(p['close']),
        'type':data['type'],
        "side":data['side']
        ,"amount":data['amount'],
        "symbol":data['symbol'],
        "price":data['price'],
        "key":data['key'],
        'recommendother1':(p['recommendother1']),
        'recommendall1':(p['recommendall1']),
        'recommendma1':(p['recommendma1']),
        'recommendother5':(p['recommendother5']),
        'recommendall5':(p['recommendall5']),
        'recommendma5':(p['recommendma5']),
        'recommendother15':(p['recommendother15']),
        'recommendall15':(p['recommendall15']),
        'recommendma15':(p['recommendma15']),
        'recommendother60':(p['recommendother60']),
        'recommendall60':(p['recommendall60']),
        'recommendma60':(p['recommendma60']),
        'recommendother240':(p['recommendother240']),
        'recommendall240':(p['recommendall240']),
        'recommendma240':(p['recommendma240']),
        'recommendother':(p['recommendother']),
        'recommendall':(p['recommendall']),
        'recommendma':(p['recommendma']),
        'recommendother1w':(p['recommendother1w']),
        'recommendall1w':(p['recommendall1w']),
        'recommendma1w':(p['recommendma1w']),
        'recommendother1m':(p['recommendother1m']),
        'recommendall1m':(p['recommendall1m']),
        'recommendma1m':(p['recommendma1m'])

        }
data1=db.combined

data2=data1.insert_one(post).inserted_id
print(data2)
'''
'''from pprint import pprint

import json
def get_news():
	import requests as r
	url="https://news-headlines.tradingview.com/headlines/yahoo/?category=bitcoin&locale=en&proSymbol=BITTREX%3ABTCUSDT"
	d=r.get(url)
	d=d.json()
	return d
#print(d[-1]['shortDescription'])
p=get_news()

#results = []
from pprint import pprint
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
sia = SIA()

#for line in d:
def sentiment_analysis(line):
	pol_score = sia.polarity_scores(line['title'])
	#pol_score['headline'] = line['title']
	pol_score['id']=line['id']
	pol_score['shortDescription']=line['shortDescription']
	pol_score['source']=line['source']
	pol_score['published']=line['published']
	pol_score['link']=line['link']
	pol_score['headline'] = line['title']
	#results.append(line)
	#results.append(pol_score)
	return pol_score


'''

'''for i in p[0:3] :
	post=sentiment_analysis(i)
	h=dict(db.news.find({'headline':post['headline']}))

	print(h)'''
'''def sentiment():
	for i in p:
		post=sentiment_analysis(i)
		h=db.news.find_one({'headline':post['headline']})
		if h != None:
			if h['headline'] != post['headline']:
				q=db.news
				q=q.insert_one(post).inserted_id
				print(q)
		else:
			q=db.news
			q=q.insert_one(post).inserted_id
			print(q)




print(r)

'''

'''
from actions import TradingView
from pprint import pprint
import json
import ccxt 
from actions import balance
import datetime


exchange = ccxt.bitmex({
# Inset your API key and secrets for exchange in question.
'apiKey': 'kYYW-m1v7wESbEWkiUKi9sSz',
'secret': 'YUpGzV9OeflUpxwkTbGabXpS-z1_rf1jIXtuw0BeM6Q8N95B',
'enableRateLimit': True,
})
#"symbol": ['XBTUSD','ETHUSD']'''
'''pprint(exchange.private_get_position({
        'filter': json.dumps({
            "isOpen": True,
            
        })
    }))'''
'''
from actions import percentage
print(percentage('ETH/USD',200))









symbol = 'BTC/USD' 
types = 'Market'  
side = 'buy'  
amount = 100.0     # this is the number of contract you'll buy, in the BTC/USD pair it's the USD amount I think? 
price =  None

# set up leverage level:
lev = 2  # 50x leverage
#exchange.private_post_position_leverage({"symbol": "XBTUSD", "leverage": str(lev)})
# now you should be able to buy maximum amt*lev contracts.


#order = exchange.create_order(symbol, types, side, amount, price)
#print(order)

def Trade_Management(exchange):
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
				'lastValue':data['lastValue']}

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
				'lastValue':data['lastValue']} }
		
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
		#print(k.matched_count)
		#print("hi")
	#print()
#Trade_Management(exchange)
#print(exchange.fetch_closed_orders())


btctvsignal,ethtvsignal=TradingView()
print(btctvsignal['recommendall1'] )
from sentiment import today_sentiment
e=list(db.order.find())[-1]['side']
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



from actions import signals

order=list(db.order.find())
btcusdt=signals(list(db.btcusdt.find())[-1]['recommendall1'])
ethusdt=list(db.ethusdt.find())

import numpy as np
import pandas as pd
order=pd.DataFrame(order)
pprint(order)

import time

#check=list(db.position.find())
#check=check[-1]['isOpen']


from actions import send_order

#post1={'type': 'market', 'side': 'buy', 'amount': 10, 'symbol': 'BTC/USD', 'price': None, 'key': '99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319'}
#post2={'type': 'market', 'side': 'sell', 'amount': 10, 'symbol': 'BTC/USD', 'price': None, 'key': '99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319'}

#while True:
btcusdt=signals(list(db.btcusdt.find())[-1]['recommendall1'])
ethusdt=signals(list(db.ethusdt.find())[-1]['recommendall1'])

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
	btctvsignal=btcusdt#['recommendall5']
	check=check == False
	if check:
		if btctvsignal == 'BUY':
			if today_sentiment() == 'POSITIVE':
				#if convert(e) == 'BUY':
				Decision="BUY1"
				send_order(post1)
				Trade_Management(exchange)
			#break
		elif btctvsignal == 'SELL':
			if today_sentiment() == 'POSITIVE':
				#if convert(e) == 'SELL':
				Decision="SELL1"
				send_order(post2)
				Trade_Management(exchange)
			#break
		elif btctvsignal == 'STRONG BUY':
			if today_sentiment() == 'POSITIVE':
				#if convert(e) == 'BUY':
				Decision="STRONG BUY1"
				send_order(post1)
				Trade_Management(exchange)
			#break
		elif btctvsignal == 'STRONG SELL':
			if today_sentiment() == 'POSITIVE':
				#if convert(e) == 'SELL':
				Decision="STRONG SELL1"
				send_order(post2)
				Trade_Management(exchange)
			#break
		elif btctvsignal == 'NEUTRAL' :
			if today_sentiment() ==  'NEGATIVE' or 'POSITIVE' or 'NEUTRAL':
				#if convert(e) == 'NEUTRAL':
				Decision="NEUTRAL1"
				Trade_Management(exchange)
			#break
		else:
			print("NO actions")
		return print('{} {} Entry {}'.format(symbol,post1['type'],Decision))
		
	else:	
		Trade_Management(exchange)
		check=list(db.position.find())
		check_open=check[-1]['isOpen']
		check_symbol=check[-1]['symbol']
		isopen=check[-1]['isOpen']
		btctvsignal=btcusdt
		check_currentqty=check[-1]['currentQty']
		currentqty=check[-1]['currentQty']
		isopen =isopen == True
		if isopen:
			Decision='NO'
			if check_currentqty > 0:
				#print('no sell signal yet')
				if btctvsignal == 'SELL':
					if today_sentiment() == 'SELL' or 'BUY' or 'NEUTRAL':
						#if convert(e) == 'SELL':
						Decision="SELL"
						post2={'type': 'market', 'side': 'sell', 'amount': currentqty, 'symbol': symbol, 'price': None, 'key': '99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319'}
	
						send_order(post2)
						Trade_Management(exchange)
				#break
				elif btctvsignal == 'STRONG SELL':
					if today_sentiment() == 'SELL' or 'BUY' or 'NEUTRAL':
						#if convert(e) == 'SELL':
						Decision="SELL"
						post2={'type': 'market', 'side': 'sell', 'amount': currentqty, 'symbol': symbol, 'price': None, 'key': '99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319'}
	
						send_order(post2)
						Trade_Management(exchange)
				#break
			elif check_currentqty < 0 :
				if btctvsignal =='BUY':
					if today_sentiment() == 'BUY':
						#if convert(e) == 'BUY':
						Decision="BUY"
						post1={'type': 'market', 'side': 'buy', 'amount': currentqty, 'symbol': symbol, 'price': None, 'key': '99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319'}
	
						send_order(post1)
						Trade_Management(exchange)

				if btctvsignal =='STRONG BUY':
					if today_sentiment() == 'BUY':
						#if convert(e) == 'BUY':
						Decision="BUY"
						post1={'type': 'market', 'side': 'buy', 'amount': currentqty, 'symbol': symbol, 'price': None, 'key': '99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319'}
	
						send_order(post1)
						Trade_Management(exchange)
			return print('{} {} Exit {}'.format(symbol,post1['type'],Decision))
				#break
	
	#time.sleep(5)
	return print('OK')
while True:
	DecisionMaker(ethusdt,percentage('ETH/USD',100),'ETH/USD')
	DecisionMaker(btcusdt,percentage('BTC/USD',100),'BTC/USD')
	time.sleep(5)	


#print(r)


'''





'''
Exchange_Responsebuyopen= {'info': {'orderID': '545ee072-6bad-7949-588d-6e73216b9061', 'clOrdID': '', 'clOrdLinkID': '', 'account': 179347, 'symbol': 'XBTUSD', 'side': 'Buy', 'simpleOrderQty': None, 'orderQty': 1, 'price': 6720.5, 'displayQty': None, 'stopPx': None, 'pegOffsetValue': None, 'pegPriceType': '', 'currency': 'USD', 'settlCurrency': 'XBt', 'ordType': 'Market', 'timeInForce': 'ImmediateOrCancel', 'execInst': '', 'contingencyType': '', 'exDestination': 'XBME', 'ordStatus': 'Filled', 'triggered': '', 'workingIndicator': False, 'ordRejReason': '', 'simpleLeavesQty': None, 'leavesQty': 0, 'simpleCumQty': None, 'cumQty': 1, 'avgPx': 6720.5, 'multiLegReportingType': 'SingleSecurity', 'text': 'Submitted via API.', 'transactTime': '2020-04-04T04:12:55.769Z', 'timestamp': '2020-04-04T04:12:55.769Z'}, 'id': '545ee072-6bad-7949-588d-6e73216b9061', 'timestamp': 1585973575769, 'datetime': '2020-04-04T04:12:55.769Z', 'lastTradeTimestamp': 1585973575769, 'symbol': 'BTC/USD', 'type': 'market', 'side': 'buy', 'price': 6720.5, 'amount': 1.0, 'cost': 6720.5, 'average': 6720.5, 'filled': 1.0, 'remaining': 0.0, 'status': 'closed', 'fee': None}
Exchange_Responsebuyclosed= {'info': {'orderID': '7fc4dbb1-4537-6450-8859-589dae397136', 'clOrdID': '', 'clOrdLinkID': '', 'account': 179347, 'symbol': 'XBTUSD', 'side': 'Sell', 'simpleOrderQty': None, 'orderQty': 1, 'price': 6721.5, 'displayQty': None, 'stopPx': None, 'pegOffsetValue': None, 'pegPriceType': '', 'currency': 'USD', 'settlCurrency': 'XBt', 'ordType': 'Market', 'timeInForce': 'ImmediateOrCancel', 'execInst': '', 'contingencyType': '', 'exDestination': 'XBME', 'ordStatus': 'Filled', 'triggered': '', 'workingIndicator': False, 'ordRejReason': '', 'simpleLeavesQty': None, 'leavesQty': 0, 'simpleCumQty': None, 'cumQty': 1, 'avgPx': 6721.5, 'multiLegReportingType': 'SingleSecurity', 'text': 'Submitted via API.', 'transactTime': '2020-04-04T04:15:42.680Z', 'timestamp': '2020-04-04T04:15:42.680Z'}, 'id': '7fc4dbb1-4537-6450-8859-589dae397136', 'timestamp': 1585973742680, 'datetime': '2020-04-04T04:15:42.680Z', 'lastTradeTimestamp': 1585973742680, 'symbol': 'BTC/USD', 'type': 'market', 'side': 'sell', 'price': 6721.5, 'amount': 1.0, 'cost': 6721.5, 'average': 6721.5, 'filled': 1.0, 'remaining': 0.0, 'status': 'closed', 'fee': None}
Exchange_Responsesell= {'info': {'orderID': '23115308-fb30-ae51-25f5-106503c7a3a1', 'clOrdID': '', 'clOrdLinkID': '', 'account': 179347, 'symbol': 'XBTUSD', 'side': 'Sell', 'simpleOrderQty': None, 'orderQty': 1, 'price': 6723.5, 'displayQty': None, 'stopPx': None, 'pegOffsetValue': None, 'pegPriceType': '', 'currency': 'USD', 'settlCurrency': 'XBt', 'ordType': 'Market', 'timeInForce': 'ImmediateOrCancel', 'execInst': '', 'contingencyType': '', 'exDestination': 'XBME', 'ordStatus': 'Filled', 'triggered': '', 'workingIndicator': False, 'ordRejReason': '', 'simpleLeavesQty': None, 'leavesQty': 0, 'simpleCumQty': None, 'cumQty': 1, 'avgPx': 6723.5, 'multiLegReportingType': 'SingleSecurity', 'text': 'Submitted via API.', 'transactTime': '2020-04-04T04:17:18.595Z', 'timestamp': '2020-04-04T04:17:18.595Z'}, 'id': '23115308-fb30-ae51-25f5-106503c7a3a1', 'timestamp': 1585973838595, 'datetime': '2020-04-04T04:17:18.595Z', 'lastTradeTimestamp': 1585973838595, 'symbol': 'BTC/USD', 'type': 'market', 'side': 'sell', 'price': 6723.5, 'amount': 1.0, 'cost': 6723.5, 'average': 6723.5, 'filled': 1.0, 'remaining': 0.0, 'status': 'closed', 'fee': None}
Exchange_Responsesellclosed {'info': {'orderID': 'f5ced3cb-5cb6-8bca-975d-fdb546bb0667', 'clOrdID': '', 'clOrdLinkID': '', 'account': 179347, 'symbol': 'XBTUSD', 'side': 'Buy', 'simpleOrderQty': None, 'orderQty': 1, 'price': 6739, 'displayQty': None, 'stopPx': None, 'pegOffsetValue': None, 'pegPriceType': '', 'currency': 'USD', 'settlCurrency': 'XBt', 'ordType': 'Market', 'timeInForce': 'ImmediateOrCancel', 'execInst': '', 'contingencyType': '', 'exDestination': 'XBME', 'ordStatus': 'Filled', 'triggered': '', 'workingIndicator': False, 'ordRejReason': '', 'simpleLeavesQty': None, 'leavesQty': 0, 'simpleCumQty': None, 'cumQty': 1, 'avgPx': 6739, 'multiLegReportingType': 'SingleSecurity', 'text': 'Submitted via API.', 'transactTime': '2020-04-04T04:19:09.965Z', 'timestamp': '2020-04-04T04:19:09.965Z'}, 'id': 'f5ced3cb-5cb6-8bca-975d-fdb546bb0667', 'timestamp': 1585973949965, 'datetime': '2020-04-04T04:19:09.965Z', 'lastTradeTimestamp': 1585973949965, 'symbol': 'BTC/USD', 'type': 'market', 'side': 'buy', 'price': 6739.0, 'amount': 1.0, 'cost': 6739.0, 'average': 6739.0, 'filled': 1.0, 'remaining': 0.0, 'status': 'closed', 'fee': None}
'''


'''
[{'account': 179347,
  'avgCostPrice': 6741,
  'avgEntryPrice': 6741,
  'bankruptPrice': 4,
  'breakEvenPrice': 6746,
  'commission': 0.00075,
  'crossMargin': True,
  'currency': 'XBt',
  'currentComm': 369570,
  'currentCost': -10482780,
  'currentQty': 1,
  'currentTimestamp': '2020-04-04T05:10:25.372Z',
  'deleveragePercentile': None,
  'execBuyCost': 14835,
  'execBuyQty': 1,
  'execComm': 11,
  'execCost': -14835,
  'execQty': 1,
  'execSellCost': 0,
  'execSellQty': 0,
  'foreignNotional': -1,
  'grossExecCost': 14835,
  'grossOpenCost': 0,
  'grossOpenPremium': 0,
  'homeNotional': 0.00014861,
  'indicativeTax': 0,
  'indicativeTaxRate': None,
  'initMargin': 0,
  'initMarginReq': 0.01,
  'isOpen': True,
  'lastPrice': 6729.06,
  'lastValue': -14861,
  'leverage': 100,
  'liquidationPrice': 4,
  'longBankrupt': 0,
  'maintMargin': 161,
  'maintMarginReq': 0.005,
  'marginCallPrice': 4,
  'markPrice': 6729.06,
  'markValue': -14861,
  'openOrderBuyCost': 0,
  'openOrderBuyPremium': 0,
  'openOrderBuyQty': 0,
  'openOrderSellCost': 0,
  'openOrderSellPremium': 0,
  'openOrderSellQty': 0,
  'openingComm': 369559,
  'openingCost': -10467945,
  'openingQty': 0,
  'openingTimestamp': '2020-04-04T05:00:00.000Z',
  'posAllowance': 0,
  'posComm': 12,
  'posCost': -14835,
  'posCost2': -14835,
  'posCross': 26,
  'posInit': 149,
  'posLoss': 0,
  'posMaint': 88,
  'posMargin': 187,
  'posState': '',
  'prevClosePrice': 7016.65,
  'prevRealisedPnl': -25,
  'prevUnrealisedPnl': 0,
  'quoteCurrency': 'USD',
  'realisedCost': -10467945,
  'realisedGrossPnl': 10467945,
  'realisedPnl': 10098375,
  'realisedTax': 0,
  'rebalancedPnl': -10098386,
  'riskLimit': 20000000000,
  'riskValue': 14861,
  'sessionMargin': 0,
  'shortBankrupt': 0,
  'simpleCost': None,
  'simplePnl': None,
  'simplePnlPcnt': None,
  'simpleQty': None,
  'simpleValue': None,
  'symbol': 'XBTUSD',
  'targetExcessMargin': 0,
  'taxBase': 0,
  'taxableMargin': 0,
  'timestamp': '2020-04-04T05:10:25.372Z',
  'underlying': 'XBT',
  'unrealisedCost': -14835,
  'unrealisedGrossPnl': -26,
  'unrealisedPnl': -26,
  'unrealisedPnlPcnt': -0.0018,
  'unrealisedRoePcnt': -0.1753,
  'unrealisedTax': 0,
  'varMargin': 0},
 {'account': 179347,
  'avgCostPrice': 0.02091,
  'avgEntryPrice': 0.02091,
  'bankruptPrice': 0,
  'breakEvenPrice': 0.02093,
  'commission': 0.00075,
  'crossMargin': True,
  'currency': 'XBt',
  'currentComm': 7836,
  'currentCost': 2107000,
  'currentQty': 1,
  'currentTimestamp': '2020-04-04T05:09:47.396Z',
  'deleveragePercentile': None,
  'execBuyCost': 2091000,
  'execBuyQty': 1,
  'execComm': 1568,
  'execCost': 2091000,
  'execQty': 1,
  'execSellCost': 0,
  'execSellQty': 0,
  'foreignNotional': -0.02089,
  'grossExecCost': 2091000,
  'grossOpenCost': 0,
  'grossOpenPremium': 0,
  'homeNotional': 1,
  'indicativeTax': 0,
  'indicativeTaxRate': None,
  'initMargin': 0,
  'initMarginReq': 0.02,
  'isOpen': True,
  'lastPrice': 0.02089,
  'lastValue': 2089000,
  'leverage': 50,
  'liquidationPrice': 0,
  'longBankrupt': 0,
  'maintMargin': 41420,
  'maintMarginReq': 0.01,
  'marginCallPrice': 0,
  'markPrice': 0.02089,
  'markValue': 2089000,
  'openOrderBuyCost': 0,
  'openOrderBuyPremium': 0,
  'openOrderBuyQty': 0,
  'openOrderSellCost': 0,
  'openOrderSellPremium': 0,
  'openOrderSellQty': 0,
  'openingComm': 6268,
  'openingCost': 16000,
  'openingQty': 0,
  'openingTimestamp': '2020-04-04T05:00:00.000Z',
  'posAllowance': 0,
  'posComm': 1600,
  'posCost': 2091000,
  'posCost2': 2091000,
  'posCross': 0,
  'posInit': 41820,
  'posLoss': 0,
  'posMaint': 22510,
  'posMargin': 43420,
  'posState': '',
  'prevClosePrice': 0.02086,
  'prevRealisedPnl': -7133,
  'prevUnrealisedPnl': 0,
  'quoteCurrency': 'XBT',
  'realisedCost': 16000,
  'realisedGrossPnl': -16000,
  'realisedPnl': -23836,
  'realisedTax': 0,
  'rebalancedPnl': 22268,
  'riskLimit': 5000000000,
  'riskValue': 2089000,
  'sessionMargin': 0,
  'shortBankrupt': 0,
  'simpleCost': None,
  'simplePnl': None,
  'simplePnlPcnt': None,
  'simpleQty': None,
  'simpleValue': None,
  'symbol': 'ETHXBT',
  'targetExcessMargin': 0,
  'taxBase': 0,
  'taxableMargin': 0,
  'timestamp': '2020-04-04T05:09:47.396Z',
  'underlying': 'ETH',
  'unrealisedCost': 2091000,
  'unrealisedGrossPnl': -2000,
  'unrealisedPnl': -2000,
  'unrealisedPnlPcnt': -0.001,
  'unrealisedRoePcnt': -0.0478,
  'unrealisedTax': 0,
  'varMargin': 0}]
  '''
