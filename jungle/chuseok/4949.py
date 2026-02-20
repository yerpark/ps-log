import sys

if __name__ == "__main__":
    while(True):
        inputStr = sys.stdin.readline().rstrip("\n")

        if (inputStr == "."):
            break

        myStack = []
        resStr = "no"
        noProblemFlag = True

        for i in range(len(inputStr)):
            if inputStr[i] == "(" or inputStr[i] == "[":
                myStack.append(inputStr[i])
            elif inputStr[i] == ")":
                if (len(myStack) == 0 or myStack.pop() != "("):
                    noProblemFlag = False
                    break
            elif inputStr[i] == "]":
                if (len(myStack) == 0 or myStack.pop() != "["):
                    noProblemFlag = False
                    break
            elif inputStr[i] == ".":
                break
        
        if (noProblemFlag and len(myStack) == 0):
            resStr = "yes"
        
        print(resStr)