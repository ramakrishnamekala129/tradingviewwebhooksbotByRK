from database import *

function=[
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
'Upside/Downside Gap Three Methods',
]

names=[
'CDL2CROWS',
'CDL3BLACKCROWS',
'CDL3INSIDE',
'CDL3LINESTRIKE',
'CDL3OUTSIDE',
'CDL3STARSINSOUTH',
'CDL3WHITESOLDIERS',
'CDLABANDONEDBABY',
'CDLADVANCEBLOCK',
'CDLBELTHOLD',
'CDLBREAKAWAY',
'CDLCLOSINGMARUBOZU',
'CDLCONCEALBABYSWALL',
'CDLCOUNTERATTACK',
'CDLDARKCLOUDCOVER',
'CDLDOJI',
'CDLDOJISTAR',
'CDLDRAGONFLYDOJI',
'CDLENGULFING',
'CDLEVENINGDOJISTAR',
'CDLEVENINGSTAR',
'CDLGAPSIDESIDEWHITE',
'CDLGRAVESTONEDOJI',
'CDLHAMMER',
'CDLHANGINGMAN',
'CDLHARAMI',
'CDLHARAMICROSS',
'CDLHIGHWAVE',
'CDLHIKKAKE',
'CDLHIKKAKEMOD',
'CDLHOMINGPIGEON',
'CDLIDENTICAL3CROWS',
'CDLINNECK',
'CDLINVERTEDHAMMER',
'CDLKICKING',
'CDLKICKINGBYLENGTH',
'CDLLADDERBOTTOM',
'CDLLONGLEGGEDDOJI',
'CDLLONGLINE',
'CDLMARUBOZU',
'CDLMATCHINGLOW',
'CDLMATHOLD',
'CDLMORNINGDOJISTAR',
'CDLMORNINGSTAR',
'CDLONNECK',
'CDLPIERCING',
'CDLRICKSHAWMAN',
'CDLRISEFALL3METHODS',
'CDLSEPARATINGLINES',
'CDLSHOOTINGSTAR',
'CDLSHORTLINE',
'CDLSPINNINGTOP',
'CDLSTALLEDPATTERN',
'CDLSTICKSANDWICH',
'CDLTAKURI',
'CDLTASUKIGAP',
'CDLTHRUSTING',
'CDLTRISTAR',
'CDLUNIQUE3RIVER',
'CDLUPSIDEGAP2CROWS',
'CDLXSIDEGAP3METHODS'
]
'''
for i in range(0,60):
    k=function[i].replace('/','').replace('-','_').replace(' ','_')
    d=names[i].replace('CDL','').lower()
    print('def {}(open,high,low,close):\n'.format(k))
    print('    {}=ta.{}(open,high,low,close)\n'.format(d,names[i]))
    print('    return {}'.format(d))'''
from pprint import pprint
import pandas as pd
df=list(db.BTCUSDT_15m.find())
df=pd.DataFrame(df)
from technicalta import technicalselector

#print(len(function))
#pprint(df)
for i in range(0,60):
    k=function[i].replace('/','').replace('-','_').replace(' ','_')
    #pprint(k)
    df[k]=technicalselector(k,df)


print(df.iloc[-1,7:])