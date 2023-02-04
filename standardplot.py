# Write a program in Python that estimates the coefficients of the simple linear 
# regression equation, prints them, and plots the actual and estimated values (regression 
# line). Define the following functions: meanFun, varianceFun,
# covarianceFun, coefficientsFun

import matplotlib.pyplot as plt
import numpy as np


def meanFun(list: list):
    #return np.average(list)
    x = 0
    for i in list:
        x += i
    return x/len(list)

def varianceFun():

    return

def covarianceFun():
    return

#r^2 = SSR/SST
def coefficientsFun():
    return

def regressionSlope(data: list, xMean: int, yMean: int):
    numerator = 0
    denominator = 0

    for item in data:
        numerator += (item[0]-xMean) * (item[1] - yMean)
        denominator += (item[0]-xMean) * (item[0]-xMean)

    #float division??? python wack
    return numerator/denominator

def regressionYIntercept(slope: int, xMean: int, yMean: int):
    return yMean - slope*xMean


def plot_regression(data, slope, yintercept):

    xList = []
    for x in data:
        xList.append(x[0])

    x = np.linspace(np.min(xList), np.max(xList), 100)  # Create a list of evenly-spaced numbers over the range
    plt.plot(x, slope*x + yintercept)       # Plot the line

    for coords in data:
        x = coords[0]
        y = coords[1]
        plt.scatter(x, y)

    plt.show()                   # Display the plot


exampleData = [[1,14],[3,24],[2,18],[1,17],[3,27],[1,3]]

xList = []
for item in exampleData:
    xList.append(item[0])

xAverage = meanFun(xList)

yList = []
for item in exampleData:
    yList.append(item[1])

yAverage = meanFun(yList)

slope = regressionSlope(exampleData, xAverage, yAverage)
yintercept = regressionYIntercept(slope, xAverage, yAverage)
print('slope='+str(slope)+'\nyIntercept='+str(yintercept))
plot_regression(exampleData, slope, yintercept)



