import xlwings as xw
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
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
@xw.ret(index=True, header=True, expand='table', numbers =int)#specifies how the data is returned
def sideBySideBarChart(x):
    df = x.apply(pd.Series)
    headings = list(df.columns.values)
    N = len(df[headings[1]])
    menMeans = df[headings[1]]
    womenMeans = df[headings[2]]
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence
    
    p1 = plt.bar(ind, menMeans, width)
    p2 = plt.bar(ind, womenMeans, width, bottom=menMeans)
    
    plt.ylabel('Scores')
    plt.title('Scores by group and gender')
    plt.xticks(df[headings[0]])
    plt.legend((p1[0], p2[0]), ('Men', 'Women'))
    
    return plt.show()