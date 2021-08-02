# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 11:08:06 2021

@author: Ramakrishnamekala
"""
#from db import mydb as db
import pymongo
from math import sqrt
from prettytable import PrettyTable
from statistics import median
from pprint import pprint
import pandas as pd
import datetime
import math
import numpy as np
from bisect import bisect_left, bisect_right




def Gann_angle(High,Low):
    while True:
    
        Mat=['16X1','8X1','4X1','3X1','2X1','1X1',
             '1X2','1X3','1X4','1X8','1X16']
        Degree=[86.25,82.5,75,71.25,63.75,45,26.25,18.75,15,7.5,3.75]
        Degree_factor=[]
        for i in Degree:
            i=i*(1/180)
            Degree_factor.append(i)
        #print(Degree_factor)
        H_Resistance=[]
        L_Resistance=[]
        for i in Degree_factor:
            j=(sqrt(Low)+i)
            j=j*j
            H_Resistance.append(j)
            
            k=(sqrt(High)-i)
            k=k*k
            L_Resistance.append(k)
            
        #print(L_Resistance)
        #print(H_Resistance)
        Mat_=Mat[::-1]
        X=PrettyTable(['Matrixs','H-Degree','H-Degree_Factor','H-Resistance','Matrix','L-Degree','L-Degree_Factor','L-Resistance'])
        for i in range(0,len(Degree)-1):
            X.add_row([Mat[i],Degree[i],Degree_factor[i],H_Resistance[i],Mat[i],Degree[i],Degree_factor[i],L_Resistance[i]])
        #print(X)
        Trendset_up=sqrt(Low)+(1/180)*30
        Trendset_up=Trendset_up*Trendset_up
        Trendset_down=sqrt(High)-(1/180)*30
        Trendset_down=Trendset_down*Trendset_down
        Trendset_up_confirm=sqrt(Low)+(1/180)*45
        Trendset_up_confirm=Trendset_up_confirm*Trendset_up_confirm
        Trendset_down_confirm=sqrt(High)-(1/180)*45
        Trendset_down_confirm=Trendset_down_confirm*Trendset_down_confirm
        Y=PrettyTable(['','UpTrend','DownTrend'])
        Y.add_row(['Trend Set',Trendset_up,Trendset_down])
        Y.add_row(['Trend Confirm',Trendset_up_confirm,Trendset_down_confirm])
    
        check_negative=H_Resistance[-3]-L_Resistance[-3]
        #print(check_negative)
        if check_negative > 7:
            #print('done')
            break
        else:
            mid=[] 
            mid.append(Low)
            mid.append(High)
            #print(mid)
            mid=median(mid)
            High=mid
            Low=mid
            Mat=['16X1','8X1','4X1','3X1','2X1','1X1',
             '1X2','1X3','1X4','1X8','1X16']
            Degree=[86.25,82.5,75,71.25,63.75,45,26.25,18.75,15,7.5,3.75]
            Degree_factor=[]
            for i in Degree:
                i=i*(1/180)
                Degree_factor.append(i)
            #print(Degree_factor)
            H_Resistance=[]
            L_Resistance=[]
            for i in Degree_factor:
                j=(sqrt(Low)+i)
                j=j*j
                H_Resistance.append(j)
                
                k=(sqrt(High)-i)
                k=k*k
                L_Resistance.append(k)
                
            #print(L_Resistance)
            #print(H_Resistance)
            Mat_=Mat[::-1]
            X=PrettyTable(['Matrixs','H-Degree','H-Degree_Factor','H-Resistance','Matrix','L-Degree','L-Degree_Factor','L-Resistance'])
            for i in range(0,len(Degree)):
                X.add_row([Mat[i],Degree[i],Degree_factor[i],H_Resistance[i],Mat_[i],Degree[i],Degree_factor[i],L_Resistance[i]])
            #print(X)
            df=pd.DataFrame(columns=(['Matrixs','H-Degree','H-Degree_Factor','H-Resistance','Matrix','L-Degree','L-Degree_Factor','L-Resistance']))
            for i in range(0,len(Degree)):
                df.loc[len(df.index)]=[Mat[i],Degree[i],Degree_factor[i],H_Resistance[i],Mat_[i],Degree[i],Degree_factor[i],L_Resistance[i]]
            
            Trendset_up=sqrt(Low)+(1/180)*30
            Trendset_up=Trendset_up*Trendset_up
            Trendset_down=sqrt(High)-(1/180)*30
            Trendset_down=Trendset_down*Trendset_down
            Trendset_up_confirm=sqrt(Low)+(1/180)*45
            Trendset_up_confirm=Trendset_up_confirm*Trendset_up_confirm
            Trendset_down_confirm=sqrt(High)-(1/180)*45
            Trendset_down_confirm=Trendset_down_confirm*Trendset_down_confirm
            Y=PrettyTable(['','UpTrend','DownTrend'])
            Y.add_row(['Trend Set',Trendset_up,Trendset_down])
            Y.add_row(['Trend Confirm',Trendset_up_confirm,Trendset_down_confirm])
        
            check_negative=H_Resistance[-3]-L_Resistance[-3]
            print(mid)
        print(High)
        print(Low)
        print(X)
        print(Y)
        return X,Y,df
def Price_Range(DataDay):
    DataDay['ln']=np.log(DataDay['Close']/DataDay['Close'].shift(1))
    DataDay['sqrt']=DataDay['ln']*DataDay['ln']
    lnmean=DataDay['ln'].mean()
    sqrtmean=DataDay['sqrt'].mean()
    variance=sqrtmean-(lnmean*lnmean)
    dailyvolalitity=math.sqrt(variance)
    yearlyvolalitity=((math.sqrt(dailyvolalitity)*math.sqrt(365))/math.sqrt(365)*100)
    pricerange=round(list(DataDay['Close'])[-1]*dailyvolalitity,1)
    print('average ln',lnmean)
    print('avearge sqrt',sqrtmean)
    print('variance',variance)
    print('Daily vaolaitiyt',dailyvolalitity)
    print('yearly valaity',yearlyvolalitity)
    print('pricerange',pricerange)
    return pricerange

def make_ordinal(n):
    '''
    Convert an integer into its ordinal representation::

        make_ordinal(0)   => '0th'
        make_ordinal(3)   => '3rd'
        make_ordinal(122) => '122nd'
        make_ordinal(213) => '213th'
    '''
    n = int(n)
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix


def Gann_angle_volatility(High,Low,price):
    while True:
    
        Mat=['16X1','8X1','4X1','3X1','2X1','1X1',
             '1X2','1X3','1X4','1X8','1X16']
        Degree=[86.25,82.5,75,71.25,63.75,45,26.25,18.75,15,7.5,3.75]
        Degree_factor=[]
        Price_factor=[]
        for i in Degree:
            i=i*(1/180)
            Degree_factor.append(i)
        #print(Degree_factor)
        for i in Degree_factor:
            i=(i*price)
            Price_factor.append(i)
            
            
        H_Resistance=[]
        L_Resistance=[]
        for i in Price_factor:
            j=(Low+i)
            H_Resistance.append(round(j,2))
            
            k=(High-i)
            L_Resistance.append(round(k,2))
            
        #print(L_Resistance)
        #print(H_Resistance)
        Mat_=Mat[::-1]
        X=PrettyTable(['Matrixs','H-Degree','H-Degree_Factor','Price Factor H','H-Resistance','Matrix','L-Degree','L-Degree_Factor','Price Factor L','L-Resistance'])
        for i in range(0,len(Degree)-1):
            X.add_row([Mat[i],Degree[i],Degree_factor[i],Price_factor[i],H_Resistance[i],Mat_[i],Degree[i],Degree_factor[i],Price_factor[i],L_Resistance[i]])
        #print(X)
        Trendset_up=sqrt(Low)+(1/180)*30
        Trendset_up=Trendset_up*Trendset_up
        Trendset_down=sqrt(High)-(1/180)*30
        Trendset_down=Trendset_down*Trendset_down
        Trendset_up_confirm=sqrt(Low)+(1/180)*45
        Trendset_up_confirm=Trendset_up_confirm*Trendset_up_confirm
        Trendset_down_confirm=sqrt(High)-(1/180)*45
        Trendset_down_confirm=Trendset_down_confirm*Trendset_down_confirm
        Y=PrettyTable(['','UpTrend','DownTrend'])
        Y.add_row(['Trend Set',Trendset_up,Trendset_down])
        Y.add_row(['Trend Confirm',Trendset_up_confirm,Trendset_down_confirm])
    
        check_negative=H_Resistance[-3]-L_Resistance[-3]
        #print(check_negative)
        if check_negative > 7:
            #print('done')
            break
        else:
            mid=[] 
            mid.append(Low)
            mid.append(High)
            #print(mid)
            mid=median(mid)
            High=mid
            Low=mid
            Mat=['16X1','8X1','4X1','3X1','2X1','1X1',
             '1X2','1X3','1X4','1X8','1X16']
            Degree=[86.25,82.5,75,71.25,63.75,45,26.25,18.75,15,7.5,3.75]
            Degree_factor=[]
            for i in Degree:
                i=i*(1/180)
                Degree_factor.append(i)
            #print(Degree_factor)
            H_Resistance=[]
            L_Resistance=[]
            for i in Price_factor:
                j=(Low+i)
                H_Resistance.append(round(j,2))
                
                k=(High-i)
                L_Resistance.append(round(k,2))
                
            #print(L_Resistance)
            #print(H_Resistance)
            Mat_=Mat[::-1]
            X=PrettyTable(['Matrixs','H-Degree','H-Degree_Factor','Price Factor H','H-Resistance','Matrix','L-Degree','L-Degree_Factor','Price Factor L','L-Resistance'])
            for i in range(0,len(Degree)):
                X.add_row([Mat[i],Degree[i],Degree_factor[i],Price_factor[i],H_Resistance[i],Mat_[i],Degree[i],Degree_factor[i],Price_factor[i],L_Resistance[i]])
            #print(X)
            df=pd.DataFrame(columns=(['Matrixs','H-Degree','H-Degree_Factor','Price Factor H','H-Resistance','Matrix','L-Degree','L-Degree_Factor','Price Factor L','L-Resistance']))
            for i in range(0,len(Degree)):
                df.loc[len(df.index)]=[Mat[i],Degree[i],Degree_factor[i],Price_factor[i],H_Resistance[i],Mat_[i],Degree[i],Degree_factor[i],Price_factor[i],L_Resistance[i]]
            
            Trendset_up=sqrt(Low)+(1/180)*30
            Trendset_up=Trendset_up*Trendset_up
            Trendset_down=sqrt(High)-(1/180)*30
            Trendset_down=Trendset_down*Trendset_down
            Trendset_up_confirm=sqrt(Low)+(1/180)*45
            Trendset_up_confirm=Trendset_up_confirm*Trendset_up_confirm
            Trendset_down_confirm=sqrt(High)-(1/180)*45
            Trendset_down_confirm=Trendset_down_confirm*Trendset_down_confirm
            Y=PrettyTable(['','UpTrend','DownTrend'])
            Y.add_row(['Trend Set',Trendset_up,Trendset_down])
            Y.add_row(['Trend Confirm',Trendset_up_confirm,Trendset_down_confirm])
        
            check_negative=H_Resistance[-3]-L_Resistance[-3]
            print(mid)
        print(High)
        print(Low)
        print(X)
        print(Y)
        return X,Y,df



def Gann_angle_volatility1(High,Low,price):
    while True:
    
        Mat=['16X1','8X1','4X1','3X1','2X1','1X1',
             '1X2','1X3','1X4','1X8','1X16']
        Degree=[86.25,82.5,75,71.25,63.75,45,26.25,18.75,15,7.5,3.75]
        Degree_factor=[]
        Price_factor=[]
        for i in Degree:
            i=i*(1/180)
            Degree_factor.append(i)
        #print(Degree_factor)

        for i in Degree_factor:
            i=(sqrt(price)+i)
            i=i*i
            Price_factor.append(i)    
            
        H_Resistance=[]
        L_Resistance=[]
        for i in Price_factor:
            j=(Low+i)
            H_Resistance.append(round(j,2))
            
            k=(High-i)
            L_Resistance.append(round(k,2))
            
        #print(L_Resistance)
        #print(H_Resistance)
        Mat_=Mat[::-1]
        X=PrettyTable(['Matrixs','H-Degree','H-Degree_Factor','Price Factor H','H-Resistance','Matrix','L-Degree','L-Degree_Factor','Price Factor L','L-Resistance'])
        for i in range(0,len(Degree)-1):
            X.add_row([Mat[i],Degree[i],Degree_factor[i],Price_factor[i],H_Resistance[i],Mat_[i],Degree[i],Degree_factor[i],Price_factor[i],L_Resistance[i]])
        #print(X)
        Trendset_up=sqrt(Low)+(1/180)*30
        Trendset_up=Trendset_up*Trendset_up
        Trendset_down=sqrt(High)-(1/180)*30
        Trendset_down=Trendset_down*Trendset_down
        Trendset_up_confirm=sqrt(Low)+(1/180)*45
        Trendset_up_confirm=Trendset_up_confirm*Trendset_up_confirm
        Trendset_down_confirm=sqrt(High)-(1/180)*45
        Trendset_down_confirm=Trendset_down_confirm*Trendset_down_confirm
        Y=PrettyTable(['','UpTrend','DownTrend'])
        Y.add_row(['Trend Set',Trendset_up,Trendset_down])
        Y.add_row(['Trend Confirm',Trendset_up_confirm,Trendset_down_confirm])
    
        check_negative=H_Resistance[-3]-L_Resistance[-3]
        #print(check_negative)
        if check_negative > 7:
            #print('done')
            break
        else:
            mid=[] 
            mid.append(Low)
            mid.append(High)
            #print(mid)
            mid=median(mid)
            High=mid
            Low=mid
            Mat=['16X1','8X1','4X1','3X1','2X1','1X1',
             '1X2','1X3','1X4','1X8','1X16']
            Degree=[86.25,82.5,75,71.25,63.75,45,26.25,18.75,15,7.5,3.75]
            Degree_factor=[]
            for i in Degree:
                i=i*(1/180)
                Degree_factor.append(i)
            #print(Degree_factor)

        
            H_Resistance=[]
            L_Resistance=[]
            for i in Price_factor:
                j=(Low+i)
                H_Resistance.append(round(j,2))
                
                k=(High-i)
                L_Resistance.append(round(k,2))
                
            #print(L_Resistance)
            #print(H_Resistance)
            Mat_=Mat[::-1]
            X=PrettyTable(['Matrixs','H-Degree','H-Degree_Factor','Price Factor H','H-Resistance','Matrix','L-Degree','L-Degree_Factor','Price Factor L','L-Resistance'])
            for i in range(0,len(Degree)):
                X.add_row([Mat[i],Degree[i],Degree_factor[i],Price_factor[i],H_Resistance[i],Mat_[i],Degree[i],Degree_factor[i],Price_factor[i],L_Resistance[i]])
            #print(X)
            df=pd.DataFrame(columns=(['Matrixs','H-Degree','H-Degree_Factor','Price Factor H','H-Resistance','Matrix','L-Degree','L-Degree_Factor','Price Factor L','L-Resistance']))
            for i in range(0,len(Degree)):
                df.loc[len(df.index)]=[Mat[i],Degree[i],Degree_factor[i],Price_factor[i],H_Resistance[i],Mat_[i],Degree[i],Degree_factor[i],Price_factor[i],L_Resistance[i]]
            
            Trendset_up=sqrt(Low)+(1/180)*30
            Trendset_up=Trendset_up*Trendset_up
            Trendset_down=sqrt(High)-(1/180)*30
            Trendset_down=Trendset_down*Trendset_down
            Trendset_up_confirm=sqrt(Low)+(1/180)*45
            Trendset_up_confirm=Trendset_up_confirm*Trendset_up_confirm
            Trendset_down_confirm=sqrt(High)-(1/180)*45
            Trendset_down_confirm=Trendset_down_confirm*Trendset_down_confirm
            Y=PrettyTable(['','UpTrend','DownTrend'])
            Y.add_row(['Trend Set',Trendset_up,Trendset_down])
            Y.add_row(['Trend Confirm',Trendset_up_confirm,Trendset_down_confirm])
        
            check_negative=H_Resistance[-3]-L_Resistance[-3]
            print(mid)
        print(High)
        print(Low)
        print(X)
        print(Y)
        return X,Y,df

def Check_state(df,Data):
    index1 = abs(df['H-Resistance'] - Data['Close'][-1]).idxmin()
    index2 = abs(df['L-Resistance'] - Data['Close'][-1]).idxmin()
    
    #print(df['L-Resistance'][index2])
    if index1  < index2:
        return index1,1
    elif index1 > index2:
        return index2,2
    
    
def targets(df,state,limit):
    
    
    if state == 1:
        tgt=list(df['H-Resistance'].loc[:limit-1])[::-1]
    if state == 2:
        tgt=list(df['L-Resistance'].loc[:limit-1])[::-1]    
    if tgt:
        for i in range(len(tgt)):
            print('{} target {}'.format(make_ordinal(i+1),tgt[i]))
        return tgt

def tracker(targets,Data):
    Data=list(Data['Close'].iloc[15:])[-1]
    #print(targets)
    #print(Data)
    for i in range(len(targets)):
        if Data < targets[i]:
            print("Next targets are {}".format(targets[i]))

def Gann_cycler(No,High,Low,limit):
    X,Y,df=Gann_angle(High,Low)
    High=df['H-Resistance'][0]
    Low=df['L-Resistance'][0]
    if limit ==1:
        High=df['H-Resistance'][0]
        mid=High
    elif limit ==2:
        Low=df['L-Resistance'][0]
        mid=Low
    for i in range(No):
        X,Y,df=Gann_angle(High,Low)
        
    

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
























