import sys


if __name__ == "__main__":
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()

    dp = [ [0] * (len(str2) + 1) for _ in range(len(str1) + 1) ]

    for i in range(len(str1) -1, -1, -1):
        for j in range(len(str2) - 1, -1, -1):
            if (str1[i] == str2[j]):
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    
    print(dp[0][0])