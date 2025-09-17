import sys
from collections import deque

if __name__ == "__main__":
    myQueue = deque()
    resList = []

    n, k = map(int, sys.stdin.readline().split())

    for i in range(1, n + 1):
        myQueue.append(i)

    while (len(myQueue) > 0):
        for _ in range(k - 1):
            if (len(myQueue) > 1):
                myQueue.append(myQueue.popleft())
            else:
                break
        resList.append(myQueue.popleft())

    print("<", end="")
    for i in range(n):
        print(resList[i], end="")
        if (i != n - 1):
            print(", ", end="")
    print(">")
