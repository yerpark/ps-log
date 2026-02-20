from collections import deque
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    myQueue = deque()

    for i in range(1, n + 1):
        myQueue.append(i)

    while (len(myQueue) > 1):
        myQueue.popleft()
        if (len(myQueue) == 1):
            break
        myQueue.append(myQueue.popleft())

    print(myQueue.popleft())

