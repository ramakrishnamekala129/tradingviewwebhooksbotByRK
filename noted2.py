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
from Exchangeside import *
from technicalta import *
#k,p=Plotindicator()

#print(listof1)

#print(indicator_data_level_2())        


'''
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
'''

#print(indicator_data_level_3())
'''
Moving_average=[
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
'''

'''
for i in Moving_average:
    print("elif technical == '{}':".format(texterconversion(i)))
    print("    tech={}()".format(texterconversion(i)))
'''


'''
def technicalselector(technical):
    if technical == 'Bollinger_Bands':
        technical='BBANDS'
    elif technical == 'Double_Exponential_Moving_Average':
        technical='DEMA'
    elif technical == 'Exponential_Moving_Average':
        technical='EMA'
    elif technical == 'HilbertTransform___Instantaneous_Trendline':
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
'''
#print(d)
#print(p)
#s for s in sentences if not any(w in s for w in required_words)
'''names=['BBANDS',
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
    'On Balance Volume'
    ]

for i in range(0,len(names)-1):
    print("elif technical == '{}':".format(function[i]))
    k=function[i].replace('/','').replace('-','_').replace(' ','_').replace('(','').replace(')','')
    print("    technical='{}()'".format(k))


listed=list(db.BTCUSDT_30m.find())
df=pd.DataFrame(listed)
df.set_index('date')
print(len(df))
from technicalta import Bollinger_Bands,High_Wave_Candle
close=df['Close']
open=df['Open']
high=df['High']
low=df['Low']
data=Bollinger_Bands(close)
pprint(data)
data=High_Wave_Candle(open,high,low,close)
pprint(data)

Moving_average=[
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
'Weighted Moving Average'
]

oscillator=[
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
'Williams']



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
    'On Balance Volume'

'''
'''
function=[
'Vector Arithmetic Add',
'Vector Arithmetic Div',
'Highest value',
'Index of highest value',
'Lowest value',
'Index of lowest value',
'Lowest and highest values ',
'Indexes of lowest and highest ',
'Vector Arithmetic Mult',
'Vector Arithmetic Substraction',
'Summation']

names=[
'ADD',
'DIV',
'MAX',
'MAXINDEX',
'MIN',
'MININDEX',
'MINMAX',
'MINMAXINDEX',
'MULT',
'SUB',
'SUM'
]
print(len(names),len(function))
for i in range(0,len(names)):
    k=function[i].replace('/','').replace('-','_').replace(' ','_').replace('(','').replace(')','')
    d=names[i].replace('CDL','').lower()
    print('def {}(close):'.format(k))
    print('    {}=ta.{}(close)'.format(d,names[i]))
    print('    return {}'.format(d))


def Vector_Arithmetic_Add(high, low):
    add=ta.ADD(high, low)
    return add
def Vector_Arithmetic_Div(high, low):
    div=ta.DIV(high, low)
    return div
def Highest_value(close, timeperiod=30):
    max=ta.MAX(close, timeperiod)
    return max
def Index_of_highest_value(close, timeperiod=30):
    maxindex=ta.MAXINDEX(close, timeperiod)
    return maxindex
def Lowest_value(close, timeperiod=30):
    min=ta.MIN(close, timeperiod)
    return min
def Index_of_lowest_value(close, timeperiod=30):
    minindex=ta.MININDEX(close, timeperiod)
    return minindex
def Lowest_and_highest_values_(close, timeperiod=30):
    min ,max=ta.MINMAX(close, timeperiod)
    return min,max
def Indexes_of_lowest_and_highest_(close, timeperiod=30):
    minmaxindex=ta.MINMAXINDEX(close, timeperiod)
    return minmaxindex
def Vector_Arithmetic_Mult(high, low):
    mult=ta.MULT(high, low)
    return mult
def Vector_Arithmetic_Substraction(high, low):
    sub=ta.SUB(high, low)
    return sub
def Summation(close, timeperiod=30):
    sum=ta.SUM(close, timeperiod)
    return sum

'''
'''
ADD                  Vector Arithmetic Add
DIV                  Vector Arithmetic Div
MAX                  Highest value over a specified period
MAXINDEX             Index of highest value over a specified period
MIN                  Lowest value over a specified period
MININDEX             Index of lowest value over a specified period
MINMAX               Lowest and highest values over a specified period
MINMAXINDEX          Indexes of lowest and highest values over a specified period
MULT                 Vector Arithmetic Mult
SUB                  Vector Arithmetic Substraction
SUM                  Summation
'''



'''
function=[
'Vector Trigonometric ACos',
'Vector Trigonometric ASin',
'Vector Trigonometric ATan',
'Vector Ceil',
'Vector Trigonometric Cos',
'Vector Trigonometric Cosh',
'Vector Arithmetic Exp',
'Vector Floor',
'Vector Log Natural',
'Vector Log10',
'Vector Trigonometric Sin',
'Vector Trigonometric Sinh',
'Vector Square Root',
'Vector Trigonometric Tan',
'Vector Trigonometric Tanh']

names=[
'ACOS',
'ASIN',
'ATAN',
'CEIL',
'COS',
'COSH',
'EXP',
'FLOOR',
'LN',
'LOG10',
'SIN',
'SINH',
'SQRT',
'TAN',
'TANH']
print(len(names),len(function))
for i in range(0,len(names)):
    k=function[i].replace('/','').replace('-','_').replace(' ','_').replace('(','').replace(')','')
    d=names[i].replace('CDL','').lower()
    print('def {}(close):'.format(k))
    print('    {}=ta.{}(close)'.format(d,names[i]))
    print('    return {}'.format(d))

def Vector_Trigonometric_ACos(close):
    acos=ta.ACOS(close)
    return acos
def Vector_Trigonometric_ASin(close):
    asin=ta.ASIN(close)
    return asin
def Vector_Trigonometric_ATan(close):
    atan=ta.ATAN(close)
    return atan
def Vector_Ceil(close):
    ceil=ta.CEIL(close)
    return ceil
def Vector_Trigonometric_Cos(close):
    cos=ta.COS(close)
    return cos
def Vector_Trigonometric_Cosh(close):
    cosh=ta.COSH(close)
    return cosh
def Vector_Arithmetic_Exp(close):
    exp=ta.EXP(close)
    return exp
def Vector_Floor(close):
    floor=ta.FLOOR(close)
    return floor
def Vector_Log_Natural(close):
    ln=ta.LN(close)
    return ln
def Vector_Log10(close):
    log10=ta.LOG10(close)
    return log10
def Vector_Trigonometric_Sin(close):
    sin=ta.SIN(close)
    return sin
def Vector_Trigonometric_Sinh(close):
    sinh=ta.SINH(close)
    return sinh
def Vector_Square_Root(close):
    sqrt=ta.SQRT(close)
    return sqrt
def Vector_Trigonometric_Tan(close):
    tan=ta.TAN(close)
    return tan
def Vector_Trigonometric_Tanh(close):
    tanh=ta.TANH(close)
    return tanh
'''    
'''
ACOS                 Vector Trigonometric ACos
ASIN                 Vector Trigonometric ASin
ATAN                 Vector Trigonometric ATan
CEIL                 Vector Ceil
COS                  Vector Trigonometric Cos
COSH                 Vector Trigonometric Cosh
EXP                  Vector Arithmetic Exp
FLOOR                Vector Floor
LN                   Vector Log Natural
LOG10                Vector Log10
SIN                  Vector Trigonometric Sin
SINH                 Vector Trigonometric Sinh
SQRT                 Vector Square Root
TAN                  Vector Trigonometric Tan
TANH                 Vector Trigonometric Tanh
'''





