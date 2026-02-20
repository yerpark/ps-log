#dp 배열 -> dp[visited][end]
    #비트마스킹 사용

import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    arr = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]

    # 점화식 세우자 
    # 어찌되었건 중요한 것은 다음에 방문할 도시와 현재 도시 
    # 이 정보 값을 알고 있어야 함l; 
    # 근데 그러면 row와 col을 어떻게 관리하지 ? 
    # 내가 지금 비트마스크를 row로 써야하는 것을 알아서 쓸 수 있지만 .. 
    # 왜 현재 있는 도시가 col이 되야 할까?
        # 그냥 visited만 가지고는 cost를 정확하게 모름
        # 계속 guessing해야 함 
        # 경우에 따라서는 방문을 못할 수도 있음
        # 따라서 현재 위치에 있는 도시를 col로 관리 
        # 근데 내가 이거 나중에 일주일 뒤에 혼자 생각해낼 수 있을까 ?

    dp = [ [sys.maxsize] * n for _ in range(1 << n) ]
    dp[1][0] = 0

    for visited in range(1 << n):
        for currCity in range(n):
            if (visited & (1 << currCity) != 0):
                for nextCity in range(n):
                    if (visited & (1 << nextCity) == 0 and arr[currCity][nextCity] != 0):
                        dp[visited | (1 << nextCity)][nextCity] = min(
                            dp[visited | (1 << nextCity)][nextCity], 
                            dp[visited][currCity] + arr[currCity][nextCity]
                        )
    
    res = sys.maxsize
    for i in range(1, n):
        if arr[i][0] != 0:
            res = min(res, dp[(1 << n) - 1][i] + arr[i][0])
    
    print(res)

    