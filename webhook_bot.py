"""
Tradingview-webhooks-bot is a python bot that works with tradingview's webhook alerts!
This bot is not affiliated with tradingview and was created by @robswc

You can follow development on github at: github.com/robswc/tradingview-webhook-bot

I'll include as much documentation here and on the repo's wiki!  I
expect to update this as much as possible to add features as they become available!
Until then, if you run into any bugs let me know!
"""
import multiprocessing
from multiprocessing import Process, current_process
from actions import TradinviewSignals,senti,lastpositions
from actions import *
#from sentiment import today_sentiment
from auth import get_token
from request_content import web_data
from flask import Flask, request, abort,jsonify
from flask import render_template
from flask import flash
from generate_alert_message import alert_message
import requests
#from sentiment import sentiment
import datetime
import pymongo
from database import db
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from Trade import Decision,MultiDecision,strategyexecutor
import json
import numpy as np
import plotly
import chart_studio.plotly as py
import plotly.graph_objs as go
from plot import technical_plotter
app = Flask(__name__)
app.secret_key ='Kingisback'

 

cron = BackgroundScheduler()
cron.start()
cron1 = BackgroundScheduler()
cron1.start()



@app.route('/')
def root():
    return 'Online'

@app.route('/index' ,methods=["GET","POST"])
def index():
    btcusdt,ethusdt=TradingView()
    #print(btcusdt,ethusdt)
    options = ['1_Min_ALL','1_Min_MA','1_Min_Osillator','5_Min_ALL','5_Min_MA','5_Min_Osillator','15_Min_ALL','15_Min_MA','15_Min_Osillator','60_Min_ALL','60_Min_MA','60_Min_Osillator','240_Min_ALL','240_Min_MA','240_Min_Osillator','1_Day_ALL','1_Day_MA','1_Day_Osillator','1_Week_ALL','1_Week_MA','1_Week_Osillator','1_Month_ALL','1_Month_MA','1_Month_Osillator','Only Strategy']
    options1=['TradingView','Only Signals','Only Strategy']
    options2=['Percent','Qty']
    options3=['Sentiment Analysis','Only Signals','Only Strategy']
    options4=['GAN Strategy','GAN Volatility Strategy']
    ordertype=['Market','Limit']
    riskmanagement=['None','Trailing Stop','Stop Loss','Take Profit']
    riskmode=['Percent','Qty']
    if request.method == "POST":
        data=request.form
        db1=db.strategy
        post={'date':datetime.datetime.now(),'signal1':data['signal1'],'signal2':data['signal2'],'signal3':data['signal3'],'signal4':data['signal4'],'strategy':data['strategy'],'Strategy':data['Strategy'],'Qty':data['quantity'],'mode':data['mode'],'ordertype':data['ordertype'],'riskmanagement':data['riskmanagement'],'riskquantity':data['riskquantity'],'riskmode':data['riskmode']}
        db2=db1.insert_one(post).inserted_id
        #print(db2)
        #return render_template('index.html',b=btcusdt,e=ethusdt,options=options,options1=options1,options2=options2)
    if 'strategy' in db.list_collection_names():
        currentstrategy=list(db.strategy.find())[-1]
        return render_template('index.html',b=btcusdt,e=ethusdt,options=options,options1=options1,options2=options2,options4=options4,currentstrategy=currentstrategy,options3=options3,ordertype=ordertype,riskmanagement=riskmanagement,riskmode=riskmode)
    return render_template('index.html',b=btcusdt,e=ethusdt,options=options,options1=options1,options2=options2,options3=options3,options4=options4,ordertype=ordertype,riskmanagement=riskmanagement,riskmode=riskmode)

