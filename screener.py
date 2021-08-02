# -*- coding: utf-8 -*-
"""
Zerodha Kite Connect - candlestick pattern scanner

@author: Mayank Rasu (http://rasuquant.com/wp/)
"""

from kiteconnect import KiteConnect
import pandas as pd
import datetime as dt
import os
import time
import numpy as np
from technicalta import *
#cwd = os.chdir("D:\\Udemy\\Zerodha KiteConnect API\\1_account_authorization")
apikey = 'CE47FSDOCGW6CPBE'
#generate trading session
'''access_token = open("access_token.txt",'r').read()
key_secret = open("api_key.txt",'r').read().split()
kite = KiteConnect(api_key=key_secret[0])
kite.set_access_token(access_token)

#get dump of all NSE instruments
instrument_dump = kite.instruments("NSE")
instrument_df = pd.DataFrame(instrument_dump)

'''
def instrumentLookup(instrument_df,symbol):
    """Looks up instrument token for a given script from instrument dump"""
    try:
        return instrument_df[instrument_df.tradingsymbol==symbol].instrument_token.values[0]
    except:
        return -1

def fetchOHLC(ticker,interval,duration):
    """extracts historical data and outputs in the form of dataframe"""
    instrument = instrumentLookup(instrument_df,ticker)
    data = pd.DataFrame(kite.historical_data(instrument,dt.date.today()-dt.timedelta(duration), dt.date.today(),interval))
    data.set_index("date",inplace=True)
    return data

def doji(ohlc_df):    
    """returns dataframe with doji candle column"""
    df = ohlc_df.copy()
    avg_candle_size = abs(df['close']-df['open']).median()#abs(df["close"]- df["open"]).median()
    df["doji"] = abs(df["close"] - df["open"]) <=  (0.05 * avg_candle_size)
    return df

def maru_bozu(ohlc_df):    
    """returns dataframe with maru bozu candle column"""
    df = ohlc_df.copy()
    avg_candle_size = abs(df["close"] - df["open"]).median()
    df["h-c"] = df["high"]-df["close"]
    df["l-o"] = df["low"]-df["open"]
    df["h-o"] = df["high"]-df["open"]
    df["l-c"] = df["low"]-df["close"]
    df["maru_bozu"] = np.where((df["close"] - df["open"] > 2*avg_candle_size) & \
                               (df[["h-c","l-o"]].max(axis=1) < 0.005*avg_candle_size),"maru_bozu_green",
                               np.where((df["open"] - df["close"] > 2*avg_candle_size) & \
                               (abs(df[["h-o","l-c"]]).max(axis=1) < 0.005*avg_candle_size),"maru_bozu_red",False))
    df.drop(["h-c","l-o","h-o","l-c"],axis=1,inplace=True)
    return df

def hammer(ohlc_df):    
    """returns dataframe with hammer candle column"""
    df = ohlc_df.copy()
    df["hammer"] = (((df["high"] - df["low"])>3*(df["open"] - df["close"])) & \
                   ((df["close"] - df["low"])/(.001 + df["high"] - df["low"]) > 0.6) & \
                   ((df["open"] - df["low"])/(.001 + df["high"] - df["low"]) > 0.6)) & \
                   (abs(df["close"] - df["open"]) > 0.1* (df["high"] - df["low"]))
    return df


def shooting_star(ohlc_df):    
    """returns dataframe with shooting star candle column"""
    df = ohlc_df.copy()
    df["sstar"] = (((df["high"] - df["low"])>3*(df["open"] - df["close"])) & \
                   ((df["high"] - df["close"])/(.001 + df["high"] - df["low"]) > 0.6) & \
                   ((df["high"] - df["open"])/(.001 + df["high"] - df["low"]) > 0.6)) & \
                   (abs(df["close"] - df["open"]) > 0.1* (df["high"] - df["low"]))
    return df

def levels(ohlc_day):    
    """returns pivot point and support/resistance levels"""
    high = round(ohlc_day["high"][-1],2)
    low = round(ohlc_day["low"][-1],2)
    close = round(ohlc_day["close"][-1],2)
    pivot = round((high + low + close)/3,2)
    r1 = round((2*pivot - low),2)
    r2 = round((pivot + (high - low)),2)
    r3 = round((high + 2*(pivot - low)),2)
    s1 = round((2*pivot - high),2)
    s2 = round((pivot - (high - low)),2)
    s3 = round((low - 2*(high - pivot)),2)
    return (pivot,r1,r2,r3,s1,s2,s3)

