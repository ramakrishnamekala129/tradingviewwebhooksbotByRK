from actions import TradinviewSignals,senti
from actions import send_order, parse_webhook,balance,TradingView
from sentiment import today_sentiment
from auth import get_token
import datetime
from database import db
def web_data(request):
    data = parse_webhook(request.get_data(as_text=True))
    # Check that the key is correct
    
    if get_token() == data['key']:
        print(' [Alert Received] ')
        print('POST Received:', data)
        if data['auto'] == False:
            send_order(data)
        
        post={"date":datetime.datetime.utcnow(),"type":data['type'],
                    "side":data['side']
                        ,"amount":data['amount'],
                        "symbol":data['symbol'],
                        "price":data['price'],
                        "key":data['key'],
                        "auto":data["auto"]}
                        
        data1=db.order
        data2=data1.insert_one(post).inserted_id

        print(data2)
        #data=list(db.order.find({'symbol':'BTC/USD'}))
        #data=data[-1]
        if data['symbol']=='BTC/USD':
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
            data1=db.combinedbtc

            data2=data1.insert_one(post).inserted_id
            print(data2)
            if data['symbol']=='ETH/USD':

                btcusdt,p=TradingView()
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
                data1=db.combinedeth

                data2=data1.insert_one(post).inserted_id
                print(data2)