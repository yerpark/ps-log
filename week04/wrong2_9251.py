import sys


if __name__ == "__main__":
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()

    dp = [ [0] * (len(str2) + 1) for _ in range(len(str1) + 1) ]

    i = len(str1) - 1
    j = len(str2) - 1

    while (i >= 0 and j >= 0):
        if (str1[i] == str2[j]):
            dp[i][j] = dp[i + 1][j + 1] + 1
            i -= 1
            j -= 1
        else:
            val1 = dp[i+1][j]
            val2 = dp[i][j + 1]
            if (val1 >= val2):
                i -= 1
                dp[i][j] = val1
            else:
                j -= 1
                dp[i][j] = val2
            

    print(dp[0][0])