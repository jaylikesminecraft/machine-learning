# Write a program in Python that estimates the inverse of a matrix. Define the following
# functions: matrixTranspose, matrixMinor, matrixDeterminant,
# matrixInverse.

# Example:
# Find the inverse of matrix A.
# A = [[4, 1, -5], [-2, 3, 1], [3, -1, 4]]

# 1. Check that it is a square matrix, here 3 × 3, since only
# square matrices can have inverses.
# 2. Evaluate the determinant to be sure 𝑨 ≠ 0, since only
# nonsingular matrices can have inverses.
# 3. Find the cofactor matrix of 𝑨,
# 4. Then transpose the cofactor matrix to get the adjoint matrix.
# 5. Multiply the adjoint matrix by 1Τ 𝑨

import numpy as np


def isSquare(matrix):
    if len(matrix) == len(matrix[0]):
        return True

    # print("matrix is not square")
    return False


def determinant(matrix):
    if not isSquare(matrix):
        quit()

    return determinantR(matrix)


def determinantR(matrix):
    if len(matrix) == 2:
        return twoByTwoDeterminant(matrix)
    else:

        laplace = []
        for i in range(len(matrix)):
            a = matrix[i][0]
            a = a*determinantR(removeRowAndColum(matrix, i, 0))
            laplace.append(a)

        return laplaceExpansion(laplace)


def laplaceExpansion(laplace):
    determinant = 0
    for i in range(len(laplace)):
        if (i % 2) == 0:
            determinant += laplace[i]*1
        else:
            determinant += laplace[i]*-1
    return determinant


def removeRowAndColum(matrix, row, colum):
    if (len(matrix) < 3):
        print("cannot remove row and colum")
        return None

    newMatrix = []

    for i in range(len(matrix)):
        newRow = []
        if i == row:
            continue
        for j in range(len(matrix)):
            if j == colum:
                continue
            newRow.append(matrix[i][j])

        newMatrix.append(newRow)

    return newMatrix


def twoByTwoDeterminant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]


def transpose(matrix):
    newMatrix = []
    newRow = []
    for i in range(len(matrix)):
        newRow = []
        for j in range(len(matrix)):
            newRow.append(matrix[j][i])
        newMatrix.append(newRow)

    return newMatrix


def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


def cofectorMatrix(matrix):

    newMatrix = []
    row = []

    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            row.append(cofactor(matrix, i, j))
        newMatrix.append(row)

    return newMatrix


def cofactor(matrix, i, j):

    newMatrix = removeRowAndColum(matrix, i, j)
    determ = determinant(newMatrix)
    if not (i+j) % 2 == 0:
        return determ * (-1)

    return determ


def adjointMatrix(matrix):
    return transpose(cofectorMatrix(matrix))


def inverseMatrix(matrix):

    if not isSquare(matrix):
        print("matrix not square, cannot compute inverse")
        quit()

    det = determinant(matrix)

    if det == 0:
        print("determinant is zero, cannot compute inverse")
        quit()

    inverseDeterminant = 1/det
    adjMatrix = adjointMatrix(matrix)

    invMatrix = []

    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            row.append(adjMatrix[i][j] * inverseDeterminant)
        invMatrix.append(row)

    return invMatrix


def roundMatrix(matrix):
    newMatrix = []

    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(round(matrix[i][j], 9))
        newMatrix.append(row)

    return newMatrix


matrix = [[4, 1, -5], [-2, 3, 1], [3, -1, 4]]
#matrix = [[1,4,3,2],[5,6,7,1],[9,10,11,12],[13,14,15,17]]
#matrix = [[1,4,3,2,7],[5,6,7,1,3],[9,10,11,12,2],[13,14,15,17,31],[13,4,1,17,31]]
#matrix = [[5,9,2],[1,8,5],[3,6,4]]
#matrix = [[5,9,2],[1,8,5],[3,6,4],[3,6,4]]
printMatrix(matrix)
print("")
printMatrix(inverseMatrix(matrix))
print("")
identityMatrix = np.matmul(matrix, inverseMatrix(matrix))
printMatrix(roundMatrix(identityMatrix))
