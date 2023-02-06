import matplotlib.pyplot as plt

def meanFun(list: list):
    x = 0
    for i in list:
        x += i
    return x/len(list)

def varianceFun(list: list, xAverage):
    sum = 0
    for x in list:
        sum += (x[0]-xAverage)*(x[0]-xAverage)

    print("variance = ", sum / (len(list) - 1))

    return sum / (len(list) - 1)

def covarianceFun(list: list, xAverage: int, yAverage: int):
    sum = 0
    for xy in list:
        sum += (xy[0]-xAverage)*(xy[1]-yAverage)

    print("covariance = ", sum / (len(list) - 1))

    return sum / (len(list) - 1)

def coefficientsFun(list: list, yAverage: int, xAverage: int):
    b0 = yAverage + xAverage

    variance = varianceFun(list, xAverage)

    b1 = covarianceFun(list, xAverage, yAverage) / variance*variance
    return b1

def regressionSlope(data: list, xMean: int, yMean: int):
    numerator = 0
    denominator = 0

    for item in data:
        numerator += (item[0]-xMean) * (item[1] - yMean)
        denominator += (item[0]-xMean) * (item[0]-xMean)

    return numerator/denominator

def regressionYIntercept(slope: int, xMean: int, yMean: int):
    return yMean - slope*xMean

def plotRegression(data, slope, yintercept):

    xList = []
    yList = []
    i = 0
    for x in data:
        xList.append(i)
        yList.append(i*slope + yintercept)
        i += 1

    plt.plot(xList, yList)

    for coords in data:
        x = coords[0]
        y = coords[1]
        plt.scatter(x, y)

    plt.show()


exampleData = [[1,14],[3,24],[2,18],[1,17],[3,27]]
# exampleData = [[1,3],[2,5],[3,7],[4,6],[5,9],[6,10],[7,23],[8,31],[9,21],[10,29]]

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
print('slope='+str(slope)+'\nyIntercept='+str(yintercept)+'\ncoefficient='+str(coefficientsFun(exampleData, yAverage, xAverage)))
plotRegression(exampleData, slope, yintercept)



