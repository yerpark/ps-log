import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))

    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        j = 1
        prevIdx = i
        while (0 <= i - j):
            if (arr[i - j] < arr[i] and dp[prevIdx] < dp[i - j]):
                prevIdx = i - j
            j += 1
        dp[i] = dp[prevIdx] + 1
    
    print(max(dp))