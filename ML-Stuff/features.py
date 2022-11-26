# We need to store background (8 x 8 Array)
# We need a function which calculates Standard deviation array (8 x 8 Array)
# To calculate the standard deviation ,
    # we calculate running sum and squaresum

from constants import *
import math

TotalBackgroundArrays = 0
RunningSumArray =  [[0 for i in range(SIDELENGTH)] for j in range(SIDELENGTH)]
RunningSquareSumArray =  [[0 for i in range(SIDELENGTH)] for j in range(SIDELENGTH)]
StandardDeviationArray = [[0 for i in range(SIDELENGTH)] for j in range(SIDELENGTH)]
# Hard Code Bachground here
BackgroundArray = [[0 for i in range(SIDELENGTH)] for j in range(SIDELENGTH)] 

def UpdateBackground(NewBackgroundArray):
    global BackgroundArray, StandardDeviationArray, RunningSquareSumArray, RunningSumArray, TotalBackgroundArrays
    assert(len(NewBackgroundArray) == SIDELENGTH)
    assert(len(NewBackgroundArray[0]) == SIDELENGTH)
    BackgroundArray = NewBackgroundArray
    TotalBackgroundArrays += 1

    for i in range(SIDELENGTH):
        for j in range(SIDELENGTH):
            RunningSumArray[i][j] += NewBackgroundArray[i][j]
            RunningSquareSumArray[i][j] += NewBackgroundArray[i][j] ** 2
            StandardDeviationArray[i][j] = RunningSquareSumArray[i][j] / TotalBackgroundArrays 
            StandardDeviationArray[i][j] -= (RunningSumArray[i][j] / TotalBackgroundArrays) ** 2
            StandardDeviationArray[i][j] = math.sqrt(StandardDeviationArray[i][j])  

            
def GetActivePointsArray(CurrentThermalData , GroundTruthValue):
    ActivePoints = [[0 for i in range(SIDELENGTH)] for j in range(SIDELENGTH)]
    if(GroundTruthValue == 0):
        UpdateBackground(CurrentThermalData)
        
    for i in range(SIDELENGTH):
        for j in range(SIDELENGTH):
            if(CurrentThermalData[i][j] - BackgroundArray[i][j] >= THRESHOLD * StandardDeviationArray[i][j]):
                ActivePoints[i][j] = 1
    return ActivePoints

    
def ExtractFeatures(ActivePoints):
    TotalActivePoints = 0
    TotalClusters = 0
    LargestClusterSize = 0
    assert(len(ActivePoints) == SIDELENGTH)
    assert(len(ActivePoints[0]) == SIDELENGTH) 

    visited = [[0 for i in range(SIDELENGTH)] for j in range(SIDELENGTH)]

    for i in range(SIDELENGTH):
        for j in range(SIDELENGTH):
            if(visited[i][j] == 1 or ActivePoints[i][j] == 0):
                continue
            print("(i,j) = (",i,",",j,")")
            ClusterSize = DFS(i,j,visited, ActivePoints)
            print("Clusterssize = ",ClusterSize)
            TotalClusters += 1
            LargestClusterSize = max(ClusterSize,LargestClusterSize)
            TotalActivePoints += ClusterSize

    return TotalActivePoints, TotalClusters, LargestClusterSize
    
def Valid(i,j):
    if not (i < SIDELENGTH and i >= 0):
        return False
    if not (j < SIDELENGTH and j >= 0):
        return False
    return True
            
def DFS(row,col,visited,ActivePoints):
    visited[row][col] = 1
    rowNbr = [-1, 1, 0, 0, -1, -1, 1, 1]
    colNbr = [0, 0, 1, -1, -1, 1, -1, 1]
    count = 1
    for i in range(len(rowNbr)):
        newrow = row + rowNbr[i]
        newcol = col + colNbr[i]
        if not Valid(newrow,newcol):
            continue
        if visited[newrow][newcol] == 1 or ActivePoints[newrow][newcol] == 0:
            continue
        count += DFS(newrow,newcol,visited ,ActivePoints)
    print([row,col,count])
    return count

if __name__ == '__main__':
    z =[[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0]]
    print(z)
    print(ExtractFeatures(z))