'''
names=[
'AD',
'ADOSC',
'OBV',
]

function=[
'Chaikin A/D Line',
'Chaikin A/D Oscillator',
'On Balance Volume']
print(len(names),len(function))
for i in range(0,len(names)):
    k=function[i].replace('/','').replace('-','_').replace(' ','_').replace('(','').replace(')','')
    d=names[i].replace('CDL','').lower()
    print('def {}(close):'.format(k))
    print('    {}=ta.{}(close)'.format(d,names[i]))
    print('    return {}'.format(d))

def Chaikin_AD_Line(high, low, close, volume):
    ad=ta.AD(high, low, close, volume)
    return ad
def Chaikin_AD_Oscillator(high, low, close, volume, fastperiod=3, slowperiod=10):
    adosc=ta.ADOSC(high, low, close, volume, fastperiod, slowperiod)
    return adosc
def On_Balance_Volume(close, volume):
    obv=ta.OBV(close, volume)
    return obv
'''

'''
AD                   Chaikin A/D Line
ADOSC                Chaikin A/D Oscillator
OBV                  On Balance Volume
'''

'''
function=['Hilbert Transform - Dominant Cycle Period',
'Hilbert Transform - Dominant Cycle Phase',
'Hilbert Transform - Phasor Components',
'Hilbert Transform - SineWave',
'Hilbert Transform - Trend vs Cycle Mode']





names=['HT_DCPERIOD',
'HT_DCPHASE',
'HT_PHASOR',
'HT_SINE',
'HT_TRENDMODE']


print(len(names),len(function))
for i in range(0,len(names)):
    k=function[i].replace('/','').replace('-','_').replace(' ','_').replace('(','').replace(')','')
    d=names[i].replace('CDL','').lower()
    print('def {}(close):'.format(k))
    print('    {}=ta.{}(close)'.format(d,names[i]))
    print('    return {}'.format(d))


def Hilbert_Transform___Dominant_Cycle_Period(close):
    ht_dcperiod=ta.HT_DCPERIOD(close)
    return ht_dcperiod
def Hilbert_Transform___Dominant_Cycle_Phase(close):
    ht_dcphase=ta.HT_DCPHASE(close)
    return ht_dcphase
def Hilbert_Transform___Phasor_Components(close):
    ht_phasor=ta.HT_PHASOR(close)
    return ht_phasor
def Hilbert_Transform___SineWave(close):
    ht_sine=ta.HT_SINE(close)
    return ht_sine
def Hilbert_Transform___Trend_vs_Cycle_Mode(close):
    ht_trendmode=ta.HT_TRENDMODE(close)
    return ht_trendmode
'''

'''
HT_DCPERIOD          Hilbert Transform - Dominant Cycle Period
HT_DCPHASE           Hilbert Transform - Dominant Cycle Phase
HT_PHASOR            Hilbert Transform - Phasor Components
HT_SINE              Hilbert Transform - SineWave
HT_TRENDMODE         Hilbert Transform - Trend vs Cycle Mode
'''

'''
names=[
'BETA',
'CORREL',
'LINEARREG',
'LINEARREG_ANGLE',
'LINEARREG_INTERCEPT',
'LINEARREG_SLOPE',
'STDDEV',
'TSF',
'VAR']



function=[
'Beta',
'Pearson Correlation Coefficient',
'Linear Regression',
'Linear Regression Angle',
'Linear Regression Intercept',
'Linear Regression Slope',
'Standard Deviation',
'Time Series Forecast',
'Variance']


print(len(names),len(function))
for i in range(0,len(names)):
    k=function[i].replace('/','').replace('-','_').replace(' ','_').replace('(','').replace(')','')
    d=names[i].replace('CDL','').lower()
    print('def {}():'.format(k))
    print('    {}=ta.{}()'.format(d,names[i]))
    print('    return {}'.format(d))

def Beta(high, low, timeperiod=5):
    beta=ta.BETA(high, low, timeperiod)
    return beta
def Pearson_Correlation_Coefficient(high, low, timeperiod=30):
    correl=ta.CORREL(high, low, timeperiod)
    return correl
def Linear_Regression(close, timeperiod=14):
    linearreg=ta.LINEARREG(close, timeperiod)
    return linearreg
def Linear_Regression_Angle(close, timeperiod=14):
    linearreg_angle=ta.LINEARREG_ANGLE(close, timeperiod)
    return linearreg_angle
def Linear_Regression_Intercept(close, timeperiod=14):
    linearreg_intercept=ta.LINEARREG_INTERCEPT(close, timeperiod)
    return linearreg_intercept
def Linear_Regression_Slope(close, timeperiod=14):
    linearreg_slope=ta.LINEARREG_SLOPE(close, timeperiod)
    return linearreg_slope
def Standard_Deviation(close, timeperiod=5, nbdev=1):
    stddev=ta.STDDEV(close, timeperiod, nbdev)
    return stddev
def Time_Series_Forecast(close, timeperiod=14):
    tsf=ta.TSF(close, timeperiod)
    return tsf
def Variance(close, timeperiod=5, nbdev=1):
    var=ta.VAR(close, timeperiod, nbdev)
    return var


'''
'''
BETA                 Beta
CORREL               Pearson Correlation Coefficient (r)
LINEARREG            Linear Regression
LINEARREG_ANGLE      Linear Regression Angle
LINEARREG_INTERCEPT  Linear Regression Intercept
LINEARREG_SLOPE      Linear Regression Slope
STDDEV               Standard Deviation
TSF                  Time Series Forecast
VAR                  Variance
'''




