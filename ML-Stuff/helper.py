from constants import SIDELENGTH
import numpy as np

def ListtoString(liststring):
    return [float(i) for i in liststring[1:][:-2].split(',')]

def oneDA_twoDA(L):
    assert(SIDELENGTH**2 == len(L))
    X = [[0 for i in range(SIDELENGTH)] for j in range(SIDELENGTH)]
    for j in range(SIDELENGTH):
        for i in range(SIDELENGTH):
            X[i][j] = L[i*SIDELENGTH + j]
    return X

def twoDA_oneDA(L):
    assert(SIDELENGTH == len(L))
    assert(SIDELENGTH == len(L[0]))
    X = []
    for i in range(SIDELENGTH):
        for j in range(SIDELENGTH):
            X.append(L[i][j])
    assert(SIDELENGTH**2 == len(X))
    return X
    
def Array_NumpyArray(A):
    NP = []
    for i in A:
        NP.append(np.array(i))
    NP = np.array(NP)

    return NP