from fin import *
from constants import *
import pprint
from features import *
import numpy as np
import matplotlib.pyplot as plt
from helper import *
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Take input from file

ThermalDataArray = TakeThermalData(THERMALDATAFILE)
GroundTruthDataArray = TakeGroundTruth(GROUNDTRUTHFILE)
ThermalDataArray, GroundTruthDataArray = RemoveErroneous(ThermalDataArray,GroundTruthDataArray)
pprint.pprint(ThermalDataArray)
pprint.pprint(GroundTruthDataArray)

# Extract features of that input

FeatureVectorArrays = [] 
for i in range(len(ThermalDataArray)):
    ActivePoints = GetActivePointsArray(ThermalDataArray[i],GroundTruthDataArray[i])
    FeatureVectorArrays.append(ExtractFeatures(ActivePoints))

pprint.pprint(FeatureVectorArrays)

NumpyFeatureVectorArray = Array_NumpyArray(FeatureVectorArrays)
NumpyGroundTruthValues = Array_NumpyArray(GroundTruthDataArray)

# --- Plotting ----
# Plot of Feature vectors with colours as classes(no of people)

SegregatedRaces = [[] for k in range(max(GroundTruthDataArray)+1)] 

for i in range(max(GroundTruthDataArray)):
    for j in range(len(FeatureVectorArrays)):
        if(GroundTruthDataArray[j] == i):
            SegregatedRaces[i].append(FeatureVectorArrays[j])

NumpySegregatedRaces = Array_NumpyArray(SegregatedRaces)
l = min([len(i) for i in SegregatedRaces if len(i) > 0])

plt.figure(figsize = (10,10))
ax = plt.axes(projection = '3d')
for i in range(max(GroundTruthDataArray)):
    scatter = ax.scatter3D(NumpySegregatedRaces[i][:l,0], NumpySegregatedRaces[i][:l,1], NumpySegregatedRaces[i][:l,2], c=COLOURS[i],depthshade=False)
    print(NumpySegregatedRaces[i][:2,0], NumpySegregatedRaces[i][:2,1], NumpySegregatedRaces[i][:2,2])
plt.show()

print(NumpySegregatedRaces)

# Training


TrainingSet = []
TestSet = []
TrainingGroundTruthValues = []
TestGroundTruthValues = []
for i,Race in enumerate(SegregatedRaces):
    x = int(RATIO * len(Race))
    TrainingSet += Race[:x]
    TestSet += Race[x:]
    TrainingGroundTruthValues += [i for i_ in range(x)]
    TestGroundTruthValues += [i for i_ in range(x,len(Race))]
TrainingSet = Array_NumpyArray(TrainingSet)
TestSet = Array_NumpyArray(TestSet)
TrainingGroundTruthValues = np.array(TrainingGroundTruthValues)
TestGroundTruthValues = np.array(TestGroundTruthValues)

print("TrainingSet = ",TrainingSet)
print("TestSet = ",TestSet )
print("X = ",TrainingGroundTruthValues); 
print("Y = ",TestGroundTruthValues )

for k in range(1,100):

    knn5 = KNeighborsClassifier(n_neighbors = k)
    knn1 = KNeighborsClassifier(n_neighbors=1)
    knn5.fit(TrainingSet,TrainingGroundTruthValues)
    knn1.fit(TrainingSet,TrainingGroundTruthValues)

    y_pred_5 = knn5.predict(TestSet)
    y_pred_1 = knn1.predict(TestSet)

    print("Accuracy with k={}".format(k), accuracy_score(TestGroundTruthValues, y_pred_5)*100)

# print("y_pred_5 = ", y_pred_5)
# print("y_pred_1 = ", y_pred_1)
# print("Accuracy with k=5", accuracy_score(TestGroundTruthValues, y_pred_5)*100)
# print("Accuracy with k=1", accuracy_score(TestGroundTruthValues, y_pred_1)*100)

# --- Linear Regression Part ---

# V_reg = []
# print((V_Test.size // V_Test[0].size))
# for i in range((V_Test.size // V_Test[0].size)):
#     if(y_test[i] == 0):
#         continue
#     newfvec = []
#     newfvec.append(V[i][0])
#     newfvec.append(V[i][2])
#     newfvec = np.array(newfvec)
#     V_reg.append(newfvec)
# V_reg = np.array(V_reg)
# print("V_reg = ",V_reg)

# y_test_reg = []
# for i in range(y_test.size):
#     if y_test[i] == 0 :
#         continue
#     y_test_reg.append(y_test[i])
# y_test_reg = np.array(y_test_reg)
# print("ytr = ",y_test_reg)

# with open("V.txt","w") as f:
#     print(V,file=f)

# with open("V_reg.txt","w") as f:
#     print(V_reg,file=f)

from sklearn.linear_model import LinearRegression
reg = LinearRegression().fit(TrainingSet, TrainingGroundTruthValues)
print("reg score = ",reg.score(TestSet, TestGroundTruthValues))
print("reg coeffs = ",reg.coef_)
print("reg intercept = ",reg.intercept_)