# Write a program in Python that estimates the coefficients of the simple linear 
# regression equation, prints them, and plots the actual and estimated values (regression 
# line). Define the following functions: meanFun, varianceFun,
# covarianceFun, coefficientsFun

import matplotlib.pyplot as plt
import numpy as np


def meanFun():
    return

def varianceFun():
    return

def covarianceFun():
    return

def coefficientsFun():
    return

def plot_regression(data, slope, yintercept):

    x = np.linspace(0, 4, 100)  # Create a list of evenly-spaced numbers over the range
    plt.plot(x, slope*x + yintercept)       # Plot the line

    for coords in data:
        x = coords[0]
        y = coords[1]
        plt.scatter(x, y)

    plt.show()                   # Display the plot

    
exampleData = [[1,14],[3,24],[2,18],[1,17],[3,27]]
slope = 5
yintercept = 10
plot_regression(exampleData, slope, yintercept)