def trend(ohlc_df,n):
    "function to assess the trend by analyzing each candle"
    df = ohlc_df.copy()
    df["up"] = np.where(df["low"]>=df["low"].shift(1),1,0)
    df["dn"] = np.where(df["high"]<=df["high"].shift(1),1,0)
    if df["close"][-1] > df["open"][-1]:
        if df["up"][-1*n:].sum() >= 0.7*n:
            return "uptrend"
    elif df["open"][-1] > df["close"][-1]:
        if df["dn"][-1*n:].sum() >= 0.7*n:
            return "downtrend"
    else:
        return None
   
def res_sup(ohlc_df,ohlc_day):
    """calculates closest resistance and support levels for a given candle"""
    level = ((ohlc_df["close"][-1] + ohlc_df["open"][-1])/2 + (ohlc_df["high"][-1] + ohlc_df["low"][-1])/2)/2
    p,r1,r2,r3,s1,s2,s3 = levels(ohlc_day)
    l_r1=level-r1
    l_r2=level-r2
    l_r3=level-r3
    l_p=level-p
    l_s1=level-s1
    l_s2=level-s2
    l_s3=level-s3
    lev_ser = pd.Series([l_p,l_r1,l_r2,l_r3,l_s1,l_s2,l_s3],index=["p","r1","r2","r3","s1","s2","s3"])
    sup = lev_ser[lev_ser>0].idxmin()
    res = lev_ser[lev_ser>0].idxmax()
    return (eval('{}'.format(res)), eval('{}'.format(sup)))

def candle_type(ohlc_df):    
    """returns the candle type of the last candle of an OHLC DF"""
    '''ohlc_df['open']=int(ohlc_df['open'])
    ohlc_df['close']=int(ohlc_df['close'])
    ohlc_df['high']=int(ohlc_df['high'])
    ohlc_df['low']=int(ohlc_df['low'])'''
    candle = None
    if doji(ohlc_df)["doji"][-1] == True:
        candle = "doji"    
    if maru_bozu(ohlc_df)["maru_bozu"][-1] == "maru_bozu_green":
        candle = "maru_bozu_green"       
    if maru_bozu(ohlc_df)["maru_bozu"][-1] == "maru_bozu_red":
        candle = "maru_bozu_red"        
    if shooting_star(ohlc_df)["sstar"][-1] == True:
        candle = "shooting_star"        
    if hammer(ohlc_df)["hammer"][-1] == True:
        candle = "hammer"       
    return candle

def candle_pattern(ohlc_df,ohlc_day):    
    """returns the candle pattern identified"""
    pattern = None
    signi = "low"
    avg_candle_size = abs(ohlc_df["close"] - ohlc_df["open"]).median()
    sup, res = res_sup(ohlc_df,ohlc_day)
    
    if (sup - 1.5*avg_candle_size) < ohlc_df["close"][-1] < (sup + 1.5*avg_candle_size):
        signi = "HIGH"
        
    if (res - 1.5*avg_candle_size) < ohlc_df["close"][-1] < (res + 1.5*avg_candle_size):
        signi = "HIGH"
    
    if candle_type(ohlc_df) == 'doji' \
        and ohlc_df["close"][-1] > ohlc_df["close"][-2] \
        and ohlc_df["close"][-1] > ohlc_df["open"][-1]:
            pattern = "doji_bullish"
    
    if candle_type(ohlc_df) == 'doji' \
        and ohlc_df["close"][-1] < ohlc_df["close"][-2] \
        and ohlc_df["close"][-1] < ohlc_df["open"][-1]:
            pattern = "doji_bearish" 
            
    if candle_type(ohlc_df) == "maru_bozu_green":
        pattern = "maru_bozu_bullish"
    
    if candle_type(ohlc_df) == "maru_bozu_red":
        pattern = "maru_bozu_bearish"
        
    if trend(ohlc_df.iloc[:-1,:],7) == "uptrend" and candle_type(ohlc_df) == "hammer":
        pattern = "hanging_man_bearish"
        
    if trend(ohlc_df.iloc[:-1,:],7) == "downtrend" and candle_type(ohlc_df) == "hammer":
        pattern = "hammer_bullish"
        
    if trend(ohlc_df.iloc[:-1,:],7) == "uptrend" and candle_type(ohlc_df) == "shooting_star":
        pattern = "shooting_star_bearish"
        
    if trend(ohlc_df.iloc[:-1,:],7) == "uptrend" \
        and candle_type(ohlc_df) == "doji" \
        and ohlc_df["high"][-1] < ohlc_df["close"][-2] \
        and ohlc_df["low"][-1] > ohlc_df["open"][-2]:
        pattern = "harami_cross_bearish"
        
    if trend(ohlc_df.iloc[:-1,:],7) == "downtrend" \
        and candle_type(ohlc_df) == "doji" \
        and ohlc_df["high"][-1] < ohlc_df["open"][-2] \
        and ohlc_df["low"][-1] > ohlc_df["close"][-2]:
        pattern = "harami_cross_bullish"
        
    if trend(ohlc_df.iloc[:-1,:],7) == "uptrend" \
        and candle_type(ohlc_df) != "doji" \
        and ohlc_df["open"][-1] > ohlc_df["high"][-2] \
        and ohlc_df["close"][-1] < ohlc_df["low"][-2]:
        pattern = "engulfing_bearish"
        
    if trend(ohlc_df.iloc[:-1,:],7) == "downtrend" \
        and candle_type(ohlc_df) != "doji" \
        and ohlc_df["close"][-1] > ohlc_df["high"][-2] \
        and ohlc_df["open"][-1] < ohlc_df["low"][-2]:
        pattern = "engulfing_bullish"
       
    return "Significance - {}, Pattern - {}".format(signi,pattern)

