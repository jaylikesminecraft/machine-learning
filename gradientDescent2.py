import random


def transpose(matrix):
    newMatrix = []
    newRow = []
    for i in range(len(matrix)):
        newRow = []
        for j in range(len(matrix)):
            newRow.append(matrix[j][i])
        newMatrix.append(newRow)

    return newMatrix

def transposeVector(vector):
    newVector = []

    for i in range(len(vector)):
        row = []
        row.append(vector[i])
        newVector.append(row)

    return newVector


def matrixMult(A, B):

    if not len(A[0]) == len(B):
        print("cannot mult")
        quit()

    newMat = []
    
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            row.append(matrixMultHelper(getRow(A, i), getCol(B, j)))
        newMat.append(row)

    return newMat

def getCol(matrix, col):
    vector = []
    
    for i in range(len(matrix)):
        row = []
        row.append(matrix[i][col])
        vector.append(row)
    
    return vector

def getRow(matrix, row):
    return matrix[row]

def matrixMultHelper(rowList, colList):
    sum = 0
    for i in range(len(rowList)):
        sum = sum + rowList[i] * colList[i][0]
    return sum
      
def gradientDescentFunction(y, data, iterations, learningRate, bTerms):

    for i in range(iterations):
        for k in range(len(bTerms)):
            bTerms[k] = bTerms[k] - learningRate * derivativeB(y, data, k, bTerms)

    return bTerms


def makeData(rows, cols):
    data = []
    for i in range(rows):
        row = []
        row.append(1)
        for j in range(cols):
            row.append(random.gauss())

        data.append(row)
    
    return data

def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def derivativeB(Y, data, bTerm, bTerms):
    totalSum = 0
    for i in range(len(data)):
        sum = Y[i][0]
        for j in range(len(data[0])):
            sum -= data[i][j]*bTerms[j]

        if bTerm > 0:
            sum *= (data[i][bTerm])

        totalSum += sum

    return totalSum * (-0.5)


bterms = [0,0,0]
learning_rate = 0.01
iterations = 1000

real_B_coefficents = [1,2,5]
data = makeData(100,2)
asdf = matrixMult(data, transposeVector(real_B_coefficents))

y = []

for i in range(len(asdf)):
    row = []
    row.append(asdf[i][0]+ random.gauss())
    y.append(row)

bTerms = [0,0,0]
print(gradientDescentFunction(y, data, iterations, 0.01, bTerms))




    