'''from stocktrends import indicators

rows = 500
data=list(db.BTCUSDT_30m.find())
df=pd.DataFrame(data)
df['open']=df['Open']
df['close']=df['Close']
df['high']=df['High']
df['low']=df['Low']
print(df)
renko = indicators.Renko(df)
print('\n\nRenko box calcuation based on periodic close')
renko.brick_size = 2
renko.chart_type = indicators.Renko.PERIOD_CLOSE
data = renko.get_ohlc_data()
print(data)
'''


'''
function=[
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
'Williams']

names=[
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
'WILLR'
]

print(len(names),len(function))
for i in range(0,len(names)):
    k=function[i].replace('/','').replace('-','_').replace(' ','_').replace('(','').replace(')','')
    d=names[i].replace('CDL','').lower()
    print('def {}():'.format(k))
    print('    {}=ta.{}()'.format(d,names[i]))
    print('    return {}'.format(d))



def Average_Directional_Movement_Index(high, low, close, timeperiod=14):
    adx=ta.ADX(high, low, close, timeperiod)
    return adx
def Average_Directional_Movement_Index_Rating(high, low, close, timeperiod=14):
    adxr=ta.ADXR(high, low, close, timeperiod)
    return adxr
def Absolute_Price_Oscillator(close, fastperiod=12, slowperiod=26, matype=0):
    apo=ta.APO(close, fastperiod, slowperiod, matype)
    return apo
def Aroon(high, low, timeperiod=14):
    aroondown, aroonup=ta.AROON(high, low, timeperiod)
    return aroondown, aroonup
def Aroon_Oscillator(high, low, timeperiod=14):
    aroonosc=ta.AROONOSC(high, low, timeperiod)
    return aroonosc
def Balance_Of_Power(open, high, low, close):
    bop=ta.BOP(open, high, low, close)
    return bop
def Commodity_Channel_Index(high, low, close, timeperiod=14):
    cci=ta.CCI(high, low, close, timeperiod=14)
    return cci
def Chande_Momentum_Oscillator(close, timeperiod=14):
    cmo=ta.CMO(close, timeperiod)
    return cmo
def Directional_Movement_Index(high, low, close, timeperiod=14):
    dx=ta.DX(high, low, close, timeperiod)
    return dx
def Moving_Average_Convergence_Divergence(close, fastperiod=12, slowperiod=26, signalperiod=9):
    macd, macdsignal, macdhist=ta.MACD(close, fastperiod, slowperiod, signalperiod)
    return macd, macdsignal, macdhist
def MACD_with_controllable_MA_type(close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0):
    macd, macdsignal, macdhistt=ta.MACDEXT(close, fastperiod, fastmatype, slowperiod, slowmatype, signalperiod, signalmatype)
    return macd, macdsignal, macdhist
def Moving_Average_Convergence_Divergence_Fix(close, signalperiod=9):
    macd, macdsignal, macdhis=ta.MACDFIX(close, signalperiod)
    return macd, macdsignal, macdhis
def Money_Flow_Index(high, low, close, volume, timeperiod=14):
    mfi=ta.MFI(high, low, close, volume, timeperiod)
    return mfi
def Minus_Directional_Indicator(high, low, close, timeperiod=14):
    minus_di=ta.MINUS_DI(high, low, close, timeperiod)
    return minus_di
def Minus_Directional_Movement(high, low, timeperiod=14):
    minus_dm=ta.MINUS_DM(high, low, timeperiod)
    return minus_dm
def Momentum(close, timeperiod=10):
    mom=ta.MOM(close, timeperiod)
    return mom
def Plus_Directional_Indicator(high, low, close, timeperiod=14):
    plus_di=ta.PLUS_DI(high, low, close, timeperiod)
    return plus_di
def Plus_Directional_Movement(high, low, timeperiod=14):
    plus_dm=ta.PLUS_DM(high, low, timeperiod)
    return plus_dm
def Percentage_Price_Oscillator(close, fastperiod=12, slowperiod=26, matype=0):
    ppo=ta.PPO(close, fastperiod, slowperiod, matype)
    return ppo
def Rate_of_change(close, timeperiod=10):
    roc=ta.ROC(close, timeperiod)
    return roc
def Rate_of_change_Percentage(close, timeperiod=10):
    rocp=ta.ROCP(close, timeperiod)
    return rocp
def Rate_of_change_ratio(close, timeperiod=10):
    rocr=ta.ROCR(close, timeperiod)
    return rocr
def Rate_of_change_ratio_100_scale(close, timeperiod=10):
    rocr100=ta.ROCR100(close, timeperiod)
    return rocr100
def Relative_Strength_Index(close, timeperiod=14):
    rsi=ta.RSI(close, timeperiod)
    return rsi
def Stochastic(high, low, close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0):
    slowk, slowd=ta.STOCH(high, low, close, fastk_period, slowk_period, slowk_matype, slowd_period, slowd_matype)
    return slowk, slowd
def Stochastic_Fast(high, low, close, fastk_period=5, fastd_period=3, fastd_matype=0):
    fastk, fastd=ta.STOCHF(high, low, close, fastk_period, fastd_period, fastd_matype)
    return fastk, fastd
def Stochastic_Relative_Strength_Index(close, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0):
    fastk, fastd=ta.STOCHRSI(close, timeperiod, fastk_period, fastd_period, fastd_matype)
    return fastk, fastd
def one_day_Rate_Of_Change_ROC_of_a_Triple_Smooth_EMA(close, timeperiod=30):
    trix=ta.TRIX(close, timeperiod)
    return trix
def Ultimate_Oscillator(high, low, close, timeperiod1=7, timeperiod2=14, timeperiod3=28):
    ultosc=ta.ULTOSC(high, low, close, timeperiod1, timeperiod2, timeperiod3)
    return ultosc
def Williams(high, low, close, timeperiod=14):
    willr=ta.WILLR(high, low, close, timeperiod)
    return willr
'''



