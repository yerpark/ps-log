# 2253벉 문제 지금까지 내가 고민한 흔적들 .. 
# 1. 실제로 경우의 수를 가지치기를 하면서 
# 그림으로 그려보니 트리 구조로 보임 -> 재귀? 
# 2. 그리고 그 전 상태 
# (현재 점프수 -1 , 점프수, 점프수 + 1을 뺀 위치에서의 값들을 
# 최소 비교해서 최소값에 + 1 해주기만 하면 됨.
#      -> 이 말을 풀어서 해보면 못 밟는 돌이 있든 말든 그건 그 전의 상태에 맡기는 걸로 
# 3. 밟을 수 없는 애들 처리를 어떻게 해야 할ㅈ ㅣ 
# -> 경우의 수에서 하나하나 고려해서 값을 아예 안넣기? 아니면 inf 처리? 
# 근데 이러면 오버플로우는 안나나 ? 
# 4. 재귀함수에 점프수를 넘겨야 하나? 반복문으로 점프수 증가시켜가며 관리 ? 
# 5. 점프수 관리하는건 어떻게 해야하지? 만약 지금 점프수가 x면 x 점프가 일어날 수 있는 최소 지점을 닷 ㅣ계산해야 함 
# -> 1에서 바로 x 점프 할 수 없으니까.. 그래서 최소 시작위치를 구하려면 1+ 2 + 3 + 4 + .. + x -1 ?

import sys, math

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    notSteppable = [ int(sys.stdin.readline()) for _ in range(m) ]

    maxJump = int(math.sqrt(2 * n)) + 2
    dp = [ [sys.maxsize] * (maxJump + 1) for _ in range(n + 1) ]
    #dp[pos][jump] -> 현재 점프 수 
    dp[1][0] = 0

    for curr in range(1, n + 1):
        if (curr in notSteppable):
                continue
        for jump in range(maxJump + 1):
            if dp[curr][jump] == sys.maxsize:
                 continue

            for nextJump in [jump - 1, jump, jump + 1]:
                if nextJump <= 0 or maxJump < nextJump:
                    continue

                next = curr + nextJump
                
                if (next <= n and next not in notSteppable):
                    dp[next][nextJump] = min(dp[next][nextJump], dp[curr][jump] + 1)

    res = min(dp[n])
    if res == sys.maxsize:
        res = -1
    print (res)