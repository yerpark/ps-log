import sys

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    
    dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

    for _ in range(t):
        n = int(sys.stdin.readline().strip())

        if n <= len(dp):
            print(dp[n-1])
            continue

        for i in range(len(dp), n):
            dp.append(dp[i - 3] + dp[i - 2])
        
        print(dp[n - 1])