'''
ADX                  Average Directional Movement Index
ADXR                 Average Directional Movement Index Rating
APO                  Absolute Price Oscillator
AROON                Aroon
AROONOSC             Aroon Oscillator
BOP                  Balance Of Power
CCI                  Commodity Channel Index
CMO                  Chande Momentum Oscillator
DX                   Directional Movement Index
MACD                 Moving Average Convergence/Divergence
MACDEXT              MACD with controllable MA type
MACDFIX              Moving Average Convergence/Divergence Fix 12/26
MFI                  Money Flow Index
MINUS_DI             Minus Directional Indicator
MINUS_DM             Minus Directional Movement
MOM                  Momentum
PLUS_DI              Plus Directional Indicator
PLUS_DM              Plus Directional Movement
PPO                  Percentage Price Oscillator
ROC                  Rate of change : ((price/prevPrice)-1)*100
ROCP                 Rate of change Percentage: (price-prevPrice)/prevPrice
ROCR                 Rate of change ratio: (price/prevPrice)
ROCR100              Rate of change ratio 100 scale: (price/prevPrice)*100
RSI                  Relative Strength Index
STOCH                Stochastic
STOCHF               Stochastic Fast
STOCHRSI             Stochastic Relative Strength Index
TRIX                 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
ULTOSC               Ultimate Oscillator
WILLR                Williams' %R
'''

'''
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
'WMA']
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
'Weighted Moving Average'
]

print(len(names),len(function))
for i in range(0,len(names)):
    k=function[i].replace('/','').replace('-','_').replace(' ','_').replace('(','').replace(')','')
    d=names[i].replace('CDL','').lower()
    print('def {}():'.format(k))
    print('    {}=ta.{}()'.format(d,names[i]))
    print('    return {}'.format(d))






def Bollinger_Bands(close, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0):
    upperband, middleband, lowerband=ta.BBANDS(close, timeperiod, nbdevup, nbdevdn, matype)
    return upperband, middleband, lowerband
def Double_Exponential_Moving_Average(close, timeperiod=30):
    dema=ta.DEMA(close, timeperiod)
    return dema
def Exponential_Moving_Average(close, timeperiod=30):
    ema=ta.EMA(close, timeperiod)
    return ema
def Hilbert_Transform___Instantaneous_Trendline(close):
    ht_trendline=ta.HT_TRENDLINE(close)
    return ht_trendline
def Kaufman_Adaptive_Moving_Average(close, timeperiod=30):
    kama=ta.KAMA(close,timeperiod)
    return kama
def Moving_average(close, timeperiod=30, matype=0):
    ma=ta.MA(close, timeperiod, matype)
    return ma
def MESA_Adaptive_Moving_Average(close, fastlimit=0, slowlimit=0):
    mama, fama =ta.MAMA(close, fastlimit, slowlimit)
    return mama, fama 
def Moving_average_with_variable_period(close, periods, minperiod=2, maxperiod=30, matype=0):
    mavp=ta.MAVP(close, periods, minperiod, maxperiod, matype)
    return mavp
def MidPoint_over_period(close, timeperiod=14):
    midpoint=ta.MIDPOINT(close, timeperiod)
    return midpoint
def Midpoint_Price_over_period(high, low, timeperiod=14):
    midprice=ta.MIDPRICE(high, low, timeperiod)
    return midprice
def Parabolic_SAR(high, low, acceleration=0, maximum=0):
    sar=ta.SAR(high, low, acceleration, maximum)
    return sar
def Parabolic_SAR___Extended(high, low, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0):
    sarext=ta.SAREXT(high, low, startvalue, offsetonreverse, accelerationinitlong, accelerationlong, accelerationmaxlong, accelerationinitshort, accelerationshort, accelerationmaxshort)
    return sarext
def Simple_Moving_Average(close, timeperiod=30):
    sma=ta.SMA(close, timeperiod)
    return sma
def Triple_Exponential_Moving_Average_T3(close, timeperiod=5, vfactor=0):
    t3=ta.T3(close, timeperiod, vfactor)
    return t3
def Triple_Exponential_Moving_Average(close, timeperiod=30):
    tema=ta.TEMA(close, timeperiod)
    return tema
def Triangular_Moving_Average(close, timeperiod=30):
    trima=ta.TRIMA(close, timeperiod)
    return trima
def Weighted_Moving_Average(close, timeperiod=30):
    wma=ta.WMA(close, timeperiod)
    return wma
'''


'''
BBANDS
DEMA
EMA
HT_TRENDLINE
KAMA
MA
MAMA
MAVP
MIDPOINT
MIDPRICE
SAR
SAREXT
SMA
T3
TEMA
TRIMA
WMA


Bollinger Bands
Double Exponential Moving Average
Exponential Moving Average
Hilbert Transform - Instantaneous Trendline
Kaufman Adaptive Moving Average
Moving average
MESA Adaptive Moving Average
Moving average with variable period
MidPoint over period
Midpoint Price over period
Parabolic SAR
Parabolic SAR - Extended
Simple Moving Average
Triple Exponential Moving Average (T3)
Triple Exponential Moving Average
Triangular Moving Average
Weighted Moving Average
'''










'''
BBANDS               Bollinger Bands
DEMA                 Double Exponential Moving Average
EMA                  Exponential Moving Average
HT_TRENDLINE         Hilbert Transform - Instantaneous Trendline
KAMA                 Kaufman Adaptive Moving Average
MA                   Moving average
MAMA                 MESA Adaptive Moving Average
MAVP                 Moving average with variable period
MIDPOINT             MidPoint over period
MIDPRICE             Midpoint Price over period
SAR                  Parabolic SAR
SAREXT               Parabolic SAR - Extended
SMA                  Simple Moving Average
T3                   Triple Exponential Moving Average (T3)
TEMA                 Triple Exponential Moving Average
TRIMA                Triangular Moving Average
WMA                  Weighted Moving Average
'''
#deletehistoricaldatamanager()
'''function=[
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
#print(len(names),len(function))
'''
'''for i in range(0,60):
    k=function[i].replace('/','').replace('-','_').replace(' ','_')
    d=names[i].replace('CDL','').lower()
    print('def {}(open,high,low,close):\n'.format(k))
    print('    {}=ta.{}(open,high,low,close)\n'.format(d,names[i]))
    print('    return {}'.format(d))'''
