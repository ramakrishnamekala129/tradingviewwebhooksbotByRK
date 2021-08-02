# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 08:32:32 2021

@author: Ramakrishnamekala
"""

import pandas as pd
import numpy as np
import ccxt
import talib.abstract as ta
from database import db
from technicalta import *

from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn import svm
import joblib

def texterconversion(text):
    tex=text.replace('/','').replace('-','_').replace(' ','_').replace('(','').replace(')','')
    return tex

df=list(db['BNBUSDT_1h'].find())


def Dataset(df):
    global listof1
    df=pd.DataFrame(df)
    df=df.iloc[:,1:]
    df['open']=df['Open']
    df['high']=df['High']
    df['low']=df['Low']
    df['close']=df['Close']
    df['volume']=df['Volume']
    l=[texterconversion(file) for file in listof1]
    for i in listof1:
        df[i]=technicalselector(texterconversion(i),df)
    #print(df)
    df['date']=pd.to_datetime(df['date'])
    df=df.drop(['periods','Open','High','Low','Close','Volume'],axis=1)
    #df=df.dropna(axis=1)
    df=df.dropna(axis=0)
    df['out']=df['close'].shift(-1)

    df['out']=np.where(df['close'] > df['out'],-1,(np.where(df['close'] < df['out'],1,0)))
    df=df.iloc[:-1,:]
    print(df.tail(1))
    return df
df=Dataset(df)
#print(df)



labels = df['out'].values
features = df.iloc[:,1:-1].values

Standarization = True

if Standarization == True:
    minmax = False
    Standard = True
    if minmax == True:
        min_max = MinMaxScaler()
        newfeatures = min_max.fit_transform(features)
        X_train, X_test, y_train, y_test = train_test_split(newfeatures, labels, test_size=0.1)
    elif Standard == True:
        std = StandardScaler()
        newfeatures = std.fit_transform(features)
        X_train, X_test, y_train, y_test = train_test_split(newfeatures, labels, test_size=0.1)
else:
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.1)


clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

accuracy = clf.score(X_train, y_train)
print ('DT Traning Data accuracy ', accuracy*100)

accuracy = clf.score(X_test, y_test)
print ('DT Testing Data accuracy ', accuracy*100)

print('------------------------------------------')
# Output a pickle file for the model
joblib.dump(clf, 'saved_model_dt.pkl')


clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(X_train, y_train)

accuracy = clf.score(X_train, y_train)
print ('RF Traning Data accuracy ', accuracy*100)

accuracy = clf.score(X_test, y_test)
print ('RF Testing Data accuracy ', accuracy*100)

print('------------------------------------------')

# Output a pickle file for the model
joblib.dump(clf, 'saved_model_rf.pkl')


clf = KNeighborsClassifier()
clf = clf.fit(X_train, y_train)

accuracy = clf.score(X_train, y_train)
print ('KNN Traning Data accuracy ', accuracy*100)

accuracy = clf.score(X_test, y_test)
print ('KNN Testing Data accuracy ', accuracy*100)

print('------------------------------------------')

# Output a pickle file for the model
joblib.dump(clf, 'saved_model_knn.pkl')

clf = MLPClassifier(activation='relu',max_iter=100000)
clf = clf.fit(X_train, y_train)

accuracy = clf.score(X_train, y_train)
print ('NN Traning Data accuracy ', accuracy*100)

accuracy = clf.score(X_test, y_test)
print ('NN Testing Data accuracy ', accuracy*100)

print('------------------------------------------')

# Output a pickle file for the model
joblib.dump(clf, 'saved_model_nn.pkl')

clf = svm.SVC(kernel='linear')
clf = clf.fit(X_train, y_train)

accuracy = clf.score(X_train, y_train)
print ('SVM Traning Data accuracy ', accuracy*100)

accuracy = clf.score(X_test, y_test)
print ('SVM Testing Data accuracy ', accuracy*100)

print('------------------------------------------')

# Output a pickle file for the model
joblib.dump(clf, 'saved_model_svm.pkl')