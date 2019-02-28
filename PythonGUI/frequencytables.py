# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 20:42:35 2019

@author: S524113
"""

import pandas as pd
import numpy as np
from prettytable import PrettyTable

def frequency_table(COLUMN, df):
    tb = PrettyTable()
    tb.field_names = [COLUMN, "Count"]
    unique_val = df[COLUMN].unique()
    for i in range(len(unique_val)):
        count = (df[COLUMN] == unique_val[i]).sum()
        tb.add_row([unique_val[i], count])
    tb.add_row(["Total", df[COLUMN].size])
    return tb.get_string(title=COLUMN +" Frequency Table")
    
def relative_frequency_table(COLUMN, df):
    tb = PrettyTable()
    tb.field_names = [COLUMN, "Count", "%"]
    unique_val = df[COLUMN].unique()
    size = df[COLUMN].size
    for i in range(len(unique_val)):
        count = (df[COLUMN] == unique_val[i]).sum()
        tb.add_row([unique_val[i], count, 100 * count/size])
    tb.add_row(["Total", size, "100"])
    return tb.get_string(title=COLUMN +" Relative Frequency Table")   

