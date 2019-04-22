import xlwings as xw
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import math as mt

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
        valueCounts = x.apply(pd.Series.value_counts, normalize = True)
        headings = list(valueCounts.columns.values)
        returning = x.apply(pd.Series.value_counts)
        returning["percent"] = valueCounts[headings[0]]
        return returning

@xw.func
@xw.arg('x', pd.DataFrame, index=False, header=True) #takes in argument as dataframe
@xw.ret(index=True, header=True, expand='table', numbers =int)#specifies how the data is returned
def contingencyTable(x):
    df = x.apply(pd.Series)
    headings = list(df.columns.values)
    tabby = pd.crosstab(columns = df[headings[0]], index= df[headings[1]], margins=True)
    return tabby

@xw.func
@xw.arg('x', pd.DataFrame, index=False, header=True) #takes in argument as dataframe
@xw.ret(index=True, header=True, expand='table', numbers =int)#specifies how the data is returned
def statMeasures(x):
    df = x.apply(pd.Series)
    #headings = list(df.columns.values)
    #Mean should find the average
    average = np.mean(df)
    #Median should find the central number
    middle = median(df)
    #Mode should find the most common number
    common = mode(df)
    #Standard Deviation
    deviate = np.std(df)
    #Range
    ran = ranging(df)
    #Minimum number
    minimum = min(df)
    #Maximum number
    maximum = max(df)
    #Sum of the list
    total = sum(df)
    #How many elements are in the list
    count = len(df)
    #First quartile
    Q1 = firstQuartile(df)
    #Third Quartile
    Q3 = thirdQuartile(df)
    #Interquartile Range
    IQR = Q3 - Q1
    #Variance
    var = variance(df)
    #Combination of all numbers in a list
    l = [average, middle, common, deviate, ran, 
         minimum, maximum, total, count, Q1, Q3, IQR, var]
    return l
def ranging(list):
    q = sorted(list)
    last = len(q) - 1
    return q[last] - q[0]
def firstQuartile(list):
    #List must be sorted to get the right values
    q = sorted(list)
    count = len(q)
    #Taking floor to get a whole number
    index = mt.floor(count/4)
    return q[index]
def thirdQuartile(list):
    #List must be sorted to get the right values
    q = sorted(list)
    count = len(q)
    #Taking floor to match Q1
    index = mt.floor(count/4)*3
    return q[index]
def variance(list):
    subtList = []
    sqList = []
    for i in list:
        subtList.append(list[i] - np.mean(list))
        sqList.append(subtList[i]**2)
    summed = sum(sqList)
    return summed/len(list)
def median(list):
    #List must be sorted to get the right values
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

@xw.func
@xw.arg('x', pd.DataFrame, index=False, header=True) #takes in argument as dataframe
@xw.ret(index=True, header=True, expand='table', numbers =int)#specifies how the data is returned
def barChart(x):
    df = x.apply(pd.Series)
    headings = list(df.columns.values)
    fig = plt.figure()
    plt.bar(df[headings[0]], df[headings[1]], align='center', alpha=0.5)
    plt.ylabel(headings[1])
    plt.xlabel(headings[0])
    sht = xw.Book().sheets[0]
    sht.pictures.add(fig,name = "test",update ="TRUE")
    return "bar slot"

@xw.func
@xw.arg('x', pd.DataFrame, index=False, header=True) #takes in argument as dataframe
@xw.ret(index=True, header=True, expand='table', numbers =int)#specifies how the data is returned
def pieChart(x):
    df = x.apply(pd.Series)
    headings = list(df.columns.values)
    fig = plt.figure()
    plt.pie(df[headings[1]],labels=list(zip(df[headings[0]],df[headings[1]])),autopct='%1.1f%%')
    sht = xw.Book().sheets[0]
    sht.pictures.add(fig,name = "test",update ="TRUE")
    return "pie slot"

@xw.func
@xw.arg('x', pd.DataFrame, index=False, header=True) #takes in argument as dataframe
def segmentedBarChart(x):
    df = x.apply(pd.Series)
    headings = list(df.columns.values)
    N = len(headings)-1

    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence
    
    alive =list( df.iloc[1])
    dead = list(df.iloc[2])
    alive = list(alive[1::])
    dead = list(dead[1::])
    
    fig = plt.figure()
    p1 = plt.bar(ind, alive, width)
    p2 = plt.bar(ind, dead, width, bottom=dead)
    
    plt.legend((p1[0], p2[0]), ('Men', 'Women'))
    
    
    sht = xw.Book().sheets[0]
    sht.pictures.add(fig,name = "test",update ="TRUE")
    return "Segmented Slot"

@xw.func
@xw.arg('x', pd.DataFrame, index=False, header=True) #takes in argument as dataframe
def sideBySideBarChart(x):
    df = x.apply(pd.Series)
    headings = list(df.columns.values)
    labels = df[0]
    n_groups = len(headings)-1 
    fig , ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8
    
    col1 = df[headings[1]]
    col2 = df[headings[2]]
    fig = plt.figure()
    plt.bar(index, col1, bar_width,
    alpha=opacity,
    color='b',
    label= labels[1])
     
    plt.bar(index + bar_width, col2, bar_width,
    alpha=opacity,
    color='g',
    label= labels[2])
    
    sht = xw.Book().sheets[0]
    sht.pictures.add(fig,name = "test",update ="TRUE")
    return "Side Slot"


@xw.func
@xw.arg('x', pd.DataFrame, index=False, header=True) #takes in argument as dataframe
def test(x):
    # data to plot
    n_groups = 4
    
    
    means_frank = (203,118,178,212)
    means_guido = (112,167,528,673)
     
    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8
    fig = plt.figure()
    rects1 = plt.bar(index, means_frank, bar_width,
    alpha=opacity,
    color='b',
    label='Frank')
     
    rects2 = plt.bar(index + bar_width, means_guido, bar_width,
    alpha=opacity,
    color='g',
    label='Guido')
     
    plt.xlabel('Person')
    plt.ylabel('Scores')
    plt.title('Scores by person')
    plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
    plt.legend()
     
    plt.tight_layout()
    sht = xw.Book().sheets[0]
    sht.pictures.add(fig,name = "test",update ="TRUE")
    return "Test Slot"



@xw.func
@xw.arg('x', pd.DataFrame, index=False, header=True) #takes in argument as dataframe
def histogram(x,binLength = 1):
    df = x.apply(pd.Series)
    headings = list(df.columns.values)
    if (binLength == 1):
        binLength = len(df[headings[0]])
    binLength = int(binLength)
    fig = plt.figure()
    plt.hist(df[headings[0]],bins =range(binLength))
    sht = xw.Book().sheets[1]
    plt.hist([1,2,1],bins =[0,1,2,3])
    sht = xw.Book().sheets[0]
    sht.pictures.add(fig,name = "test",update ="TRUE")
    return "Histogram Slot"
