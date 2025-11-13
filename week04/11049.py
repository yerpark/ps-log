import sys

def function1():
    n = int(sys.stdin.readline())

    r = [0] * n
    c = [0] * n

    for i in range(n):
        r[i], c[i] = map(int, sys.stdin.readline().split())

    dp = [[0] * n for _ in range(n)]
    #dp[startIdx][endIdx] 

    for multipleSize in range(2, n + 1):
        for startIdx in range((n - multipleSize) + 1):
            minCost = sys.maxsize
            endIdx = startIdx + multipleSize - 1
            for midIdx in range(startIdx, endIdx):
                cost = dp[startIdx][midIdx] + dp[midIdx + 1][endIdx] +  r[startIdx] * c[midIdx] * c[endIdx]
                if (minCost > cost):
                    minCost = cost
            dp[startIdx][endIdx] = minCost
    
    return (dp[0][n - 1])

print(function1())