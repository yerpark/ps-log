import sys

if __name__ == "__main__" :
    n = int(sys.stdin.readline().strip())

    for _ in range(n):
        inputVal = sys.stdin.readline().strip()
        myStack = []

        for i in range(len(inputVal)) :
            if (inputVal[i] == "(") :
                myStack.append("(")
            else :
                if (len(myStack) == 0) :
                    print("NO")
                    break 
                myStack.pop()
        else :
            if (len(myStack) != 0) :
                print("NO")
            else :
                print("YES")
        