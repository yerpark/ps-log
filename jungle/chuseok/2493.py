import sys

if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())
    towers = list(map(int, sys.stdin.readline().split()))
    myStack = [(1, towers[0])]

    print("0 ", end="")

    for i in range(1, n):

        while (myStack and myStack[-1][1] < towers[i]):
            myStack.pop()
        
        if (myStack):
            print(f"{myStack[-1][0]} ", end="")
        else:
            print("0 ", end="")
        
        myStack.append((i + 1, towers[i]))
    