##############################################################################################
tickers = ["ZEEL","WIPRO","VEDL","ULTRACEMCO","UPL","TITAN","TECHM","TATASTEEL",
           "TATAMOTORS","TCS","SUNPHARMA","SBIN","SHREECEM","RELIANCE","POWERGRID",
           "ONGC","NESTLEIND","NTPC","MARUTI","M&M","LT","KOTAKBANK","JSWSTEEL","INFY",
           "INDUSINDBK","IOC","ITC","ICICIBANK","HDFC","HINDUNILVR","HINDALCO",
           "HEROMOTOCO","HDFCBANK","HCLTECH","GRASIM","GAIL","EICHERMOT","DRREDDY",
           "COALINDIA","CIPLA","BRITANNIA","INFRATEL","BHARTIARTL","BPCL","BAJAJFINSV",
           "BAJFINANCE","BAJAJ-AUTO","AXISBANK","ASIANPAINT","ADANIPORTS","IDEA",
           "MCDOWELL-N","UBL","NIACL","SIEMENS","SRTRANSFIN","SBILIFE","PNB",
           "PGHH","PFC","PEL","PIDILITIND","PETRONET","PAGEIND","OFSS","NMDC","NHPC",
           "MOTHERSUMI","MARICO","LUPIN","L&TFH","INDIGO","IBULHSGFIN","ICICIPRULI",
           "ICICIGI","HINDZINC","HINDPETRO","HAVELLS","HDFCLIFE","HDFCAMC","GODREJCP",
           "GICRE","DIVISLAB","DABUR","DLF","CONCOR","COLPAL","CADILAHC","BOSCHLTD",
           "BIOCON","BERGEPAINT","BANKBARODA","BANDHANBNK","BAJAJHLDNG","DMART",
           "AUROPHARMA","ASHOKLEY","AMBUJACEM","ADANITRANS","ACC",
           "WHIRLPOOL","WABCOINDIA","VOLTAS","VINATIORGA","VBL","VARROC","VGUARD",
           "UNIONBANK","UCOBANK","TRENT","TORNTPOWER","TORNTPHARM","THERMAX","RAMCOCEM",
           "TATAPOWER","TATACONSUM","TVSMOTOR","TTKPRESTIG","SYNGENE","SYMPHONY",
           "SUPREMEIND","SUNDRMFAST","SUNDARMFIN","SUNTV","STRTECH","SAIL","SOLARINDS",
           "SHRIRAMCIT","SCHAEFFLER","SANOFI","SRF","SKFINDIA","SJVN","RELAXO",
           "RAJESHEXPO","RECLTD","RBLBANK","QUESS","PRESTIGE","POLYCAB","PHOENIXLTD",
           "PFIZER","PNBHOUSING","PIIND","OIL","OBEROIRLTY","NAM-INDIA","NATIONALUM",
           "NLCINDIA","NBCC","NATCOPHARM","MUTHOOTFIN","MPHASIS","MOTILALOFS","MINDTREE",
           "MFSL","MRPL","MANAPPURAM","MAHINDCIE","M&MFIN","MGL","MRF","LTI","LICHSGFIN",
           "LTTS","KANSAINER","KRBL","JUBILANT","JUBLFOOD","JINDALSTEL","JSWENERGY",
           "IPCALAB","NAUKRI","IGL","IOB","INDHOTEL","INDIANB","IBVENTURES","IDFCFIRSTB",
           "IDBI","ISEC","HUDCO","HONAUT","HAL","HEXAWARE","HATSUN","HEG","GSPL",
           "GUJGASLTD","GRAPHITE","GODREJPROP","GODREJIND","GODREJAGRO","GLENMARK",
           "GLAXO","GILLETTE","GMRINFRA","FRETAIL","FCONSUMER","FORTIS","FEDERALBNK",
           "EXIDEIND","ESCORTS","ERIS","ENGINERSIN","ENDURANCE","EMAMILTD","EDELWEISS",
           "EIHOTEL","LALPATHLAB","DALBHARAT","CUMMINSIND","CROMPTON","COROMANDEL","CUB",
           "CHOLAFIN","CHOLAHLDNG","CENTRALBK","CASTROLIND","CANBK","CRISIL","CESC",
           "BBTC","BLUEDART","BHEL","BHARATFORG","BEL","BAYERCROP","BATAINDIA",
           "BANKINDIA","BALKRISIND","ATUL","ASTRAL","APOLLOTYRE","APOLLOHOSP",
           "AMARAJABAT","ALKEM","APLLTD","AJANTPHARM","ABFRL","ABCAPITAL","ADANIPOWER",
           "ADANIGREEN","ADANIGAS","ABBOTINDIA","AAVAS","AARTIIND","AUBANK","AIAENG","3MINDIA"]


