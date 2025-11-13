import sys

#항상 최선의 선택을 했다고 가정 . . 
#왜냐면 (AB)C든 A(BC)든 행렬의 결과는 똑같으니까
#두 케이스를 비교해서 dp table을 채우면 된다.

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    arr = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
    if (n // 2 == 0):
        dp = [0]
    else:
        dp = [0] * (n // 2)

    lastRow = arr[0][0]
    lastCol = arr[0][1]
    for i in range(0, n, 2):
        if (i == n - 1):
            break
        elif (i + 1 == n - 1):
            dp[i//2] = (lastRow * lastCol * arr[i + 1][1]) + dp[(i//2) - 1]
        else:
            res1 = (lastRow * lastCol * arr[i + 1][1]) + (lastRow * arr[i+2][0] * arr[i+2][1])
            res2 = (lastCol * arr[i + 1][1] * arr[i + 2][1]) + (lastRow * lastCol * arr[i + 2][1])
            dp[i//2] = min(res1, res2)
            if (i != 0):
                dp[i//2] += dp[(i//2) - 1]
            lastCol = arr[i + 2][1]
    
    print(max(dp))