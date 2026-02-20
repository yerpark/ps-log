import sys

inputVal = list(map(int, sys.stdin.readline().split()))
inputArr = list(map(int, sys.stdin.readline().split()))

for i in range(0, 10) :
    if (inputArr[i] < inputVal[1]) :
        print(str(inputArr[i]), end="")
    if (i != 9) :
        print(end="")