def main():
    for ticker in tickers:
        try:
            ohlc = fetchOHLC(ticker, '5minute',5)
            ohlc_day = fetchOHLC(ticker, 'day',30) 
            ohlc_day = ohlc_day.iloc[:-1,:]       
            cp = candle_pattern(ohlc,ohlc_day) 
            print(ticker, ": ",cp)   
        except:
            print("skipping for ",ticker)
'''        
# Continuous execution        
starttime=time.time()
timeout = time.time() + 60*60*1  # 60 seconds times 60 meaning the script will run for 1 hr
while time.time() <= timeout:
    try:
        print("passthrough at ",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        main()
        time.sleep(300 - ((time.time() - starttime) % 300.0)) # 300 second interval between each new execution
    except KeyboardInterrupt:
        print('\n\nKeyboard exception received. Exiting.')
        exit()'''

from pprint import pprint
def AlphaData_fxintraday(frombase,to,interval):
    import requests
    import json
    from pprint import pprint
    global apikey
    url="https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol={}&to_symbol={}&interval={}min&apikey={}".format(frombase,to,interval,apikey)
    data=requests.get(url).json()
    #pprint(dict(data['Time Series FX ({}min)'.format(interval)]))#['2020-07-31 20:20:00'])#['4. close'])
    import pandas as pd
    try:
        if data:
            data=data['Time Series FX ({}min)'.format(interval)]
            df=pd.DataFrame(data).T
            df['open']=df['1. open']
            df['high']=df['2. high']
            df['low']=df['3. low']
            df['close']=df['4. close']
            df=df.drop(['1. open','2. high','3. low', '4. close'], axis=1)
            return df#data['Time Series FX ({}min)'.format(interval)]
    except:
        print("An exception occurred")
        
frombase=['EUR','USD','GBP','AUD','EUR']
to=['USD','JPY','CAD','CNY','CHF','HKD','GBP','KRW']
'''
for j in frombase:
    for i in to:
        pprint('{}/{} in process'.format(i,j))
        data=AlphaData_intraday(i,j,60)
        pprint('{}/{} Done'.format(i,j))
        time.sleep(30)
'''

