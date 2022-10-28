from math import sqrt
from helper import *
from collections import deque

# Global Variables
sideLength = 8
queueLength = 10
pixelCount = 64
backgroundQueue = [deque([0 for i in range(queueLength)]) for i in range(pixelCount)]
measuresOfDispersion = [[0, 0] for i in range(pixelCount)]   # index 0 has sum and 1 has sum of squares

# Background update
def updateBackground(M, B, S):
    global sideLength, queueLength, pixelCount, backgroundQueue, measuresOfDispersion
    B = M
    B = B
    for j in range(sideLength):
        for i in range(sideLength):
            index = i * sideLength + j
            pushed = M[i][j]
            popped = 0
            if(len(backgroundQueue[index]) >= queueLength):
                popped = backgroundQueue[index].popleft()

            backgroundQueue[index].append(pushed)
            measuresOfDispersion[index][0] += pushed
            measuresOfDispersion[index][0] -= popped
            measuresOfDispersion[index][1] += (pushed**2)
            measuresOfDispersion[index][1] -= (popped**2)

            mean = measuresOfDispersion[index][0] / queueLength
            secondmoment = measuresOfDispersion[index][1] / queueLength 
            S[i][j] = sqrt(secondmoment - (mean**2))

# takes M = currentthermalmap
#       B = thermalmap of background
#       S = stddeviation
# returns feature vector
def extractFeatureVector(M, B, S):
    X = [[0 for i in range(sideLength)] for j in range(sideLength)]
    F = [[0 for i in range(sideLength)] for j in range(sideLength)]
    feature1 = 0
    for j in range(sideLength):
        for i in range(sideLength):
            X[i][j] = M[i][j] - B[i][j]
            if (X[i][j] > (3 * S[i][j])):
                F[i][j] = 1
                feature1 += 1
    feature2, feature3 = connectedComponents(X, len(X))
    return [feature1, feature2, feature3]

def oneDA_twoDA(L):
    assert(sideLength**2 == len(L))
    X = [[0 for i in range(sideLength)] for j in range(sideLength)]
    for j in range(sideLength):
        for i in range(sideLength):
            X[i][j] = L[i*sideLength + j]
    return X


def teachFeatureVector(Vector, value):
    Vector.append(value)
    return Vector

