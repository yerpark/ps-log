#dp 테이블 구성
    #row: R,G,B 3개
    #col: 집 idx (n번집)
    #val: 1번부터 채워나갔을 때의 최소 비용
    #이 집이 해당 Row색을 칠하는 경우, 안 칠하는 경우를 비교 
    #두 경우는 각각 2가지의 경우가 있음
    #앞에서부터 채워나감

import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    costArr = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    dp = [ [0] * n for _ in range(3)]

    #0 빨 1 초 2 파 
    dp[0][0] = costArr[0][0]
    dp[1][0] = costArr[0][1]
    dp[2][0] = costArr[0][2]

    #0-base, i번째집 -> 1base에선 i + 1
    for i in range(1, n):
        
        for color in range(3):
            dp[color][i] = costArr[i][color] + min(dp[(color + 1) % 3][i - 1], dp[(color + 2) % 3][i - 1])
    
    print(min(dp[0][n - 1], dp[1][n - 1], dp[2][n - 1]))


    