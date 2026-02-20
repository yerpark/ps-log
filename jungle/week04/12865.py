#dp 테이블 채우기
    # 물건 인덱스 번호가 row
    # 무게가 col
    # 내용이 value

import sys

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    objects = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    dp = [0] * (k + 1) #dp[k]로 바로 볼 수 있게

    for object in objects:
        for weight in range(k, object[0] -1, -1): #이것도 object[0]만큼 weight += object[0]하니까 틀림
            dp[weight] = max(dp[weight], object[1] + dp[weight - object[0]])
    
    print(max(dp))


