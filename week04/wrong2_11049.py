import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    arr = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
    
    dp = [[0] * n for _ in range(n + 1)]

    #idx 0 행은 무시 . 그냥 들어가는 값임 

    #첫번째 dp 테이블 행 채우기
    for first in range(n - 1):
        dp[2][first] = arr[first][0] * arr[first][1] * arr[first + 1][1]
    
    for multipleSize in range(3, n + 1):
        
        for first in range(n - multipleSize + 1):
            minCnt = float('inf')
            for firstSize in range(1, multipleSize):
                firstVal = arr[first][0]
                midVal = arr[first + firstSize - 1][1]
                endVal = arr[first + multipleSize - 1][1]
                cost = firstVal * midVal * endVal + dp[firstSize][first] + dp[multipleSize - firstSize][first + firstSize]
                if cost < minCnt :
                    minCnt = cost

            dp[multipleSize][first] = minCnt
    
    print(dp[n][0])
    