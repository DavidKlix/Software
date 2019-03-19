# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:44:21 2019

@author: S524113
"""
import xlwings as xw
import pandas as pd
@xw.func
@xw.arg('x', pd.DataFrame, index=False, header=True) #takes in argument as dataframe
@xw.ret(index=True, header=True, expand='table', numbers =int)#specifies how the data is returned
def contingencyTable(x):
    df = x.apply(pd.Series)
    tabby = pd.crosstab(df['Sex'], df['Status'], margins=True)
    return tabby