def AlphaData_fxdaily(frombase,to):
    import requests
    import json
    from pprint import pprint
    global apikey
    url="https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={}&to_symbol={}&apikey={}".format(frombase,to,apikey)
    #url="https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol={}&to_symbol={}&interval={}min&apikey={}".format(frombase,to,interval,apikey)
    data=requests.get(url).json()
    #pprint(dict(data['Time Series FX ({}min)'.format(interval)]))#['2020-07-31 20:20:00'])#['4. close'])
    import pandas as pd
    try:
        if data:
            data=data['Time Series FX (Daily)']
            df=pd.DataFrame(data).T
            df['open']=df['1. open']
            df['high']=df['2. high']
            df['low']=df['3. low']
            df['close']=df['4. close']
            df=df.drop(['1. open','2. high','3. low', '4. close'], axis=1)
            return df#data['Time Series FX ({}min)'.format(interval)]
    except:
        print("An exception occurred")

'''
for j in frombase:
    for i in to:
        pprint('{}/{} in process'.format(i,j))
        dataintra=AlphaData_intraday(i,j,5)
        datadaily=AlphaData_daily(i,j)
        pprint(dataintra)
        if len(dataintra) > 0:
            if len(datadaily) > 0 :
                pprint(candle_type(dataintra))
                #cp = candle_pattern(dataintra,datadaily) 
                pprint('{}/{} Done'.format(i,j))
                time.sleep(5)'''
'''

for j in frombase:
    for i in to:
        pprint('{}/{} in process'.format(i,j))
        data=AlphaData_daily(i,j)
        
        pprint('{}/{} Done'.format(i,j))
        time.sleep(5)
'''




def AlphaData_intraday(symbol,interval):
    import requests
    import json
    from pprint import pprint
    global apikey
    url="https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval={}min&apikey={}".format(symbol,interval,apikey)
    data=requests.get(url).json()
    #pprint(dict(data['Time Series FX ({}min)'.format(interval)]))#['2020-07-31 20:20:00'])#['4. close'])
    import pandas as pd
    try:
        if data:
            data=data['Time Series ({}min)'.format(interval)]
            df=pd.DataFrame(data).T
            df['open']=df['1. open']
            df['high']=df['2. high']
            df['low']=df['3. low']
            df['close']=df['4. close']
            df['volume']=df['5. volume']
            df['volume']=df['5. volume']
            df=df.drop(['1. open','2. high','3. low', '4. close','5. volume'], axis=1)
            df['open']=pd.to_numeric(df['open'])
            df['high']=pd.to_numeric(df['high'])
            df['low']=pd.to_numeric(df['low'])
            df['close']=pd.to_numeric(df['close'])
            df['volume']=pd.to_numeric(df['volume'])
            return df#data['Time Series FX ({}min)'.format(interval)]
    except:
        print("An exception occurred")


def AlphaData_daily(symbol):
    import requests
    import json
    from pprint import pprint
    global apikey
    url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}".format(symbol,apikey)
    #url="https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol={}&to_symbol={}&interval={}min&apikey={}".format(frombase,to,interval,apikey)
    data=requests.get(url).json()
    #pprint(dict(data['Time Series FX ({}min)'.format(interval)]))#['2020-07-31 20:20:00'])#['4. close'])
    import pandas as pd
    try:
        if data:
            data=data['Time Series (Daily)']
            df=pd.DataFrame(data).T
            df['open']=df['1. open']
            df['high']=df['2. high']
            df['low']=df['3. low']
            df['close']=df['4. close']
            df['volume']=df['5. volume']
            df=df.drop(['1. open','2. high','3. low', '4. close','5. volume'], axis=1)
            df['open']=pd.to_numeric(df['open'])
            df['high']=pd.to_numeric(df['high'])
            df['low']=pd.to_numeric(df['low'])
            df['close']=pd.to_numeric(df['close'])
            df['volume']=pd.to_numeric(df['volume'])
            return df#data['Time Series FX ({}min)'.format(interval)]
    except:
        print("An exception occurred")

''''
for i in to:
    pprint('{}/{} in process'.format(i,j))
    dataintra=AlphaData_intraday(i,5)
    datadaily=AlphaData_daily(i)
    pprint(dataintra)
    if len(dataintra) > 0:
        if len(datadaily) > 0 :
            pprint(candle_type(dataintra))
            #cp = candle_pattern(dataintra,datadaily) 
            pprint('{}/{} Done'.format(i,j))
            time.sleep(5)'''
