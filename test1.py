import pandas as pd



price=31198.40
pricerange=429.510

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