'''
def Two_Crows(open,high,low,close):

    2crows=ta.CDL2CROWS(open,high,low,close)

    return 2crows
def Three_Black_Crows(open,high,low,close):

    3blackcrows=ta.CDL3BLACKCROWS(open,high,low,close)

    return 3blackcrows
def Three_Inside_UpDown(open,high,low,close):

    3inside=ta.CDL3INSIDE(open,high,low,close)

    return 3inside
def Three_Line_Strike(open,high,low,close):

    3linestrike=ta.CDL3LINESTRIKE(open,high,low,close)

    return 3linestrike
def Three_Outside_UpDown(open,high,low,close):

    3outside=ta.CDL3OUTSIDE(open,high,low,close)

    return 3outside
def Three_Stars_In_The_South(open,high,low,close):

    3starsinsouth=ta.CDL3STARSINSOUTH(open,high,low,close)

    return 3starsinsouth
def Three_Advancing_White_Soldiers(open,high,low,close):

    3whitesoldiers=ta.CDL3WHITESOLDIERS(open,high,low,close)

    return 3whitesoldiers
def Abandoned_Baby(open,high,low,close):

    abandonedbaby=ta.CDLABANDONEDBABY(open,high,low,close)

    return abandonedbaby
def Advance_Block(open,high,low,close):

    advanceblock=ta.CDLADVANCEBLOCK(open,high,low,close)

    return advanceblock
def Belt_hold(open,high,low,close):

    belthold=ta.CDLBELTHOLD(open,high,low,close)

    return belthold
def Breakaway(open,high,low,close):

    breakaway=ta.CDLBREAKAWAY(open,high,low,close)

    return breakaway
def Closing_Marubozu(open,high,low,close):

    closingmarubozu=ta.CDLCLOSINGMARUBOZU(open,high,low,close)

    return closingmarubozu
def Concealing_Baby_Swallow(open,high,low,close):

    concealbabyswall=ta.CDLCONCEALBABYSWALL(open,high,low,close)

    return concealbabyswall
def Counterattack(open,high,low,close):

    counterattack=ta.CDLCOUNTERATTACK(open,high,low,close)

    return counterattack
def Dark_Cloud_Cover(open,high,low,close):

    darkcloudcover=ta.CDLDARKCLOUDCOVER(open,high,low,close)

    return darkcloudcover
def Doji(open,high,low,close):

    doji=ta.CDLDOJI(open,high,low,close)

    return doji
def Doji_Star(open,high,low,close):

    dojistar=ta.CDLDOJISTAR(open,high,low,close)

    return dojistar
def Dragonfly_Doji(open,high,low,close):

    dragonflydoji=ta.CDLDRAGONFLYDOJI(open,high,low,close)

    return dragonflydoji
def Engulfing_Pattern(open,high,low,close):

    engulfing=ta.CDLENGULFING(open,high,low,close)

    return engulfing
def Evening_Doji_Star(open,high,low,close):

    eveningdojistar=ta.CDLEVENINGDOJISTAR(open,high,low,close)

    return eveningdojistar
def Evening_Star(open,high,low,close):

    eveningstar=ta.CDLEVENINGSTAR(open,high,low,close)

    return eveningstar
def UpDown_gap_side_by_side_white_lines(open,high,low,close):

    gapsidesidewhite=ta.CDLGAPSIDESIDEWHITE(open,high,low,close)

    return gapsidesidewhite
def Gravestone_Doji(open,high,low,close):

    gravestonedoji=ta.CDLGRAVESTONEDOJI(open,high,low,close)

    return gravestonedoji
def Hammer(open,high,low,close):

    hammer=ta.CDLHAMMER(open,high,low,close)

    return hammer
def Hanging_Man(open,high,low,close):

    hangingman=ta.CDLHANGINGMAN(open,high,low,close)

    return hangingman
def Harami_Pattern(open,high,low,close):

    harami=ta.CDLHARAMI(open,high,low,close)

    return harami
def Harami_Cross_Pattern(open,high,low,close):

    haramicross=ta.CDLHARAMICROSS(open,high,low,close)

    return haramicross
def High_Wave_Candle(open,high,low,close):

    highwave=ta.CDLHIGHWAVE(open,high,low,close)

    return highwave
def Hikkake_Pattern(open,high,low,close):

    hikkake=ta.CDLHIKKAKE(open,high,low,close)

    return hikkake
def Modified_Hikkake_Pattern(open,high,low,close):

    hikkakemod=ta.CDLHIKKAKEMOD(open,high,low,close)

    return hikkakemod
def Homing_Pigeon(open,high,low,close):

    homingpigeon=ta.CDLHOMINGPIGEON(open,high,low,close)

    return homingpigeon
def Identical_Three_Crows(open,high,low,close):

    identical3crows=ta.CDLIDENTICAL3CROWS(open,high,low,close)

    return identical3crows
def In_Neck_Pattern(open,high,low,close):

    inneck=ta.CDLINNECK(open,high,low,close)

    return inneck
def Inverted_Hammer(open,high,low,close):

    invertedhammer=ta.CDLINVERTEDHAMMER(open,high,low,close)

    return invertedhammer
def Kicking(open,high,low,close):

    kicking=ta.CDLKICKING(open,high,low,close)

    return kicking
def Kicking___bullbear(open,high,low,close):

    kickingbylength=ta.CDLKICKINGBYLENGTH(open,high,low,close)

    return kickingbylength
def Ladder_Bottom(open,high,low,close):

    ladderbottom=ta.CDLLADDERBOTTOM(open,high,low,close)

    return ladderbottom
def Long_Legged_Doji(open,high,low,close):

    longleggeddoji=ta.CDLLONGLEGGEDDOJI(open,high,low,close)

    return longleggeddoji
def Long_Line_Candle(open,high,low,close):

    longline=ta.CDLLONGLINE(open,high,low,close)

    return longline
def Marubozu(open,high,low,close):

    marubozu=ta.CDLMARUBOZU(open,high,low,close)

    return marubozu
def Matching_Low(open,high,low,close):

    matchinglow=ta.CDLMATCHINGLOW(open,high,low,close)

    return matchinglow
def Mat_Hold(open,high,low,close):

    mathold=ta.CDLMATHOLD(open,high,low,close)

    return mathold
def Morning_Doji_Star(open,high,low,close):

    morningdojistar=ta.CDLMORNINGDOJISTAR(open,high,low,close)

    return morningdojistar
def Morning_Star(open,high,low,close):

    morningstar=ta.CDLMORNINGSTAR(open,high,low,close)

    return morningstar
def On_Neck_Pattern(open,high,low,close):

    onneck=ta.CDLONNECK(open,high,low,close)

    return onneck
def Piercing_Pattern(open,high,low,close):

    piercing=ta.CDLPIERCING(open,high,low,close)

    return piercing
def Rickshaw_Man(open,high,low,close):

    rickshawman=ta.CDLRICKSHAWMAN(open,high,low,close)

    return rickshawman
def RisingFalling_Three_Methods(open,high,low,close):

    risefall3methods=ta.CDLRISEFALL3METHODS(open,high,low,close)

    return risefall3methods
def Separating_Lines(open,high,low,close):

    separatinglines=ta.CDLSEPARATINGLINES(open,high,low,close)

    return separatinglines
def Shooting_Star(open,high,low,close):

    shootingstar=ta.CDLSHOOTINGSTAR(open,high,low,close)

    return shootingstar
def Short_Line_Candle(open,high,low,close):

    shortline=ta.CDLSHORTLINE(open,high,low,close)

    return shortline
def Spinning_Top(open,high,low,close):

    spinningtop=ta.CDLSPINNINGTOP(open,high,low,close)

    return spinningtop
def Stalled_Pattern(open,high,low,close):

    stalledpattern=ta.CDLSTALLEDPATTERN(open,high,low,close)

    return stalledpattern
def Stick_Sandwich(open,high,low,close):

    sticksandwich=ta.CDLSTICKSANDWICH(open,high,low,close)

    return sticksandwich
def Takuri(open,high,low,close):

    takuri=ta.CDLTAKURI(open,high,low,close)

    return takuri
def Tasuki_Gap(open,high,low,close):

    tasukigap=ta.CDLTASUKIGAP(open,high,low,close)

    return tasukigap
def Thrusting_Pattern(open,high,low,close):

    thrusting=ta.CDLTHRUSTING(open,high,low,close)

    return thrusting
def Tristar_Pattern(open,high,low,close):

    tristar=ta.CDLTRISTAR(open,high,low,close)

    return tristar
def Unique_3_River(open,high,low,close):

    unique3river=ta.CDLUNIQUE3RIVER(open,high,low,close)

    return unique3river
def Upside_Gap_Two_Crows(open,high,low,close):

    upsidegap2crows=ta.CDLUPSIDEGAP2CROWS(open,high,low,close)

    return upsidegap2crows
'''

