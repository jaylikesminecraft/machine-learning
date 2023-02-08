import matplotlib.pyplot as plt
import numpy as np

def plotRegression(data, slope, yintercept):
    x = np.linspace(0, 5, 100)  # Create a list of evenly-spaced numbers over the range
    plt.plot(x, x*slope+yintercept) 
    for coords in data:
        x = coords[0]
        y = coords[1]
        plt.scatter(x, y)
    plt.show()

data = [[1,14],[3,24],[2,18],[1,17],[3,27]]

xAverage = np.average(list(map(lambda item : item[0], data)))
yAverage = np.average(list(map(lambda item : item[1], data)))

slope = sum(list(map(lambda item : (item[0]-xAverage)*(item[1]-yAverage), data))) / sum(list(map(lambda item : np.square(item[0]-xAverage), data)))
yintercept = yAverage - slope*xAverage
variance = sum(list(map(lambda item : np.square(item[0]-xAverage), data))) / (len(data)-1)
covariance = sum(list(map(lambda item : (item[0]-xAverage)*(item[1]-yAverage), data))) / (len(data)-1)
coefficients = covariance/np.square(variance)

print("slope = ", slope)
print("variance = ", variance)
print("covariance = ", covariance)
print("coefficients = ", coefficients)
print("x average = ", xAverage)
print("y average = ", yAverage)
print(data)
plotRegression(data, slope, yintercept)