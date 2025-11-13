#스택을 사용해서 괄호 관리
    # 스택에 뭔가가 남아있다면 계속 곱하고 
    # 아니면 더하기 

import sys
from collections import deque

if __name__ == "__main__":
    inputStr = sys.stdin.readline().strip()
    myStack = []
    res = 0
    tmpRes = 1
    
    for i in range(len(inputStr)):
        if (inputStr[i] == '(' or inputStr[i] == '['):
            myStack.append(inputStr[i])
            if (i != 0 and inputStr[i - 1] == ")" or inputStr[i - 1] == "]"):
                res += tmpRes
                tmpRes = 1

        elif (inputStr[i] == ')'):
            if (len(myStack) == 0 or myStack.pop() != '('):
                res = 0
                break
            tmpRes *= 2
            
        elif (inputStr[i] == ']'):
            if (len(myStack) == 0 or myStack.pop() != '['):
                res = 0
                break
            tmpRes *= 3

        else:
            res = 0
            break

    print(res)