'''
Two Crows
Three Black Crows
Three Inside Up/Down
Three-Line Strike
Three Outside Up/Down
Three Stars In The South
Three Advancing White Soldiers
Abandoned Baby
Advance Block
Belt-hold
Breakaway
Closing Marubozu
Concealing Baby Swallow
Counterattack
Dark Cloud Cover
Doji
Doji Star
Dragonfly Doji
Engulfing Pattern
Evening Doji Star
Evening Star
Up/Down-gap side-by-side white lines
Gravestone Doji
Hammer
Hanging Man
Harami Pattern
Harami Cross Pattern
High-Wave Candle
Hikkake Pattern
Modified Hikkake Pattern
Homing Pigeon
Identical Three Crows
In-Neck Pattern
Inverted Hammer
Kicking
Kicking - bull/bear
Ladder Bottom
Long Legged Doji
Long Line Candle
Marubozu
Matching Low
Mat Hold
Morning Doji Star
Morning Star
On-Neck Pattern
Piercing Pattern
Rickshaw Man
Rising/Falling Three Methods
Separating Lines
Shooting Star
Short Line Candle
Spinning Top
Stalled Pattern
Stick Sandwich
Takuri
Tasuki Gap
Thrusting Pattern
Tristar Pattern
Unique 3 River
Upside Gap Two Crows
Upside/Downside Gap Three Methods
''' 


'''
Overlap_Studies

BBANDS
DEMA
EMA
HT_TRENDLINE
KAMA
MA
MAMA
MAVP
MIDPOINT
MIDPRICE
SAR
SAREXT
SMA
T3
TEMA
TRIMA
WMA


Momentum Indicators

ADX
ADXR
APO
AROON
AROONOSC
BOP
CCI
CMO
DX
MACD
MACDEXT
MACDFIX
MFI
MINUS_DI
MINUS_DM
MOM
PLUS_DI
PLUS_DM
PPO
ROC
ROCP
ROCR
ROCR100
RSI
STOCH
STOCHF
STOCHRSI
TRIX
ULTOSC
WILLR


Volume Indicators

AD
ADOSC
OBV


Volatility Indicators

ATR
NATR
TRANGE

Price Transform

AVGPRICE
MEDPRICE
TYPPRICE
WCLPRICE


Cycle Indicators

HT_DCPERIOD
HT_DCPHASE
HT_PHASOR
HT_SINE
HT_TRENDMODE




Pattern Recognition

CDL2CROWS
CDL3BLACKCROWS
CDL3INSIDE
CDL3LINESTRIKE
CDL3OUTSIDE
CDL3STARSINSOUTH
CDL3WHITESOLDIERS
CDLABANDONEDBABY
CDLADVANCEBLOCK
CDLBELTHOLD
CDLBREAKAWAY
CDLCLOSINGMARUBOZU
CDLCONCEALBABYSWALL
CDLCOUNTERATTACK
CDLDARKCLOUDCOVER
CDLDOJI
CDLDOJISTAR
CDLDRAGONFLYDOJI
CDLENGULFING
CDLEVENINGDOJISTAR
CDLEVENINGSTAR
CDLGAPSIDESIDEWHITE
CDLGRAVESTONEDOJI
CDLHAMMER
CDLHANGINGMAN
CDLHARAMI
CDLHARAMICROSS
CDLHIGHWAVE
CDLHIKKAKE
CDLHIKKAKEMOD
CDLHOMINGPIGEON
CDLIDENTICAL3CROWS
CDLINNECK
CDLINVERTEDHAMMER
CDLKICKING
CDLKICKINGBYLENGTH
CDLLADDERBOTTOM
CDLLONGLEGGEDDOJI
CDLLONGLINE
CDLMARUBOZU
CDLMATCHINGLOW
CDLMATHOLD
CDLMORNINGDOJISTAR
CDLMORNINGSTAR
CDLONNECK
CDLPIERCING
CDLRICKSHAWMAN
CDLRISEFALL3METHODS
CDLSEPARATINGLINES
CDLSHOOTINGSTAR
CDLSHORTLINE
CDLSPINNINGTOP
CDLSTALLEDPATTERN
CDLSTICKSANDWICH
CDLTAKURI
CDLTASUKIGAP
CDLTHRUSTING
CDLTRISTAR
CDLUNIQUE3RIVER
CDLUPSIDEGAP2CROWS
CDLXSIDEGAP3METHODS



Statistic Functions

BETA
CORREL
LINEARREG
LINEARREG_ANGLE
LINEARREG_INTERCEPT
LINEARREG_SLOPE
STDDEV
TSF
VAR

'''





