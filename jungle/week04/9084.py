#배열 하나만 써서 bottom up 

import sys

if __name__ == "__main__":

    t = int(sys.stdin.readline().strip())

    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        coins = list(map(int, sys.stdin.readline().split()))
        targetVal = int(sys.stdin.readline().strip())

        dp = [0] * (targetVal + 1)
        dp = 1
        
        for coin in coins:
            for val in range(coin, targetVal + 1):
                dp[val] += dp[val - coin]
        
        print(dp[targetVal])
