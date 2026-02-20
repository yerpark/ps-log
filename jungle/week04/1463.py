import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    dp = [0] * (n + 1)
    dp[1] = 0
    for a in range(2, 4):
        if (a <= n):
            dp[a] = 1
    for i in range(4, n + 1):
        val1 = val2 = val3 = n + 1
        val1 = dp[i - 1] + 1
        if (i % 2 == 0):
            val2 = dp[i // 2] + 1
        if (i % 3 == 0):
            val3 = dp[i // 3] + 1
        
        dp[i] = min(val1, val2, val3)

    print(dp[n])