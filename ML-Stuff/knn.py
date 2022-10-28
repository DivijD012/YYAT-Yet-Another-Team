import numpy as np
import pandas as pd
from ml import *

import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier

X_train = []
y_train = []

with open("data.txt","r") as f:
    X = f.readlines()
    for x in X:
        x_list = ([float(i) for i in x[1:][:-2].split(',')])
        # x_np = np.array(x_list)
        X_train.append(x_list)

with open("people.txt","r") as f:
    Y = f.readlines()
    for y in Y:
        y_train.append(int(y))


# X_train = np.array(X_train)
# y_train = np.array(y_train)

# print(X_train)
# print(y_train)

for i in range(len(X_train)):
    X_train[i] = oneDA_twoDA(X_train[i])
B = X_train[0]
S = B
updateBackground(X_train[0],B,S)

V = []

for i in range(len(X_train)):
    v = extractFeatureVector(X_train[i],B,S)
    V.append(np.array(v))

V = np.array(V)

a = np.array([1,2,3,4,5,6])
b = np.array([1,2,4,3,4,6])
c = np.array([-1,2,3,4,5,0])

plt.style.use('seaborn')
plt.figure(figsize = (10,10))
ax = plt.axes(projection = '3d')
ax.scatter3D(V[:,0], V[:,1], V[:,2], c=y_train, marker= '*',edgecolors='black')
plt.show()

knn5 = KNeighborsClassifier(n_neighbors = 5)
knn1 = KNeighborsClassifier(n_neighbors=1)

knn5.fit(V, y_train)
knn1.fit(V, y_train)

# y_pred_5 = knn5.predict(X_test)
# y_pred_1 = knn1.predict(X_test)

# from sklearn.metrics import accuracy_score
# print("Accuracy with k=5", accuracy_score(y_test, y_pred_5)*100)
# print("Accuracy with k=1", accuracy_score(y_test, y_pred_1)*100)

# plt.figure(figsize = (15,5))
# plt.subplot(1,2,1)
# plt.scatter(X_test[:,0], X_test[:,1], c=y_pred_5, marker= '*', s=100,edgecolors='black')
# plt.title("Predicted values with k=5", fontsize=20)

# plt.subplot(1,2,2)
# plt.scatter(X_test[:,0], X_test[:,1], c=y_pred_1, marker= '*', s=100,edgecolors='black')
# plt.title("Predicted values with k=1", fontsize=20)
# plt.show()