@app.route('/get', methods=["GET","POST"])
def get():
    btcusdt,ethusdt=TradingView()
    btc=lastpositions('BTCUSD')
    eth=lastpositions('ETHUSD')
    #s=today_sentiment()
    l1=lasttrades(1)
    l2=lasttrades(2)
    l3=lasttrades(3)
    l4=lasttrades(4)
    l5=lasttrades(5)
    l6=lasttrades(6)
    l7=lasttrades(7)
    l8=lasttrades(8)
    l9=lasttrades(9)
    l10=lasttrades(10)
    print(l1)
    return jsonify(b=btcusdt,e=ethusdt,btc=btc,eth=eth,l1=l1,l2=l2,l3=l3,l4=l4,l5=l5,l6=l6,l7=l7,l8=l8,l9=l9,l10=l10)#,s=s,)

@app.route('/showLineChart', methods=["GET","POST"])
def line():
    import pandas as pd
    from technical import qtpylib
    tf=['5m','1m','15m','1h','2h','4h','12h','1d','30m']
    symbols=['ETH/USDT','BTC/USDT']
    candle=['Heikinashi','Renko','candle']
    technical,technical_names=listed_technical()
    if 'chart' in db.list_collection_names():
        chart=list(db.chart.find())[-1]
    elif not 'chart' in db.list_collection_names():
        chart={
        'date':datetime.datetime.now(),
        'symbols':'BTC/USDT',
        'candle':'Heikinashi',
        'tf':'1m'
        }
        db.chart.insert_one(chart)
    else:
        print('Error ocurred in chart section')
    syinfo=db.chart.find_one(sort=[('_id', pymongo.DESCENDING)])
    print(syinfo)
    data=Plotcandle(syinfo['symbols'],syinfo['tf'])
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    data1=Plotcandle(syinfo['symbols'],'5m')
    graphJSON1 = json.dumps(data1, cls=plotly.utils.PlotlyJSONEncoder)
    chart=db.chart.find_one(sort=[('_id', pymongo.DESCENDING)])
    if chart:
        indicator=chart['technical']
        graph=[technical_plotter(d) for d in indicator]
        if request.method == "POST":
            data=request.form
            print(data)
            post={
                'date':datetime.datetime.now(),
                'tf':data['tf'],
                'symbols':data['symbols'],
                'candle':data['candle'],
                'technical':data.getlist('technical')
                }

            db.chart.insert_one(post)
            return render_template('index1.html',graphJSON=graphJSON,graphJSON1=graphJSON1,tf=tf,symbols=symbols,candle=candle,technical=technical,graph=graph)
    return render_template('index1.html',graphJSON=graphJSON,graphJSON1=graphJSON1,tf=tf,symbols=symbols,candle=candle,technical=technical,graph=graph)

@app.route('/plot', methods=["GET","POST"])
def line1():
    import pandas as pd
    from technical import qtpylib
    tf=['5m','1m','15m','1h','2h','4h','12h','1d','30m']
    symbols=['ETH/USDT','BTC/USDT']
    candle=['Heikinashi','Renko','candle']
    technical,technical_names=listed_technical()
    if 'chart' in db.list_collection_names():
        chart=list(db.chart.find())[-1]
    elif not 'chart' in db.list_collection_names():
        chart={
        'date':datetime.datetime.now(),
        'symbols':'BTC/USDT',
        'candle':'Heikinashi',
        'tf':'1m'
        }
        db.chart.insert_one(chart)
    else:
        print('Error ocurred in chart section')
    syinfo=db.chart.find_one(sort=[('_id', pymongo.DESCENDING)])
    print(syinfo)
    data=Plotcandle(syinfo['symbols'],syinfo['tf'])
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    data1=Plotcandle(syinfo['symbols'],'5m')
    graphJSON1 = json.dumps(data1, cls=plotly.utils.PlotlyJSONEncoder)
    chart=db.chart.find_one(sort=[('_id', pymongo.DESCENDING)])
    indicator=chart['technical']
    graph=[technical_plotter(d) for d in indicator]
    if request.method == "POST":
        data=request.form
        print(data)
        post={
            'date':datetime.datetime.now(),
            'tf':data['tf'],
            'symbols':data['symbols'],
            'candle':data['candle'],
            'technical':data.getlist('technical')
            }

        db.chart.insert_one(post)
        return render_template('plot.html',graphJSON=graphJSON,graphJSON1=graphJSON1,tf=tf,symbols=symbols,candle=candle,technical=technical,graph=graph)
    return render_template('plot.html',graphJSON=graphJSON,graphJSON1=graphJSON1,tf=tf,symbols=symbols,candle=candle,technical=technical,graph=graph)

