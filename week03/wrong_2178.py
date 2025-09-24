#인접 -> 상하좌우만 가능
#bfs의 기본적인 걸 적용 예정
    #경로를 큐에 넣고 마지막에서 꺼내서 탐색
    #나중에 최단거리큐를 구하기 

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
    myQueue.append([[0, 0]])
    completePath = None
    
    while (len(myQueue) != 0):
        path = myQueue.popleft()
        curr = path[-1]

        if (curr[0] == n - 1 and curr[1] == m - 1):
            completePath.append(path)
            break

        for i in range(4):
            # 배열 범위인지 체크
            nr = curr[0] + dr[i]
            nc = curr[1] + dc[i]
            if (nr < 0 or nr > n - 1 or nc < 0 or nc > m - 1):
                continue
            
            if ([nr, nc] in path):
                continue

            if (arr[nr][nc] == 1):
                tmpPath = list(path)
                tmpPath.append([nr, nc])
                myQueue.append(tmpPath)
    
    minLen = n * m + 1
    for path in completePath:
        minLen = min(len(path), minLen)

    print(minLen)