from math import sqrt
from helper import *
from collections import deque

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier

# Global Variables
sideLength = 8
queueLength = 10
pixelCount = 64
backgroundQueue = [deque([]) for i in range(pixelCount)]
measuresOfDispersion = [[0, 0] for i in range(pixelCount)]   # index 0 has sum and 1 has sum of squares

def initBackground(M):
    global sideLength, queueLength, pixelCount, backgroundQueue, measuresOfDispersion
    for _ in range(queueLength):
        x = deque()         
        l = deque()
        for j in range(sideLength):
            for i in range(sideLength):
                l.append(M[i][j])
                index = i*sideLength + j
                measuresOfDispersion[index][0] += M[i][j]
                measuresOfDispersion[index][1] += (M[i][j]**2)
                x.append(l)
    backgroundQueue = x


            
# takes M = currentthermalmap
#       B = thermalmap of background
#       S = stddeviation
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

            mean = measuresOfDispersion[index][0] / len(backgroundQueue[index])
            secondmoment = measuresOfDispersion[index][1] / len(backgroundQueue[index])
            S[i][j] = sqrt(secondmoment - (mean**2))




# takes M = currentthermalmap
#       B = thermalmap of background
#       S = stddeviation
# returns feature vector
def extractFeatureVector(M, B, S):
    X = [[0 for i in range(sideLength)] for j in range(sideLength)]
    Factive = [[0 for i in range(sideLength)] for j in range(sideLength)] # Active Points 
    feature1 = 0
    for j in range(sideLength):
        for i in range(sideLength):
            X[i][j] = M[i][j] - B[i][j]
            if (abs(X[i][j] > (4 * S[i][j]))):
                Factive[i][j] = 1
                feature1 += 1
    feature2,feature3 = connectedComponents(Factive, len(Factive))
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



# Training Part

Mvals = []
y_train = []

with open("data.txt","r") as f:
    X = f.readlines()
    for x in X:
        x_list = ([float(i) for i in x[1:][:-2].split(',')])
        Mvals.append(x_list)

with open("people.txt","r") as f:
    Y = f.readlines()
    for y in Y:
        y_train.append(int(y))


for i in range(len(Mvals)):
    Mvals[i] = oneDA_twoDA(Mvals[i])
S = [[0 for i in range(sideLength)] for j in range(sideLength)]
# initBackground(Mvals[0])
B = []
for i in range(10):
    updateBackground(Mvals[i],B,S)
# print(backgroundQueue[-1])
B = Mvals[0]


V = []
for i in range(len(Mvals)):
    v = extractFeatureVector(Mvals[i],B,S)
    V.append(np.array(v))
V = np.array(V)

print(V)

plt.figure(figsize = (10,10))
ax = plt.axes(projection = '3d')
ax.scatter3D(V[:,0], V[:,1], V[:,2], c=np.array(y_train))
plt.show()

knn5 = KNeighborsClassifier(n_neighbors = 5)
knn1 = KNeighborsClassifier(n_neighbors=1)
knn5.fit(V, y_train)
knn1.fit(V, y_train)

X_test = []
y_test = []

with open("testdata.txt","r") as f:
    X = f.readlines()
    for x in X:
        x_list = ([float(i) for i in x[1:][:-2].split(',')])
        X_test.append(x_list)

print("X_test = ",X_test)

for i in range(len(X_test)):
    X_test[i] = oneDA_twoDA(X_test[i])

V = []
for i in range(len(X_test)):
    v = extractFeatureVector(X_test[i],B,S)
    V.append(np.array(v))
V = np.array(V)

X_test = V
print(X_test)

with open("testpeople.txt","r") as f:
    Y = f.readlines()
    for y in Y:
        y_test.append(int(y))

y_pred_5 = knn5.predict(X_test)
y_pred_1 = knn1.predict(X_test)

print("y_pred_5 = ", y_pred_5)
print("y_pred_1 = ", y_pred_1)

from sklearn.metrics import accuracy_score
print("Accuracy with k=5", accuracy_score(y_test, y_pred_5)*100)
print("Accuracy with k=1", accuracy_score(y_test, y_pred_1)*100)