def main():
    for ticker in tickers:
        try:
            ohlc = fetchOHLC(ticker, '5minute',5)
            ohlc_day = fetchOHLC(ticker, 'day',30) 
            ohlc_day = ohlc_day.iloc[:-1,:]       
            cp = candle_pattern(ohlc,ohlc_day) 
            print(ticker, ": ",cp)   
        except:
            print("skipping for ",ticker)

ticks=['atvi','adbe','amd','alxn','algn','goog','googl','amzn','amgn','adi','anss','aapl','amat','asml','adsk','adp','bidu','biib','bmrn','bkng','avgo','cdns','cdw','cern','chtr','chkp','ctas','csco','ctxs','ctsh','cmcsa','cprt','cost','csx','dxcm','docu','dltr','ebay','ea','exc','expe','fb','fast','fisv','fox','foxa','gild','idxx','ilmn','incy','intc','intu','isrg','jd','klac','lrcx','lbtya','lbtyk','lulu','mar','mxim','meli','mchp','mu','msft','mrna','mdlz','mnst','ntap','ntes','nflx','nvda','nxpi','orly','pcar','payx','pypl','pep','qcom','regn','rost','sgen','siri','swks','splk','sbux','snps','tmus','ttwo','tsla','txn','khc','tcom','ulta','vrsn','vrsk','vrtx','wba','wdc','wday','xel','xlnx','zm']



    
patterns=['Two Crows',
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
'Upside/Downside Gap Three Methods']

def texterconversion(text):
    tex=text.replace('/','').replace('-','_').replace(' ','_').replace('(','').replace(')','')
    return tex


