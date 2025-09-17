import sys

if __name__ == "__main__" :
    n = int(sys.stdin.readline().strip())
    myStack = []

    for _ in range(n) :
        operationList = sys.stdin.readline().split()

        if (operationList[0] == "push") :
            myStack.append(operationList[1])
        elif (operationList[0] == "pop") :
            if (len(myStack) == 0) :
                print(-1)
            else :
                print(myStack.pop())
        elif (operationList[0] == "size") :
            print(len(myStack))
        elif (operationList[0] == "empty") :
            if (len(myStack) == 0) :
                print(1)
            else :
                print(0)
        elif (operationList[0] == "top") :
            if (len(myStack) == 0) :
                print (-1)
            else :
                print(myStack[len(myStack) - 1])
    