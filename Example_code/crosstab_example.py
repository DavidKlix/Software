# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:44:21 2019

@author: S524113
"""

import pandas as pd

df = pd.read_csv('tabby.csv')

tabby = pd.crosstab(df['Sex'], df['Status'], margins=True)

print(tabby)