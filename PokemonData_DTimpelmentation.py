#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 12:17:08 2017

@author: Debanjan Goswami
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
data = pd.read_csv('/Users/debanjangoswami/Pokemon.csv')

#prints the first five values of data
print(data.head())

#Generation of Heatmap based upon the correlation matrix
sns.heatmap(data.corr())

#drops all the columns that are significant in the predictions
data=data.drop('Type 1',axis=1)
data=data.drop('Type 2',axis=1)

# replacing all the NAN values with last valid observation forward to next valid observation
data=data.fillna(method='pad',axis=1)

# assigning labels to the data
labelEncoder =LabelEncoder()
for col in data.columns:
    data[col] = labelEncoder.fit_transform(data[col])
    
    
#drops the output data from given input#dropping 
X = data.drop('Legendary', axis=1)

#output required
y = data['Legendary']

#splits the data into training and testing parts
split=int(0.8*data.shape[0])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
dt = DecisionTreeClassifier(max_depth=10)

#fitting the training data
print(dt.fit(X_train,y_train))
#Accuracy on the training Set
print(dt.score(X_train,y_train))
#checks the accracy score for the testing parts of the data
print(dt.score(X_test,y_test))
