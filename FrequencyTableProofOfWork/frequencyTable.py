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
#pd is the module
#Series is a type
#value_counts is a function
@xw.func
@xw.arg('x', pd.DataFrame, index=False, header=True) #takes in argument as dataframe
@xw.ret(index=True, header=True, expand='table', numbers =int)#specifies how the data is returned
def frequencyTablePercent(x):
    valueCounts = frequencyTable(x)
    total = 0
    for valueCounts in x:
        total += 1
    if total == 0:
        return 0
    return total
