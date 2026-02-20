# 연속된 3개의 계단을 모두 밟으면 안되는 조건을 치환
    # i가 연속구간에 있는지 아닌지로 판단 

    # 연속구간인 경우
        # dp[i] = dp[i-3] + arr[i] + arr[i - 1]
    # 아닌 경우
        # dp[i] = dp[i-2] + arr[i]

import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    arr = [ int(sys.stdin.readline().strip()) for _ in range(n)]

    dp = [0] * n

    if n <= 2:
        print (sum(arr))
    else:
        dp[0] = arr[0]
        dp[1] = dp[0] + arr[1]
        dp[2] = max(arr[1] + arr[2], arr[0] + arr[2])

        for i in range(3, n):
            dp[i] = max(dp[i - 3] + arr[i] + arr[i - 1], dp[i - 2] + arr[i])
        
        print(dp[n-1])