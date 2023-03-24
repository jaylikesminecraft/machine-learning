import math
import matplotlib.pyplot as plt
import numpy as np

def sigmoidEstimation(x: list, weights: list):
    sum = weights[0] # bias
    for i in range(len(x)):
        sum += weights[i+1] * x[i]
    return sigmoid(sum)

def sigmoid(z):
    a = 1 / (1 + math.exp((-1) * z))
    return a

def backpropogationError(x: list, y: float, weights: list, bTerm: int, xPoint: int):
    error = sigmoidEstimation(x,weights) - y
    b = sigmoid(weightedSum(weights, x))
    if bTerm == 0:
        c = (1-b)
    else:
        c = (1-b) * x[bTerm-1]

    return [error*b*c, error]

def backPropagation(x, y, iterations, learningRate, weights):
    
    errorRate = []

    for i in range(iterations):
        error = 0
        for m in range(len(x)):
            for k in range(len(weights)): 
                backError, error = backpropogationError(x[m], y[m], weights, k, m)
                weights[k] = weights[k] - learningRate * backError

        errorRate.append(error)
        
    return weights, errorRate

def plotData(error, iter):

    plt.plot(error)
    plt.show()
    return

def weightedSum(weights: list, x: list):
    sum = 0
    for j in range(len(weights)-1):
        sum += weights[j+1] * x[j]
    return sum + weights[0]

def limitBounds(x):
    
    limitedX = []
    maximums = []

    for j in range(len(x[0])):
        maximums.append(max(list(map(lambda item : item[j], x))))

    for i in range(len(x)):
        row = [0] * len(x[0])
        for j in range(len(x[0])):
            row[j] = x[i][j] / maximums[j]
        limitedX.append(row)
            
    return limitedX
            
numOfInptus = 2
# weights[0] is the bias

x = [[1,1],[0,1],[1,0],[0,0]]
weights = [0] * (len(x[0]) + 1)
#x = limitBounds(x)
y = [1,0,0,0]

weights, error = backPropagation(x, y, 10000, .1, weights)

print(weights)
for i in range(len(x)):
    print(str(x[i])+" = "+str(sigmoidEstimation(x[i], weights)))

plotData(error,100)