import math
import matplotlib.pyplot as plt
import numpy as np
import random

def probabilityFun(x, weights):

    sum = 0
    for i in range(len(weights)):
        if not i == 0:
            sum += weights[i] * x[i-1]
        else:
            sum += weights[i] #intercept / bias
    return sigmoid(sum)

def sigmoid(z):
    a = 1 / (1 + math.exp((-1) * z))
    return a

def costFunctionPoint(x, y, weights):
    probability = probabilityFun(x, weights)
    return (y * math.log(probability) + (1 - y) * (math.log(1-probability)))

def costFunctionAll(x, y, weights):
    sum = 0
    for i in range(len(y)):
        for j in range(len(x[0])):
            sum += costFunctionPoint(x[j], y[i], weights)
    return sum/len(x) * (-1)

def gradient(x, y, k, weights):
    
    totalsum = 0
    for i in range(len(x)):
        sum = 0
        for j in range(len(x[0])):
            sum = (y[i] - probabilityFun(x[i], weights)) 
        if k > 0 :
            sum *= x[i][j]
        totalsum += sum

    return totalsum

def error(x, y, weights):
    sum = 0
    for i in range(len(x)):
        sum += (y[i] - probabilityFun(x[i], weights))* (y[i] - probabilityFun(x[i], weights))
    return sum

def gradientAscentFunction(x, y, iterations, learningRate, weights):
    for i in range(iterations):
        for k in range(len(weights)):                
            weights[k] = weights[k] + learningRate * gradient(x, y, k, weights)
    return weights

def makeData():
    
    #data = [[0,0],[0,1],[0,2],[0,3],[0,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10]]
    data = [[0,.5],[0,.75],[0,1],[0,1.25],[0,1.5],[0,1.75],[1,1.75],[0,2],[1,2.25],[0,2.5],[1, 2.75],[0,3],[1,3.25],[0,3.5],[1,4],[1,4.25],[1,4.5],[1,4.75],[1,5],[1,5.5]]
    x = []
    y = []
    for i in range(len(data)):
        row = []
        y.append(data[i][0])
        row.append(data[i][1])
        x.append(row)

    return [data, x, y]

def makeRandomData():
    data = []
    x = []
    y = []
    for i in range(100):
        row=  []
        row.append(random.randint(0,10))
        x.append(row)
        if row[0] > 5:
            y.append(1)
        else:
            y.append(0)
    return data, x, y

def plotData(x,y,midpoint, slope,weights):
    
    # y = m x + b
    # b = y - m x 

    b = 0.5 - slope * midpoint
    
    resolu = 100
    max = 0
    for i in range(len(x)):
        if x[i][0] > max:
            max = x[i][0]
        
    xtemp = np.linspace(0, max, resolu)

    plt.plot(xtemp, xtemp*slope + b)    

    xi = []
    for i in range(resolu):
        row = []
        row.append(xtemp[i])
        xi.append(row)

    yi = []
    for i in range(resolu):
        yi.append(probabilityFun(xi[i], weights))
        
    plt.plot(xi, yi)
    
    for i in range(len(y)):
        xi = x[i]
        yi = y[i]
        plt.scatter(xi, yi)

    plt.ylim(-.1,1.1)
    plt.show()

data, x, y = makeData()
#data, x, y = makeRandomData()
weights = [0, 0]
weights = gradientAscentFunction(x,y, 1000, .11, weights)
print(weights)
print("error=",error(x,y,weights))

midpoint = ((-1) * weights[0]) / weights[1]
print("u=",midpoint)
ymidpoint = probabilityFun([midpoint], weights)
slope = (weights[1])*0.25
print("slope=",slope)
plotData(x,y,midpoint,slope, weights)


