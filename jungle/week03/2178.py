#인접 -> 상하좌우만 가능
#bfs의 기본 적용
#경로 전체 저장 X implicit way로
#현재 방문 노드와 거리를 큐에 저장하고, 방문 여부는 visited 배열로 관리

import sys
from collections import deque

#상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    arr = []
    for _ in range(n):
        valStr = sys.stdin.readline().strip()
        tmp = []
        for i in range(len(valStr)):
            tmp.append(int(valStr[i]))
        arr.append(tmp)
    
    myQueue = deque()
    myQueue.append([0, 0, 1])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while (len(myQueue) != 0):
        curr = myQueue.popleft()

        if (curr[0] == n - 1 and curr[1] == m - 1):
            print(curr[2])
            break

        for i in range(4):
            # 배열 범위인지 체크
            nr = curr[0] + dr[i]
            nc = curr[1] + dc[i]
            if (nr < 0 or nr > n - 1 or nc < 0 or nc > m - 1):
                continue
            
            if (visited[nr][nc] == True):
                continue

            if (arr[nr][nc] == 1):
                visited[nr][nc] = True
                myQueue.append([nr, nc, curr[2] + 1])