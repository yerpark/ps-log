from collections import deque
import sys

if __name__ == "__main__" :
    myQueue = deque()

    n = int(sys.stdin.readline().strip())

    for _ in range(n):
        operation = sys.stdin.readline().split()

        if (operation[0] == "push"):
            myQueue.append(int(operation[1]))
        elif (operation[0] == "pop"):
            if (len(myQueue) == 0):
                print(-1)
            else:
                print(myQueue.popleft())
        elif (operation[0] == "size"):
            print(len(myQueue))
        elif (operation[0] == "empty"):
            if (len(myQueue) == 0):
                print(1)
            else:
                print(0)
        elif (operation[0] == "front"):
            if (len(myQueue) == 0):
                print(-1)
            else:
                print(myQueue[0])
        elif (operation[0] == "back"):
            if (len(myQueue) == 0):
                print(-1)
            else:
                print(myQueue[len(myQueue) - 1])