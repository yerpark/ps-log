import sys

c = (int)(sys.stdin.readline().strip())

for _ in range(c) :
    inputVal = list(map(int, sys.stdin.readline().split()))
    sumVal = 0
    for i in range(1, inputVal[0] + 1) :
        sumVal += inputVal[i]
    average = sumVal / inputVal[0]
    studentCnt = 0
    for i in range(1, inputVal[0] + 1) :
        if (average < inputVal[i]) :
            studentCnt += 1
    print(f"{(studentCnt / inputVal[0]) * 100 :.3f}%")
        