'''
Overlap Studies


BBANDS
DEMA
EMA
HT_TRENDLINE
KAMA
MA
MAMA
MAVP
MIDPOINT
MIDPRICE
SAR
SAREXT
SMA
T3
TEMA
TRIMA
WMA


Momentum Indicators

ADX
ADXR
APO
AROON
AROONOSC
BOP
CCI
CMO
DX
MACD
MACDEXT
MACDFIX
MFI
MINUS_DI
MINUS_DM
MOM
PLUS_DI
PLUS_DM
PPO
ROC
ROCP
ROCR
ROCR100
RSI
STOCH
STOCHF
STOCHRSI
TRIX
ULTOSC
WILLR


Volume Indicators

AD
ADOSC
OBV


Volatility Indicators

ATR
NATR
TRANGE

Price Transform

AVGPRICE
MEDPRICE
TYPPRICE
WCLPRICE


Cycle Indicators

HT_DCPERIOD
HT_DCPHASE
HT_PHASOR
HT_SINE
HT_TRENDMODE




Pattern Recognition

CDL2CROWS
CDL3BLACKCROWS
CDL3INSIDE
CDL3LINESTRIKE
CDL3OUTSIDE
CDL3STARSINSOUTH
CDL3WHITESOLDIERS
CDLABANDONEDBABY
CDLADVANCEBLOCK
CDLBELTHOLD
CDLBREAKAWAY
CDLCLOSINGMARUBOZU
CDLCONCEALBABYSWALL
CDLCOUNTERATTACK
CDLDARKCLOUDCOVER
CDLDOJI
CDLDOJISTAR
CDLDRAGONFLYDOJI
CDLENGULFING
CDLEVENINGDOJISTAR
CDLEVENINGSTAR
CDLGAPSIDESIDEWHITE
CDLGRAVESTONEDOJI
CDLHAMMER
CDLHANGINGMAN
CDLHARAMI
CDLHARAMICROSS
CDLHIGHWAVE
CDLHIKKAKE
CDLHIKKAKEMOD
CDLHOMINGPIGEON
CDLIDENTICAL3CROWS
CDLINNECK
CDLINVERTEDHAMMER
CDLKICKING
CDLKICKINGBYLENGTH
CDLLADDERBOTTOM
CDLLONGLEGGEDDOJI
CDLLONGLINE
CDLMARUBOZU
CDLMATCHINGLOW
CDLMATHOLD
CDLMORNINGDOJISTAR
CDLMORNINGSTAR
CDLONNECK
CDLPIERCING
CDLRICKSHAWMAN
CDLRISEFALL3METHODS
CDLSEPARATINGLINES
CDLSHOOTINGSTAR
CDLSHORTLINE
CDLSPINNINGTOP
CDLSTALLEDPATTERN
CDLSTICKSANDWICH
CDLTAKURI
CDLTASUKIGAP
CDLTHRUSTING
CDLTRISTAR
CDLUNIQUE3RIVER
CDLUPSIDEGAP2CROWS
CDLXSIDEGAP3METHODS



Statistic Functions

BETA
CORREL
LINEARREG
LINEARREG_ANGLE
LINEARREG_INTERCEPT
LINEARREG_SLOPE
STDDEV
TSF
VAR

'''






#closedorders=exchange.private_get_position()
#print(closedorders)
'''
tf=['1m','5m','1h','1d','2h','15m','4h','12h']
def timeframelimitrange(time):
    if time == '1m':
        time=1440
    elif time == '5m':
        time=288
    elif time == '15m':
        time=96
    elif time == '30m':
        time=48
    elif time == '1h':
        time=24
    elif time == '2h':
        time=12
    elif time=='4h':
        time=6
    elif time == '12h':
        time=2
    elif time == '1d':
        time=1
    return time

historicsymbols=['BTC/USDT','ETH/USDT']
for symbol in historicsymbols:
    for time in tf:
        coin='{}{}'.format(symbol,time).replace('/','')
        if coin in db.list_collection_names():
            data=list(db[coin].find().sort('_id',pymongo.ASCENDING).limit(timeframelimitrange(time)))
            #pprint(data)
            #k=db[coin].create_index([('Timestamp',pymongo.ASCENDING)],unique=True )
            #print(k)
            df=pd.DataFrame(data)
            #print(coin)
            #print(df.tail())
            df.to_csv('{}.csv'.format(coin))
'''






































'''


def StrategyExecutor(btcusdt):
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



    if riskmanagement == 'Trailing Stop':
        trailingStoploss(symbol,side,riskpercent,amount)
    elif riskmanagement == 'Stop Loss':
        if type == 'Market':
            Stoploss(symbol,side,riskpercent,amount)
        elif type == 'Limit':
            Limit_Stoploss(symbol,side,riskpercent,qty,price)
        else:
            print('Error in riskmanagement')
    elif riskmanagement == 'Take Profit':
        if type == 'Market':
            take_profit(symbol,side,riskpercent,amount)
        elif type == 'Limit':
            Limit_take_profit(symbol,side,riskpercent,qty,price)
        else:
            print('Error in riskmanagement')
    else:
        print('None of Risk Management')
'''
'''
symbol='BTC/USD'
types='Stop'
side='buy'
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

r=pricepercent(symbol,5)
print(r)

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
#riskmanager(symbol)

#p=trailingStoploss(symbol,side)
#print(p)
#time.sleep(10)
#p=exchange.cancel_order(p['info']['orderID'])
#pprint(balance())

#pprint(p)
#Trade_Management(exchange)
#p=list(db.position.find({'symbol':'XBTUSD'}).sort("_id", pymongo.DESCENDING).limit(1))

#pprint(p[0]['isOpen'])
r={'filter': json.dumps({'open':'true'
    })}
'''



'''p=exchange.fetch_open_orders()
print(p)
listing=[]
for i in p:
    listing.append(i['symbol'])
print(listing)
'''
'''
amount=percent(1)
percent=5
k=pricepercent(symbol,percent)
print(k)
data=take_profit(symbol,side,percent,amount)
#data=trailingStoploss(symbol,side,percent,amount)
riskmanager(symbol)
symbol='ETH/USD'
data=trailingStoploss(symbol,side,percent,amount)
riskmanager(symbol)
print(data)
'''

