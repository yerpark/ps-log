#큰 동전부터 빼서 줄여나가기 
#입력받으면서 k 보다 작은 애의 인덱스 가지고 있기 

import sys

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())

    coins = []
    for i in range(n):
        coin = int(sys.stdin.readline().strip())
        coins.append(coin)
        if (coin <= k):
            maxIdx = i
        
    cnt = 0
    while (k > 0):
        cnt += (k //coins[maxIdx])
        k -= (coins[maxIdx] * (k //coins[maxIdx]))

        while (0 <= maxIdx and k < coins[maxIdx]):
            maxIdx -= 1
    
    print(cnt)
        