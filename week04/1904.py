#처음부터 크기가 n일때 만들 수 있는 경우의 수를 다 배열에 기록
#해당 배열에서 작은 subproblem으로 계산
#경우의 수는 크게 두개로 나눔 1을 사용하냐 안사용하냐 
    # 1 사용 - 크기 n -1 인 경우의 수 더하기
    # 1 사용 X - 크기 n -2 인 경우의 수 더하기

import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    dp = [0, 1, 2, 3, 5]

    for i in range(5, n + 1):
        dp.append((dp[i - 2] + dp[i - 1]) % 15746)

    print(dp[n])