def technical_lib(technical,df):
    open=df['open']
    high=df['high']
    low=df['low']
    close=df['close']
    if technical == 'Two_Crows':
        tech=Two_Crows(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Three_Black_Crows':
        tech=Three_Black_Crows(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Three_Inside_UpDown':
        tech=Three_Inside_UpDown(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Three_Line_Strike':
        tech=Three_Line_Strike(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Three_Outside_UpDown':
        tech=Three_Outside_UpDown(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Three_Stars_In_The_South':
        tech=Three_Stars_In_The_South(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Three_Advancing_White_Soldiers':
        tech=Three_Advancing_White_Soldiers(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Abandoned_Baby':
        tech=Abandoned_Baby(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Advance_Block':
        tech=Advance_Block(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Belt_hold':
        tech=Belt_hold(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Breakaway':
        tech=Breakaway(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Closing_Marubozu':
        tech=Closing_Marubozu(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Concealing_Baby_Swallow':
        tech=Concealing_Baby_Swallow(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Counterattack':
        tech=Counterattack(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Dark_Cloud_Cover':
        tech=Dark_Cloud_Cover(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Doji':
        tech=Doji(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Doji_Star':
        tech=Doji_Star(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Dragonfly_Doji':
        tech=Dragonfly_Doji(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Engulfing_Pattern':
        tech=Engulfing_Pattern(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Evening_Doji_Star':
        tech=Evening_Doji_Star(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Evening_Star':
        tech=Evening_Star(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'UpDown_gap_side_by_side_white_lines':
        tech=UpDown_gap_side_by_side_white_lines(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Gravestone_Doji':
        tech=Gravestone_Doji(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Hammer':
        tech=Hammer(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Hanging_Man':
        tech=Hanging_Man(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Harami_Pattern':
        tech=Harami_Pattern(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Harami_Cross_Pattern':
        tech=Harami_Cross_Pattern(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'High_Wave_Candle':
        tech=High_Wave_Candle(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Hikkake_Pattern':
        tech=Hikkake_Pattern(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Modified_Hikkake_Pattern':
        tech=Modified_Hikkake_Pattern(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Homing_Pigeon':
        tech=Homing_Pigeon(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Identical_Three_Crows':
        tech=Identical_Three_Crows(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'In_Neck_Pattern':
        tech=In_Neck_Pattern(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Inverted_Hammer':
        tech=Inverted_Hammer(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Kicking':
        tech=Kicking(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Kicking___bullbear':
        tech=Kicking___bullbear(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Ladder_Bottom':
        tech=Ladder_Bottom(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Long_Legged_Doji':
        tech=Long_Legged_Doji(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Long_Line_Candle':
        tech=Long_Line_Candle(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Marubozu':
        tech=Marubozu(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Matching_Low':
        tech=Matching_Low(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Mat_Hold':
        tech=Mat_Hold(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Morning_Doji_Star':
        tech=Morning_Doji_Star(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))        
    elif technical == 'Morning_Star':
        tech=Morning_Star(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'On_Neck_Pattern':
        tech=On_Neck_Pattern(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Piercing_Pattern':
        tech=Piercing_Pattern(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Rickshaw_Man':
        tech=Rickshaw_Man(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'RisingFalling_Three_Methods':
        tech=RisingFalling_Three_Methods(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Separating_Lines':
        tech=Separating_Lines(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Shooting_Star':
        tech=Shooting_Star(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Short_Line_Candle':
        tech=Short_Line_Candle(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Spinning_Top':
        tech=Spinning_Top(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Stalled_Pattern':
        tech=Stalled_Pattern(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Stick_Sandwich':
        tech=Stick_Sandwich(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Takuri':
        tech=Takuri(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Tasuki_Gap':
        tech=Tasuki_Gap(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Thrusting_Pattern':
        tech=Thrusting_Pattern(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Tristar_Pattern':
        tech=Tristar_Pattern(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Unique_3_River':
        tech=Unique_3_River(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'Upside_Gap_Two_Crows':
        tech=Upside_Gap_Two_Crows(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    elif technical == 'UpsideDownside_Gap_Three_Methods':
        tech=UpsideDownside_Gap_Three_Methods(open,high,low,close)
        tech=pd.DataFrame(tech)
        tech[0]=(np.where(tech[0] > 0,'{}_bullish'.format(technical),np.where(tech[0] < 0,'{}_bearish'.format(technical),0)))
    else:
        print('Error ocurred')
    return tech


''''
for i in ticks:
    try:    
        
        pprint('{} in process'.format(i))
        dataintra=AlphaData_intraday(i,5)
        #pprint(pd.DataFrame(Two_Crows(dataintra['open'],dataintra['high'],dataintra['low'],dataintra['close'])))
        datadaily=AlphaData_daily(i)
        pprint(res_sup(dataintra,datadaily))
        '''#for j in patterns:
            #data=technical_lib(texterconversion(j),dataintra)
            #data=data.iloc[:1,0]
            #tech=pd.DataFrame(Two_Crows(dataintra['open'],dataintra['high'],dataintra['low'],dataintra['close']))
            #if data[0] != 0:
            #    pprint(data)'''
''' pprint(dataintra)
        if len(dataintra) > 0:
            if len(datadaily) > 0 :
                pprint(candle_type(dataintra))
                cp = candle_pattern(dataintra,datadaily) 
                print(cp)
                pprint('{} Done'.format(i))
                #time.sleep(5)
        time.sleep(15)
    except:
        print(i,' got skipped')
'''









#forex_pairs=['AUD/CAD ','AUD/CHF',' AUD/JPY','AUD/NZD',' AUD/USD',' CAD/CHF','CAD/JPY ','CHF/JPY',' EUR/AUD','EUR/CAD ','EUR/CHF',' EUR/GBP','EUR/JPY ','EUR/NOK',' EUR/NZD','EUR/SEK ','EUR/TRY',' EUR/USD','GBP/AUD ','GBP/CAD',' GBP/CHF','GBP/JPY ','GBP/NZD',' GBP/USD','NZD/CAD ','NZD/CHF ','NZD/JPY','NZD/USD ','TRY/JPY ','USD/CAD','USD/CHF ','USD/CNH ','USD/JPY','USD/MXN ','USD/NOK ','USD/SEK','USD/TRY ','USD/ZAR',' ZAR/JPY']
pairs=['AUD/CAD', 'AUD/CHF', 'AUD/JPY', 'AUD/NZD', 'AUD/USD', 'AUS200', 'Bund', 'CAD/CHF', 'CAD/JPY', 'CHF/JPY', 'CHN50', 'Copper', 'ESP35', 'EUR/AUD', 'EUR/CAD', 'EUR/CHF', 'EUR/GBP', 'EUR/JPY', 'EUR/NOK']
import fxcmpy
access_='a933e3362d93f30f9ebf251206e8a5fb0bb5f44a'

con = fxcmpy.fxcmpy(access_token=access_, log_level='error', server='demo', log_file='log.txt')
#print(con.get_instruments())
for i in pairs:
    data = con.get_candles(i, period='m5', number=10)
    pprint(data)
    time.sleep(15)
con.close()