'''
for i,k in data['info'].items():
    #print(i)
    print("'{}':data['info']['{}'],".format(i,i))
#print('hi')
for i,k in data.items():
    #print(i)
    print("'{}':data['{}'],".format(i,i))
'''

'''
post={
'date':datetime.datetime.now(),
'orderID':data['info']['orderID'],
'clOrdID':data['info']['clOrdID'],
'clOrdLinkID':data['info']['clOrdLinkID'],
'account':data['info']['account'],
'symbol':data['info']['symbol'],
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
post1=db.riskmanager.insert_one(post).inserted_id
print(post1)
data1=exchange.private_get_position({'filter': json.dumps({"isOpen": True})})
pprint(data1)
if symbol == 'ETH/USD':
    symbol='ETHUSD'
elif symbol == 'BTC/USD':
    symbol = 'XBTUSD'
else:
    print('Error Ocurred')

if 'riskmanager' in db.list_collection_names():
    print(True)
    if data1:
        for data2 in data1:
            if symbol == data2['symbol']:
                order = list(db.riskmanager.find({'symbol':symbol}).sort("_id", pymongo.DESCENDING).limit(1))
                orderid=order[0]['orderID']
                data=exchange.cancel_order(orderid)
                print(p)
                print(data['symbol'])
                post={
'date':datetime.datetime.now(),
'orderID':data['info']['orderID'],
'clOrdID':data['info']['clOrdID'],
'clOrdLinkID':data['info']['clOrdLinkID'],
'account':data['info']['account'],
'symbol':data['info']['symbol'],
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

    if not data1:
        order = list(db.riskmanager.find({'symbol':symbol}).sort("_id", pymongo.DESCENDING).limit(1))
        orderid=order[0]['orderID']
        p=exchange.cancel_order(orderid)
        print(p)
'''

#data1=exchange.fetch_open_orders({'filter': json.dumps({"symbol": 'XBTUSD'})})
#data1=exchange.fetch_open_orders()
#print(data1)
'''listed=[]
if data1:
    for data in data1:
        if symbol == data['symbol']:
            listed=listed.append([symbol])
            print(listed,True)
'''

#symbol='ETHUSD'

'''
for check in position:
    print(check['symbol'])
    if symbol == check['symbol']:
        for data in data1:
            #if symbol == data['symbol']:
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
'''










'''
def newTrade_Management(exchange):
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
                'lastValue':data['lastValue']}

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
                'lastValue':data['lastValue']} }
        
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

'''







#btcusdt=list(db.btcusdt.find().sort("date", pymongo.DESCENDING).limit(1))
'''btcusdt=db.btcusdt.find_one(sort=[('date', pymongo.DESCENDING)])
btc=list(db.btcusdt.find())[-1]
#print(btc)
options = ['1_Min_ALL','1_Min_MA','1_Min_Osillator','5_Min_ALL','5_Min_MA','5_Min_Osillator','15_Min_ALL','15_Min_MA','15_Min_Osillator','60_Min_ALL','60_Min_MA','60_Min_Osillator','240_Min_ALL','240_Min_MA','240_Min_Osillator','1_Day_ALL','1_Day_MA','1_Day_Osillator','1_Week_ALL','1_Week_MA','1_Week_Osillator','1_Month_ALL','1_Month_MA','1_Month_Osillator']
#print(btcusdt)
btcusdt=list(db.BTCUSD1h.find().sort("_id", pymongo.DESCENDING).limit(100))[::-1]
#btcusdt=btcusdt.reverse()
print(btcusdt)
df=pd.DataFrame(btcusdt)

df['highest'] = df['Close'].cummax()
df['trailingstop'] = df['highest']*0.99
df['exit_signal'] = df['Close'] < df['trailingstop']
print(df)
'''
'''#for k,d in btcusdt.items(): 
    #print("elif signal=='{}' :\n    d=' '".format(k))
    #print("d='{}'".format(k))
'''
'''
def StrategyExecutor(btcusdt):
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

btcusdt=list(db.btcusdt.find())[-1]
ethusdt=list(db.ethusdt.find())[-1]


while True:
    StrategyExecutor(btcusdt)
    StrategyExecutor(ethusdt)
    time.sleep(10)
'''





































'''


def MultiDecisionMaker(btctvsignal1=btcusdt['recommendall1'],btctvsignal5=btcusdt['recommendall5'],btctvsignal15=btcusdt['recommendall15'],amount=percentage('BTC/USD',100),symbol='BTC/USD'):
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


while True:
    MultiDecisionMaker()
    time.sleep(5)

'''


















































































'''from database import db
from actions import *
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
    if check:
        if btctvsignal1 > 0 and btctvsignal5 > 0 and btctvsignal15 > 0 :
            if today_sentiment() == 'POSITIVE':
                if webhook['side'] == 'buy' and webhook['auto'] == True:
                    Decision="Long Entry"
                    send_order(post1)
                    time.sleep(3)
                    Trade_Management(exchange)
                #break
        elif  btctvsignal1 < 0 and btctvsignal5 < 0 and btctvsignal15 < 0 :
            if today_sentiment() == 'POSITIVE':
                if webhook['side'] == 'sell' and webhook['auto'] == True:
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
                        if webhook['side'] == 'sell' and webhook['auto'] == True:
                            Decision="Long Exit"
                            post2={'type': 'market', 'side': 'sell', 'amount': abs(currentqty), 'symbol': symbol, 'price': None, 'key': '99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319'}
        
                            send_order(post2)
                            time.sleep(3)
                            Trade_Management(exchange)
                #break
            elif check_currentqty < 0:
                if btctvsignal1 > 0 and btctvsignal5 > 0 and btctvsignal15 > 0 :
                    if today_sentiment() == 'POSITIVE':
                        if webhook['side'] == 'buy' and webhook['auto'] == True:
                            Decision="Short Exit"
                            post1={'type': 'market', 'side': 'buy', 'amount': abs(currentqty), 'symbol': symbol, 'price': None, 'key': '99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319'}
        
                            send_order(post1)
                            time.sleep(3)
                            Trade_Management(exchange)
            Trade_Management(exchange)
            return print('{} {} {}'.format(symbol,post1['type'],Decision))  
    #time.sleep(5)
    return print('OK')
'''