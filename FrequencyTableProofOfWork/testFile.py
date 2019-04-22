# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:03:10 2019

@author: S518024
"""
import numpy as np
import math as mt
#df = x.apply(pd.Series)
df = [1,3,5,4,2,3,1,4,3,2,3,3,4,1,4,3,4,1,4,4,3]
def median(list):
    sortedList = sorted(list)
    index = len(sortedList)/2
    indexFloor = mt.floor(index)
    indexCeiling = mt.ceil(index)
    if sortedList[indexFloor] == sortedList[indexCeiling]:
        return sortedList[indexFloor]
    else:
        return sortedList[indexFloor], sortedList[indexCeiling]

def mode(list):
    modes = []
    modeDict = {}
    for i in list:
        if i not in modeDict:
            modeDict[i] = 1
        else:
            modeDict[i] += 1
    max_value = 0
    for i in modeDict:
        if modeDict[i] == 0:
            modes = [i]
            max_value = modeDict[i]
        else:
            if modeDict[i] == max_value:
                modes.append(i)
            else:
                if modeDict[i] > max_value:
                    modes = [i]
                    max_value = modeDict[i]
    return modes
#headings = list(df.columns.values)
#Mean should find the average
average = np.mean(df)
#Median should find the central number
middle = median(df)
#Mode should find the most common number
common = mode(df)
#Standard Deviation
deviate = np.std(df)
l = [average, middle, common, deviate]
#return l


x = [1,3,5,4,2,3,1,4,3,2,3,3,4,1,4,3,4,1,4,4,3]
'''y = mode(x)
print(y)
z = np.mean(x)
l = median(x)
print(z)
print(l)'''