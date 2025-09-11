



import sys

sys.setrecursionlimit(10**6) 
n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 상 하 좌 우 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

maxDepth = max(arr[0])
for i in range(1, n) :
    maxDepth = max(maxDepth, max(arr[i]))

def checkFourWay(row, col, depth) :
    visited[row][col] = True

    for i in range(4) :
        nr = row + dr[i]
        nc = col + dc[i]
        if (0 <= nr < n and 0 <= nc < n) :
            if not visited[nr][nc] and arr[nr][nc] > depth :
                checkFourWay(nr, nc, depth)

def checkFourWay(row, col, depth) :
    if (arr[row][col] <= depth) :
        visited[row][col] = True
        return True

    if (visited[row][col] == True) :
        return True
    
    visited[row][col] = True

    for i in range(4) :
        if (0 <= row + dr[i] and row + dr[i] < n and 0 <= col + dc[i] and col + dc[i] < n):
            checkFourWay(row + dr[i], col + dc[i], depth)
    




maxCnt = 0

for depth in range(maxDepth + 1): 
    visited = [ [False] * n for _ in range(n)]
    tmpCnt = 0
    for row in range(n) :
        for col in range(n) :
            if (visited[row][col] == True) :
                continue 
            if (arr[row][col] <= depth) :
                visited[row][col] = True
                continue
            # print(f"depth:{depth} row:{row} col:{col}")
            checkFourWay(row, col, depth)
            tmpCnt += 1

    maxCnt = max(maxCnt, tmpCnt)

print(maxCnt)