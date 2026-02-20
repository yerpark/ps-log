# 뱀의 몸을 큐로 관리해야 하는 이유
    # 2차원 배열로 관리하면 꼬리가 줄어들면 다음 꼬리는 어느 방향인지 모름, 탐색을 해야 함
    # 그래도 visited 2차원 배열로 다음 행선지가 뱀의 몸인지 아닌지 구분해야 할 듯

# 다음 목적지가 뱀의 몸 혹은 벽인지 검사
    # 몸이면
        # 종료, x 프린트
    # 몸이 아니면
        # 사과가 있었다면 -> 다음 목적지 뱀으로 만들기, 큐에 넣기, visited 체크
        # 없다면 -> 큐에서 하나 빼서 visited도 빼기 
    # 방향 전환은 ? 이것도 큐에 넣어서 .. 빼자 .. 
        # 방향전환해야하는지 확인 .. 이동전에 

import sys
from collections import deque

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    k = int(sys.stdin.readline().strip())

    apple = [ [False] * (n + 1) for _ in range(n + 1) ]
    for _ in range(k):
        appleRow, appleCol = map(int, sys.stdin.readline().split())
        apple[appleRow][appleCol] = True

    l = int(sys.stdin.readline().strip())

    dirChange = deque()

    for _ in range(l):
        dirChange.append(sys.stdin.readline().split())
        dirChange[-1][0] = int(dirChange[-1][0])
    
    tail = deque()
    snake = [ [False] * (n + 1) for _ in range(n + 1) ]

    # 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    di = 1 #현재 방향 인덱스는 우 

    tail.append((1, 1))
    snake[1][1] = True
    timeCnt = 0

    row = 1
    col = 1

    while (tail):
        timeCnt += 1
        if (dirChange and timeCnt == dirChange[0][0] + 1):
            #방향 바꿔야 함
            if (dirChange[0][1] == "D"):
                di = (di + 1) % 4
            elif (dirChange[0][1] == "L"):
                di = (di - 1) % 4
            dirChange.popleft()

        row += dr[di]
        col += dc[di]

        if (row <= 0 or n < row or col <= 0 or n < col or snake[row][col] == True):
            break 

        if (apple[row][col] == True):
            apple[row][col] = False
        else:
            tmp = tail.popleft()
            snake[tmp[0]][tmp[1]] = False

        tail.append((row, col))
        snake[row][col] = True

    print(timeCnt)


        