@app.route('/webhook', methods=["GET","POST"])
def webhook():
    p=list(db.order.find())
    p1=p[-1]
    p2=p[-2]
    p3=p[-3]
    p4=p[-4]
    p5=p[-5]
    btc=lastpositions('BTCUSD')
    eth=lastpositions('ETHUSD')
    l1=lasttrades(1)
    l2=lasttrades(2)
    l3=lasttrades(3)
    l4=lasttrades(4)
    l5=lasttrades(5)
    l6=lasttrades(6)
    l7=lasttrades(7)
    l8=lasttrades(8)
    l9=lasttrades(9)
    l10=lasttrades(10)
    if request.method == 'POST':
        # Parse the string data from tradingview into a python dict
        web_data(request)      
        return render_template("webhook.html",p1=p1,p2=p2,p3=p3,p4=p4,p5=p5,btc=btc,eth=eth,l1=l1,l2=l2,l3=l3,l4=l4,l5=l5,l6=l6,l7=l7,l8=l8,l9=l9,l10=l10)
    else:
        return render_template("webhook.html",p1=p1,p2=p2,p3=p3,p4=p4,p5=p5,btc=btc,eth=eth,l1=l1,l2=l2,l3=l3,l4=l4,l5=l5,l6=l6,l7=l7,l8=l8,l9=l9,l10=l10)
@app.route('/alerts', methods=["GET","POST"])
def alerts_page():
  
    if request.method == "POST":
        data=request.form
        a=alert_message(data)
        return render_template("alerts.html",a=a) 
    return render_template("alerts.html")      

@app.route('/order', methods=["GET","POST"])
def order_page():
  
    if request.method == "POST":
        data=request.form
        a=alert_message(data)
        if a:
            a=send_order(a)
            return render_template("order.html",a=a) 
        #r = requests.post('http://127.0.0.1:5000/webhook',a)

    return render_template("order.html") 


@app.route('/balance', methods=["GET","POST"])
def balance_page():
    info =balance()
    bal={"date":datetime.datetime.utcnow(),"prevrealisedpnl":info[0]['prevRealisedPnl'],"RealisedPnl":info[0]['realisedPnl'],"UnrealisedPnl":info[0]['unrealisedPnl'],"MarginBalance":info[0]['marginBalance'],"Free":info[1]['free'],"Used":info[1]['used'],"Total":info[1]['total'],}
    print(bal)
    balance1=db.balance
    p=db.balance.find_one(sort=[('_id', pymongo.DESCENDING)])
    #print(p)
    if p['Free'] !=bal['Free']:
        balance2=balance1.insert_one(bal).inserted_id
        print(balance2)
    
    print(p)
    return render_template("balance.html",info=info) 
@app.route('/account', methods=['GET','POST'])
def account():
    account=db.account
    if request.method == 'POST':
        data=request.form
        post={
        'date':datetime.datetime.now(),'name':data['name'],'apikey':data['apikey'],'apisecret':data['apisecret']
        }
        account=account.insert_one(post).inserted_id
        print(account)

    return render_template("account.html") 

@cron1.scheduled_job('interval', minutes=1)
def interval5():
    historicaldatamanager()
    print('Interval Based Task Completed 2')
    return True
@cron.scheduled_job('interval', minutes=1)
def interval():
    #TradinviewSignals()
    #sentiment()
    #Decision()
    #MultiDecision()
    #historicaldatamanager()
    strategyexecutor()
    print('Interval Based Task Completed')
    return True


if __name__ == '__main__':
    app.run(debug=True)