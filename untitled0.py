# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:19:18 2021

@author: Ramakrishnamekala
"""

import pandas as pd
filename = 'pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv(filename, names=names)
print(data.shape)
