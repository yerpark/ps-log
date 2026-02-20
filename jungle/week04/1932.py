#가장 어려운 점 .. 이 피라미드를 배열에 어떻게 넣을 것인지
#넣기만 하면 괜찮은데 
#입력 배열이 그냥 이차원 배열로 주어지니까 그 안에서 어떻게 자식과 부모의 관계를 맺을지 보면 ㄱㅊ을듯
#리프노드에서부터 올라가면서 더했을때 가장 최고가 되는 애를 저장
#부모 후보 중에서 

import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    arr = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    dp = arr[n - 1].copy()
    dp.append(0)

    for len in range(n - 1, 0, -1):
        for i in range(len):
            dp[i] = max(dp[i], dp[i + 1]) + arr[len - 1][i]
    
    print(dp[0])


    