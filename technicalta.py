from database import db 
import pymongo
import numpy as np
import pandas as pd
import talib  as ta
from pprint import pprint
from technical import qtpylib
listof3=['Bollinger Bands','Moving Average Convergence-Divergence Fix','Moving Average Convergence-Divergence']

listof2=['Aroon','MESA Adaptive Moving Average','Stochastic','Stochastic Fast','Stochastic Relative Strength Index']

listof1=[
'Double Exponential Moving Average',
'Exponential Moving Average',
'Hilbert Transform - Instantaneous Trendline',
'Kaufman Adaptive Moving Average',
'Moving average',
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
'Aroon Oscillator',
'Balance Of Power',
'Commodity Channel Index',
'Chande Momentum Oscillator',
'Directional Movement Index',
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

#oscillator
def Moving_Average_Convergence_Divergence(close, fastperiod=12, slowperiod=26, signalperiod=9):
    macd, macdsignal, macdhist=ta.MACD(close, fastperiod, slowperiod, signalperiod)
    return macd, macdsignal, macdhist
def MACD_with_controllable_MA_type(close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0):
    macd, macdsignal, macdhist=ta.MACDEXT(close, fastperiod, fastmatype, slowperiod, slowmatype, signalperiod, signalmatype)
    return macd, macdsignal, macdhist
def Moving_Average_Convergence_Divergence_Fix(close, signalperiod=9):
    macd, macdsignal, macdhis=ta.MACDFIX(close, signalperiod)
    return macd, macdsignal, macdhis


#movingaverges 
def Bollinger_Bands(close, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0):
    upperband, middleband, lowerband=ta.BBANDS(close, timeperiod, nbdevup, nbdevdn, matype)
    return upperband, middleband, lowerband
#listof3=['Bollinger_Bands','Moving_Average_Convergence_Divergence_Fix','MACD_with_controllable_MA_type','Moving_Average_Convergence_Divergence']

#listof2=['Aroon','MESA_Adaptive_Moving_Average','Stochastic','Stochastic_Fast','Stochastic_Relative_Strength_Index']

#Movingaverages
def MESA_Adaptive_Moving_Average(close, fastlimit=0, slowlimit=0):
    mama, fama =ta.MAMA(close, fastlimit, slowlimit)
    return mama, fama 


#osillator
def Stochastic(high, low, close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0):
    slowk, slowd=ta.STOCH(high, low, close, fastk_period, slowk_period, slowk_matype, slowd_period, slowd_matype)
    return slowk, slowd
def Stochastic_Fast(high, low, close, fastk_period=5, fastd_period=3, fastd_matype=0):
    fastk, fastd=ta.STOCHF(high, low, close, fastk_period, fastd_period, fastd_matype)
    return fastk, fastd
def Stochastic_Relative_Strength_Index(close, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0):
    fastk, fastd=ta.STOCHRSI(close, timeperiod, fastk_period, fastd_period, fastd_matype)
    return fastk, fastd
def Aroon(high, low, timeperiod=14):
    aroondown, aroonup=ta.AROON(high, low, timeperiod)
    return aroondown, aroonup



#moving averages
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



#osicllator
def Average_Directional_Movement_Index(high, low, close, timeperiod=14):
    adx=ta.ADX(high, low, close, timeperiod)
    return adx
def Average_Directional_Movement_Index_Rating(high, low, close, timeperiod=14):
    adxr=ta.ADXR(high, low, close, timeperiod)
    return adxr
def Absolute_Price_Oscillator(close, fastperiod=12, slowperiod=26, matype=0):
    apo=ta.APO(close, fastperiod, slowperiod, matype)
    return apo

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

def one_day_Rate_Of_Change_ROC_of_a_Triple_Smooth_EMA(close, timeperiod=30):
    trix=ta.TRIX(close, timeperiod)
    return trix
def Ultimate_Oscillator(high, low, close, timeperiod1=7, timeperiod2=14, timeperiod3=28):
    ultosc=ta.ULTOSC(high, low, close, timeperiod1, timeperiod2, timeperiod3)
    return ultosc
def Williams(high, low, close, timeperiod=14):
    willr=ta.WILLR(high, low, close, timeperiod)
    return willr
def Chaikin_AD_Line(high, low, close, volume):
    ad=ta.AD(high, low, close, volume)
    return ad
def Chaikin_AD_Oscillator(high, low, close, volume, fastperiod=3, slowperiod=10):
    adosc=ta.ADOSC(high, low, close, volume, fastperiod, slowperiod)
    return adosc
def On_Balance_Volume(close, volume):
    obv=ta.OBV(close, volume)
    return obv






















def Two_Crows(open,high,low,close):

    crows=ta.CDL2CROWS(open,high,low,close)

    return crows
def Three_Black_Crows(open,high,low,close):

    blackcrows=ta.CDL3BLACKCROWS(open,high,low,close)

    return blackcrows
def Three_Inside_UpDown(open,high,low,close):

    inside=ta.CDL3INSIDE(open,high,low,close)

    return inside
def Three_Line_Strike(open,high,low,close):

    linestrike=ta.CDL3LINESTRIKE(open,high,low,close)

    return linestrike
def Three_Outside_UpDown(open,high,low,close):

    outside=ta.CDL3OUTSIDE(open,high,low,close)

    return outside
def Three_Stars_In_The_South(open,high,low,close):

    starsinsouth=ta.CDL3STARSINSOUTH(open,high,low,close)

    return starsinsouth
def Three_Advancing_White_Soldiers(open,high,low,close):

    whitesoldiers=ta.CDL3WHITESOLDIERS(open,high,low,close)

    return whitesoldiers
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
def UpsideDownside_Gap_Three_Methods(open,high,low,close):

    upsidegap2crows=ta.CDLXSIDEGAP3METHODS(open,high,low,close)

    return upsidegap2crows

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

def technicalselector(technical,df):
    open=df['Open']
    close=df['Close']
    high=df['High']
    low=df['Low']
    volume=df['Volume']
    if technical == 'Chaikin_AD_Line':
        tech=Chaikin_AD_Line(high, low, close, volume)
    elif technical == 'Chaikin_AD_Oscillator':
        tech=Chaikin_AD_Oscillator(high, low, close, volume, fastperiod=3, slowperiod=10)
    elif technical == 'On_Balance_Volume':
        tech=On_Balance_Volume(close, volume)
    elif technical == 'Bollinger_Bands':
        tech=Bollinger_Bands(close, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
    elif technical == 'Double_Exponential_Moving_Average':
        tech=Double_Exponential_Moving_Average(close, timeperiod=30)
    elif technical == 'Exponential_Moving_Average':
        tech=Exponential_Moving_Average(close, timeperiod=30)
    elif technical == 'Hilbert_Transform___Instantaneous_Trendline':
        tech=Hilbert_Transform___Instantaneous_Trendline(close)
    elif technical == 'Kaufman_Adaptive_Moving_Average':
        tech=Kaufman_Adaptive_Moving_Average(close, timeperiod=30)
    elif technical == 'Moving_average':
        tech=Moving_average(close, timeperiod=30, matype=0)
    elif technical == 'MESA_Adaptive_Moving_Average':
        tech=MESA_Adaptive_Moving_Average(close, fastlimit=0.5, slowlimit=0.5)
    elif technical == 'Moving_average_with_variable_period':
        df['periods']=6
        periods=df['periods']
        tech=Moving_average_with_variable_period(close, periods, minperiod=2, maxperiod=30, matype=0)
    elif technical == 'MidPoint_over_period':
        tech=MidPoint_over_period(close, timeperiod=14)
    elif technical == 'Midpoint_Price_over_period':
        tech=Midpoint_Price_over_period(high, low, timeperiod=14)
    elif technical == 'Parabolic_SAR':
        tech=Parabolic_SAR(high, low, acceleration=0, maximum=0)
    elif technical == 'Parabolic_SAR___Extended':
        tech=Parabolic_SAR___Extended(high, low, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)
    elif technical == 'Simple_Moving_Average':
        tech=Simple_Moving_Average(close, timeperiod=30)
    elif technical == 'Triple_Exponential_Moving_Average_T3':
        tech=Triple_Exponential_Moving_Average_T3(close, timeperiod=5, vfactor=0)
    elif technical == 'Triple_Exponential_Moving_Average':
        tech=Triple_Exponential_Moving_Average(close, timeperiod=30)
    elif technical == 'Triangular_Moving_Average':
        tech=Triangular_Moving_Average(close, timeperiod=30)
    elif technical == 'Weighted_Moving_Average':
        tech=Weighted_Moving_Average(close, timeperiod=30)
    elif technical == 'Average_Directional_Movement_Index':
        tech=Average_Directional_Movement_Index(high, low, close, timeperiod=14)
    elif technical == 'Average_Directional_Movement_Index_Rating':
        tech=Average_Directional_Movement_Index_Rating(high, low, close, timeperiod=14)
    elif technical == 'Absolute_Price_Oscillator':
        tech=Absolute_Price_Oscillator(close, fastperiod=12, slowperiod=26, matype=0)
    elif technical == 'Aroon':
        tech=Aroon(high, low, timeperiod=14)
    elif technical == 'Aroon_Oscillator':
        tech=Aroon_Oscillator(high, low, timeperiod=14)
    elif technical == 'Balance_Of_Power':
        tech=Balance_Of_Power(open, high, low, close)
    elif technical == 'Commodity_Channel_Index':
        tech=Commodity_Channel_Index(high, low, close, timeperiod=14)
    elif technical == 'Chande_Momentum_Oscillator':
        tech=Chande_Momentum_Oscillator(close, timeperiod=14)
    elif technical == 'Directional_Movement_Index':
        tech=Directional_Movement_Index(high, low, close, timeperiod=14)
    elif technical == 'Moving_Average_Convergence_Divergence':
        tech=Moving_Average_Convergence_Divergence(close, fastperiod=12, slowperiod=26, signalperiod=9)
    elif technical == 'MACD_with_controllable_MA_type':
        tech=MACD_with_controllable_MA_type(close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
        print(tech)
    elif technical == 'Moving_Average_Convergence_Divergence_Fix':
        tech=Moving_Average_Convergence_Divergence_Fix(close, signalperiod=9)
    elif technical == 'Money_Flow_Index':
        tech=Money_Flow_Index(high, low, close, volume, timeperiod=14)
    elif technical == 'Minus_Directional_Indicator':
        tech=Minus_Directional_Indicator(high, low, close, timeperiod=14)
    elif technical == 'Minus_Directional_Movement':
        tech=Minus_Directional_Movement(high, low, timeperiod=14)
    elif technical == 'Momentum':
        tech=Momentum(close, timeperiod=10)
    elif technical == 'Plus_Directional_Indicator':
        tech=Plus_Directional_Indicator(high, low, close, timeperiod=14)
    elif technical == 'Plus_Directional_Movement':
        tech=Plus_Directional_Movement(high, low, timeperiod=14)
    elif technical == 'Percentage_Price_Oscillator':
        tech=Percentage_Price_Oscillator(close, fastperiod=12, slowperiod=26, matype=0)
    elif technical == 'Rate_of_change':
        tech=Rate_of_change(close, timeperiod=10)
    elif technical == 'Rate_of_change_Percentage':
        tech=Rate_of_change_Percentage(close, timeperiod=10)
    elif technical == 'Rate_of_change_ratio':
        tech=Rate_of_change_ratio(close, timeperiod=10)
    elif technical == 'Rate_of_change_ratio_100_scale':
        tech=Rate_of_change_ratio_100_scale(close, timeperiod=10)
    elif technical == 'Relative_Strength_Index':
        tech=Relative_Strength_Index(close, timeperiod=14)
    elif technical == 'Stochastic':
        tech=Stochastic(high, low, close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    elif technical == 'Stochastic_Fast':
        tech=Stochastic_Fast(high, low, close, fastk_period=5, fastd_period=3, fastd_matype=0)
    elif technical == 'Stochastic_Relative_Strength_Index':
        tech=Stochastic_Relative_Strength_Index(close, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
    elif technical == 'one_day_Rate_Of_Change_ROC_of_a_Triple_Smooth_EMA':
        tech=one_day_Rate_Of_Change_ROC_of_a_Triple_Smooth_EMA(close, timeperiod=30)
    elif technical == 'Ultimate_Oscillator':
        tech=Ultimate_Oscillator(high, low, close, timeperiod1=7, timeperiod2=14, timeperiod3=28)
    elif technical == 'Williams':
        tech=Williams(high, low, close, timeperiod=14)
    elif technical == 'Two_Crows':
        tech=Two_Crows(open,high,low,close)
    elif technical == 'Three_Black_Crows':
        tech=Three_Black_Crows(open,high,low,close)
    elif technical == 'Three_Inside_UpDown':
        tech=Three_Inside_UpDown(open,high,low,close)
    elif technical == 'Three_Line_Strike':
        tech=Three_Line_Strike(open,high,low,close)
    elif technical == 'Three_Outside_UpDown':
        tech=Three_Outside_UpDown(open,high,low,close)
    elif technical == 'Three_Stars_In_The_South':
        tech=Three_Stars_In_The_South(open,high,low,close)
    elif technical == 'Three_Advancing_White_Soldiers':
        tech=Three_Advancing_White_Soldiers(open,high,low,close)
    elif technical == 'Abandoned_Baby':
        tech=Abandoned_Baby(open,high,low,close)
    elif technical == 'Advance_Block':
        tech=Advance_Block(open,high,low,close)
    elif technical == 'Belt_hold':
        tech=Belt_hold(open,high,low,close)
    elif technical == 'Breakaway':
        tech=Breakaway(open,high,low,close)
    elif technical == 'Closing_Marubozu':
        tech=Closing_Marubozu(open,high,low,close)
    elif technical == 'Concealing_Baby_Swallow':
        tech=Concealing_Baby_Swallow(open,high,low,close)
    elif technical == 'Counterattack':
        tech=Counterattack(open,high,low,close)
    elif technical == 'Dark_Cloud_Cover':
        tech=Dark_Cloud_Cover(open,high,low,close)
    elif technical == 'Doji':
        tech=Doji(open,high,low,close)
    elif technical == 'Doji_Star':
        tech=Doji_Star(open,high,low,close)
    elif technical == 'Dragonfly_Doji':
        tech=Dragonfly_Doji(open,high,low,close)
    elif technical == 'Engulfing_Pattern':
        tech=Engulfing_Pattern(open,high,low,close)
    elif technical == 'Evening_Doji_Star':
        tech=Evening_Doji_Star(open,high,low,close)
    elif technical == 'Evening_Star':
        tech=Evening_Star(open,high,low,close)
    elif technical == 'UpDown_gap_side_by_side_white_lines':
        tech=UpDown_gap_side_by_side_white_lines(open,high,low,close)
    elif technical == 'Gravestone_Doji':
        tech=Gravestone_Doji(open,high,low,close)
    elif technical == 'Hammer':
        tech=Hammer(open,high,low,close)
    elif technical == 'Hanging_Man':
        tech=Hanging_Man(open,high,low,close)
    elif technical == 'Harami_Pattern':
        tech=Harami_Pattern(open,high,low,close)
    elif technical == 'Harami_Cross_Pattern':
        tech=Harami_Cross_Pattern(open,high,low,close)
    elif technical == 'High_Wave_Candle':
        tech=High_Wave_Candle(open,high,low,close)
    elif technical == 'Hikkake_Pattern':
        tech=Hikkake_Pattern(open,high,low,close)
    elif technical == 'Modified_Hikkake_Pattern':
        tech=Modified_Hikkake_Pattern(open,high,low,close)
    elif technical == 'Homing_Pigeon':
        tech=Homing_Pigeon(open,high,low,close)
    elif technical == 'Identical_Three_Crows':
        tech=Identical_Three_Crows(open,high,low,close)
    elif technical == 'In_Neck_Pattern':
        tech=In_Neck_Pattern(open,high,low,close)
    elif technical == 'Inverted_Hammer':
        tech=Inverted_Hammer(open,high,low,close)
    elif technical == 'Kicking':
        tech=Kicking(open,high,low,close)
    elif technical == 'Kicking___bullbear':
        tech=Kicking___bullbear(open,high,low,close)
    elif technical == 'Ladder_Bottom':
        tech=Ladder_Bottom(open,high,low,close)
    elif technical == 'Long_Legged_Doji':
        tech=Long_Legged_Doji(open,high,low,close)
    elif technical == 'Long_Line_Candle':
        tech=Long_Line_Candle(open,high,low,close)
    elif technical == 'Marubozu':
        tech=Marubozu(open,high,low,close)
    elif technical == 'Matching_Low':
        tech=Matching_Low(open,high,low,close)
    elif technical == 'Mat_Hold':
        tech=Mat_Hold(open,high,low,close)
    elif technical == 'Morning_Doji_Star':
        tech=Morning_Doji_Star(open,high,low,close)
    elif technical == 'Morning_Star':
        tech=Morning_Star(open,high,low,close)
    elif technical == 'On_Neck_Pattern':
        tech=On_Neck_Pattern(open,high,low,close)
    elif technical == 'Piercing_Pattern':
        tech=Piercing_Pattern(open,high,low,close)
    elif technical == 'Rickshaw_Man':
        tech=Rickshaw_Man(open,high,low,close)
    elif technical == 'RisingFalling_Three_Methods':
        tech=RisingFalling_Three_Methods(open,high,low,close)
    elif technical == 'Separating_Lines':
        tech=Separating_Lines(open,high,low,close)
    elif technical == 'Shooting_Star':
        tech=Shooting_Star(open,high,low,close)
    elif technical == 'Short_Line_Candle':
        tech=Short_Line_Candle(open,high,low,close)
    elif technical == 'Spinning_Top':
        tech=Spinning_Top(open,high,low,close)
    elif technical == 'Stalled_Pattern':
        tech=Stalled_Pattern(open,high,low,close)
    elif technical == 'Stick_Sandwich':
        tech=Stick_Sandwich(open,high,low,close)
    elif technical == 'Takuri':
        tech=Takuri(open,high,low,close)
    elif technical == 'Tasuki_Gap':
        tech=Tasuki_Gap(open,high,low,close)
    elif technical == 'Thrusting_Pattern':
        tech=Thrusting_Pattern(open,high,low,close)
    elif technical == 'Tristar_Pattern':
        tech=Tristar_Pattern(open,high,low,close)
    elif technical == 'Unique_3_River':
        tech=Unique_3_River(open,high,low,close)
    elif technical == 'Upside_Gap_Two_Crows':
        tech=Upside_Gap_Two_Crows(open,high,low,close)
    elif technical == 'UpsideDownside_Gap_Three_Methods':
        tech=UpsideDownside_Gap_Three_Methods(open,high,low,close)
    else:
        print('Error ocurred')
    return tech



def data_maker():
    chart=db.chart.find_one(sort=[('_id', pymongo.DESCENDING)])
    symbol=chart['symbols'].replace("/","")
    tf=chart['tf']
    coin="{}_{}".format(symbol,tf)
    candle=chart['candle']
    df=list(db[coin].find().sort('_id',pymongo.DESCENDING).limit(500))[::-1]
    df=pd.DataFrame(df)
    #pprint(df)
    if candle == 'Heikinashi':
        df['open']=df['Open']
        df['close']=df['Close']
        df['high']=df['High']
        df['low']=df['Low']
        h=qtpylib.heikinashi(df)
        df['Open']=h['open']
        df['High']=h['high']
        df['Low']=h['low']
        df['Close']=h['close']
        df=df.drop(columns=['open','low','high','close'])
        return df
    elif candle=='Renko':
        print('Error in Data Maker')
    elif candle=='candle':
        return df
        #print('Error in Data Maker')
    else:
        print('Error in Data Maker')
def texterconversion(text):
    tex=text.replace('/','').replace('-','_').replace(' ','_').replace('(','').replace(')','')
    return tex



def indicator_data_level_1():
    from technicalta import texterconversion,listof1,listof3,listof2,technicalselector
    chart=db.chart.find_one(sort=[('_id', pymongo.DESCENDING)])
    symbol=chart['symbols'].replace("/","")
    tf=chart['tf']
    coin="{}_{}".format(symbol,tf)
    indicator=chart['technical']
    #print(chart)
    df=data_maker()
    listof3=listof3
    listof2=listof2
    listof1=listof1
    listof3=[texterconversion(file) for file in listof3 ]
    listof2=[texterconversion(file) for file in listof2 ]
    listof1=[texterconversion(file) for file in listof1 ]
    names_indicator=list([texterconversion(file) for file in indicator if texterconversion(file) in listof1])
    data=list([list(technicalselector(file,df)) for file in names_indicator ])
    columns_names=list([texterconversion(file) for file in indicator if texterconversion(file) in listof1])
    df1=pd.DataFrame(data).transpose()
    df1.columns=columns_names
    df=df.join(df1)
    df.set_index("date", inplace = True)
    df=df.drop(columns=['_id','Open','Low','High','Volume','Close'])
    #pprint(df)
    return df
def indicator_data_level_2():
    from technicalta import texterconversion,listof1,listof3,listof2,technicalselector
    chart=db.chart.find_one(sort=[('_id', pymongo.DESCENDING)])
    symbol=chart['symbols'].replace("/","")
    tf=chart['tf']
    coin="{}_{}".format(symbol,tf)
    indicator=chart['technical']
    #print(chart)
    df=data_maker()
    listof3=listof3
    listof2=listof2
    listof1=listof1
    listof3=[texterconversion(file) for file in listof3 ]
    listof2=[texterconversion(file) for file in listof2 ]
    listof1=[texterconversion(file) for file in listof1 ]
    names_indicator=list([texterconversion(file) for file in indicator if texterconversion(file) in listof2])
    data=list([list(technicalselector(file,df)) for file in names_indicator ])
    columns_names=list([texterconversion(file) for file in indicator if texterconversion(file) in listof2])
    length=len(columns_names)
    for i in range(0,length):
        df1=pd.DataFrame(data[i]).transpose()
        df1.columns=["{}_0".format(columns_names[i]),"{}_1".format(columns_names[i])]
        #pprint(df1)
        df=df.join(df1)
    #pprint(df)
    df.set_index("date", inplace = True)
    df=df.drop(columns=['_id','Open','Low','High','Volume','Close'])
    #pprint(df)
    return df
def indicator_data_level_3():
    from technicalta import texterconversion,listof1,listof3,listof2,technicalselector
    chart=db.chart.find_one(sort=[('_id', pymongo.DESCENDING)])
    symbol=chart['symbols'].replace("/","")
    tf=chart['tf']
    coin="{}_{}".format(symbol,tf)
    indicator=chart['technical']
    #print(chart)
    df=data_maker()
    listof3=listof3
    listof2=listof2
    listof1=listof1
    listof3=[texterconversion(file) for file in listof3 ]
    listof2=[texterconversion(file) for file in listof2 ]
    listof1=[texterconversion(file) for file in listof1 ]
    names_indicator=list([texterconversion(file) for file in indicator if texterconversion(file) in listof3])
    data=list([list(technicalselector(file,df)) for file in names_indicator ])
    columns_names=list([texterconversion(file) for file in indicator if texterconversion(file) in listof3])
    #pprint(columns_names)
    length=len(columns_names)
    for i in range(0,length):
        df1=pd.DataFrame(data[i]).transpose()
        df1.columns=["{}_0".format(columns_names[i]),"{}_1".format(columns_names[i]),"{}_2".format(columns_names[i])]
        #pprint(df1)
        df=df.join(df1)
    #pprint(df)
    df.set_index("date", inplace = True)
    df=df.drop(columns=['_id','Open','Low','High','Volume','Close'])
    #pprint(df)
    return df

