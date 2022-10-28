

def connectedComponents(X, n):
    connectedComp = 0
    m = len(X[0])
    max_len = 0
    visited = [[0 for i in range(8)] for j in range(8)]
    for i in range(n):
        for j in range(m):
            if (not visited[i][j]):
                c = X[i][j]
                count = 0
                DFS(X, i, j, c, n, m, count, visited)
                max_len = max(count, max_len)
                connectedComp += 1
    return (connectedComp, max_len)


def DFS(M, row, col, c, n, m, count, visited):
    rowNbr = [-1, 1, 0, 0, -1, -1, 1, 1]
    colNbr = [0, 0, 1, -1, -1, 1, -1, 1]
    visited[row][col] = True
    count += 1
    for k in range(8):  #checks 8 neighbours
        if (valid(M, row + rowNbr[k], col + colNbr[k], c, n, m, visited)):
            DFS(M, row + rowNbr[k], col + colNbr[k], c, n, m, count, visited)


def valid(M, row, col, c, n, m, visited):
    if (not ((row >= 0 and row < n) and (col >= 0 and col < m))):
        return False
    return (M[row][col] == c and not visited[row][col])
