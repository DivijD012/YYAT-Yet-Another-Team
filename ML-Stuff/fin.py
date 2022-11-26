from constants import *
from helper import ListtoString,oneDA_twoDA

def TakeThermalData(filename):
    DataArray = [] # Array of arrays of size 64
    with open(filename,"r") as f:
        for line in f.readlines():
            DataArray.append(oneDA_twoDA(ListtoString(line)))
    return DataArray

def TakeGroundTruth(filename):
    DataArray = [] # Array of integers
    with open(filename,"r") as f:
        for line in f.readlines():
            DataArray.append(int(line))
    return DataArray

def RemoveErroneous(ThermalDataArray, GroundTruthDataArray):
    assert(len(ThermalDataArray) == len(GroundTruthDataArray))
    arrayLength = len(ThermalDataArray)
    NewThermalDataArray  = []
    NewGroundTruthDataArray = []
    for i in range(arrayLength):
        if(GroundTruthDataArray[i] == -1):
            continue
        NewThermalDataArray.append(ThermalDataArray[i])
        NewGroundTruthDataArray.append(GroundTruthDataArray[i])
    return NewThermalDataArray, NewGroundTruthDataArray

