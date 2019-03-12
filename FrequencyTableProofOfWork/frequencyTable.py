import xlwings as xw
import pandas as pd


@xw.func
def hello(name):
    return "hello {0}".format(name)

@xw.func
@xw.arg('x', pd.DataFrame, index=False, header=True) #takes in argument as dataframe
@xw.ret(index=True, header=True, expand='table', numbers =int)#specifies how the data is returned
def frequencyTable(x):
    valueCounts = x.apply(pd.Series.value_counts)
    return valueCounts
'''
def frequencyTablePercent(x):
    valueCounts = x.apply(pd.Series.value_counts)
    total = 0
    for n in Series:
        total += 1
    return valueCounts/total
'''