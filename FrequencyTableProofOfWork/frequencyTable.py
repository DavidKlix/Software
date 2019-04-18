import xlwings as xw
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt

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

#@xw.func
#@xw.arg('x', pd.DataFrame, index=False, header=True) #takes in argument as dataframe
#@xw.ret(index=True, header=True, expand='table', numbers =int)#specifies how the data is returned
#def statMeasures(x):
 #   
 #   return results



@xw.func
@xw.arg('x', pd.DataFrame, index=False, header=True) #takes in argument as dataframe
@xw.ret(index=True, header=True, expand='table', numbers =int)#specifies how the data is returned
def barChart(x):
    df = x.apply(pd.Series)
    headings = list(df.columns.values)
    plt.bar(df[headings[0]], df[headings[1]], align='center', alpha=0.5)
    plt.ylabel(headings[1])
    plt.xlabel(headings[0])
    return plt.show()

@xw.func
@xw.arg('x', pd.DataFrame, index=False, header=True) #takes in argument as dataframe
@xw.ret(index=True, header=True, expand='table', numbers =int)#specifies how the data is returned
def pieChart(x):
    df = x.apply(pd.Series)
    headings = list(df.columns.values)
    plt.pie(df[headings[1]],labels=list(zip(df[headings[0]],df[headings[1]])),autopct='%1.1f%%')
    return plt.show()

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
    
    p1 = plt.bar(ind, alive, width)
    p2 = plt.bar(ind, dead, width, bottom=dead)
    
    plt.legend((p1[0], p2[0]), ('Men', 'Women'))
    
    return plt.show()

@xw.func
@xw.arg('x', pd.DataFrame, index=False, header=True) #takes in argument as dataframe
def sideBySideBarChart(x):
    df = x.apply(pd.Series)
    headings = list(df.columns.values)
    labels = df[0]
    n_groups = len(headings)-1 
    
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8
    
    alive =list( df.iloc[1])
    dead = list(df.iloc[2])
    alive = list(alive[1::])
    dead = list(dead[1::])
    
    rects1 = plt.bar(index, alive, bar_width,
    alpha=opacity,
    color='b',
    label= labels[1])
     
    rects2 = plt.bar(index + bar_width, dead, bar_width,
    alpha=opacity,
    color='g',
    label= labels[2])

    #plt.xticks(index + bar_width, (headings))
    #plt.legend()
     
    
    return plt.show()


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
    return plt.show()


@xw.func
@xw.arg('x', pd.DataFrame, index=False, header=True) #takes in argument as dataframe
def histogram(x,binLength = 1):
    df = x.apply(pd.Series)
    headings = list(df.columns.values)
    if (binLength == 1):
        binLength = len(df[headings[0]])
    binLength = int(binLength)
    theHist = np.histogram([1,2,1],bins =[0,1,2,3])
    return theHist