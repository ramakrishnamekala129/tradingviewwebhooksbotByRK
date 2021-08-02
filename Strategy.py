from Gann_library import *



from database import db 
from pprint import pprint
Symbol='ETHUSDT'

def Gann_Targets(Symbol):
	Timeframe='1d'
	Input=db['{}_{}'.format(Symbol,Timeframe)].find_one(sort=[('_id', pymongo.DESCENDING)])
	#print(Input)
	X,Y,DF=Gann_angle(Input['High'], Input['Low'])
	del X, Y

	LongEntry=DF['H-Resistance'][8]
	ShortEntry=DF['L-Resistance'][8]
	LongFirstTarget=DF['H-Resistance'][5]
	LongSecondTarget=DF['H-Resistance'][0]
	ShortFirstTarget=DF['L-Resistance'][5]
	ShortSecondTarget=DF['L-Resistance'][0]
	LongStoploss=DF['H-Resistance'][10]
	ShortStoploss=DF['L-Resistance'][10]
	del DF
	Post={
		'LongEntry':LongEntry,
		'LongFirstTarget':LongFirstTarget,
		'LongSecondTarget':LongSecondTarget,
		'LongStoploss':LongStoploss,
		'ShortEntry':ShortEntry,
		'ShortFirstTarget':ShortFirstTarget,
		'ShortSecondTarget':ShortSecondTarget,
		'ShortStoploss':ShortStoploss
	}
	print(Post)
	return Post


def Gann_Volality_Targets(Symbol):
	Timeframe='1d'
	Input=db['{}_{}'.format(Symbol,Timeframe)].find_one(sort=[('_id', pymongo.DESCENDING)])
	data=list(db['{}_{}'.format(Symbol,Timeframe)].find().sort("_id", pymongo.DESCENDING).limit(11))
	data=pd.DataFrame(data)
	print(data)
	Pricerange=Price_Range(data)

	#print(Input)
	X,Y,DF=Gann_angle_volatility(Input['High'], Input['Low'],Pricerange)
	del X, Y

	LongEntry=DF['H-Resistance'][8]
	ShortEntry=DF['L-Resistance'][8]
	LongFirstTarget=DF['H-Resistance'][5]
	LongSecondTarget=DF['H-Resistance'][0]
	ShortFirstTarget=DF['L-Resistance'][5]
	ShortSecondTarget=DF['L-Resistance'][0]
	LongStoploss=DF['H-Resistance'][10]
	ShortStoploss=DF['L-Resistance'][10]
	del DF
	Post={
		'LongEntry':LongEntry,
		'LongFirstTarget':LongFirstTarget,
		'LongSecondTarget':LongSecondTarget,
		'LongStoploss':LongStoploss,
		'ShortEntry':ShortEntry,
		'ShortFirstTarget':ShortFirstTarget,
		'ShortSecondTarget':ShortSecondTarget,
		'ShortStoploss':ShortStoploss
	}
	print(Post)
	return Post

def Level_3_Gann_Volality_Targets(Symbol):
	Timeframe='1d'
	Input=db['{}_{}'.format(Symbol,Timeframe)].find_one(sort=[('_id', pymongo.DESCENDING)])
	data=list(db['{}_{}'.format(Symbol,Timeframe)].find().sort("_id", pymongo.DESCENDING).limit(11))
	data=pd.DataFrame(data)
	print(data)
	Pricerange=Price_Range(data)

	#print(Input)
	X1,Y1,DF1=Gann_angle_volatility(Input['High'], Input['Low'],Pricerange)
	X2,Y2,DF2=Gann_angle_volatility(DF1['H-Resistance'][0], DF1['L-Resistance'][0],Pricerange)
    #print(DF2['H-Resistance'][0], DF2['L-Resistance'][0],Pricerange)
	X3,Y3,DF3=Gann_angle_volatility(DF2['H-Resistance'][0], DF2['L-Resistance'][0],Pricerange)

	del X1, Y1, X2, Y2 , X3, Y3
	frames=[DF3,DF2,DF1]
	df=pd.concat(frames)
	pprint( df)
    
def Fibonacci_Levels(price,pricerange):
    Mat=[0.236,0.382,0.5,0.618,0.786,0.888,1.0,1.236,1.272,1.618]
    Referenceprice=[]
    H_resistance=[]
    L_resistance=[]
    for i in Mat:
    	p=i*pricerange
    	Referenceprice.append(p)
    	H_resistance.append(price+p)
    	L_resistance.append(price-p)
    
    post={
          'LongLevel1':H_resistance[0],
          'LongLevel2':H_resistance[1],
          'LongLevel3':H_resistance[2],
          'LongLevel4':H_resistance[3],
          'LongLevel5':H_resistance[4],
          'LongLevel6':H_resistance[5],
          'LongLevel7':H_resistance[6],
          'LongLevel8':H_resistance[7],
          'LongLevel9':H_resistance[8],
          'LongLevel10':H_resistance[9],
          'ShortLevel1':L_resistance[0],
          'ShortLevel2':L_resistance[1],
          'ShortLevel3':L_resistance[2],
          'ShortLevel4':L_resistance[3],
          'ShortLevel5':L_resistance[4],
          'ShortLevel6':L_resistance[5],
          'ShortLevel7':L_resistance[6],
          'ShortLevel8':L_resistance[7],
          'ShortLevel9':L_resistance[8],
          'ShortLevel10':L_resistance[9]
          
          }
    return post