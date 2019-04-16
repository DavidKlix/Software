# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:03:10 2019

@author: S518024
"""

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
        if modeDict[i] >= max_value:
            modes.append(i)
            max_value = modeDict[i]
    return modes

x = [1,3,5,4,2,3,1,4,3,2,3,3,4,1,4,3,4,1,3]
y = mode(x)
print(y)