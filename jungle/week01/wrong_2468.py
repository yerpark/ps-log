import sys

n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

maxDepth = max(arr[0])
for i in range(1, n) :
    maxDepth = max(maxDepth, max(arr[i]))

def checkRight(row, col, depth) :
    i = 0
    while (col + i < n and arr[row][col + i] > depth) :
        visited[row][col + i] = True
        i += 1
    if (col + i < n):
        visited[row][col + i] = True
        checkFourWay(row, col + i - 1, depth, "VERTICAL")

def checkLeft(row, col, depth):
    i = 0
    while(col - i >= 0 and arr[row][col - i] > depth) :
        visited[row][col - i] = True
        i +=1
    if (col - i >= 0) :
        visited[row][col - i] = True
        checkFourWay(row, col - i + 1, depth, "VERTICAL")

def checkUp(row, col, depth):
    i = 0
    while(row - i >= 0 and arr[row - i][col] > depth):
        visited[row - i][col] = True
        i += 1
    if (row - i >= 0):
        visited[row - i][col] = True
        checkFourWay(row - i + 1, col, depth, "HORIZONTAL")

def checkDown(row, col, depth): 
    i = 0
    while(row + i < n and arr[row + i][col] > depth) :
        visited[row + i][col] = True
        i += 1
    if (row + i < n) :
        visited[row + i][col] = True
        checkFourWay(row + i - 1, col, depth, "HORIZONTAL")


def checkFourWay(row, col, depth, state) :

    if (visited[row][col] == True) :
        return True

    if (state == "ALL") :
        checkRight(row, col, depth)
        checkLeft(row, col, depth)
        checkUp(row, col, depth)
        checkDown(row, col, depth)
    elif (state == "HORIZONTAL") :
        checkRight(row, col, depth)
        checkLeft(row, col, depth)
    elif (state == "VERTICAL"):
        checkUp(row, col, depth)
        checkDown(row, col, depth)





maxCnt = 0

#다 잠기거나 다 안잠기는건 의미 x 그래도 예외처리를 위해 일단
for depth in range(1, maxDepth + 1): 
    visited = [ [False] * n for _ in range(n)]
    tmpCnt = 0
    for row in range(n) :
        for col in range(n) :
            if (visited[row][col] == True) :
                continue 
            if (arr[row][col] <= depth) :
                visited[row][col] = True
                continue
            print(f"depth:{depth} row:{row} col:{col}")
            checkFourWay(row, col, depth, "ALL")
            tmpCnt += 1

    maxCnt = max(maxCnt, tmpCnt)

print(maxCnt)