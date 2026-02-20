import sys

a, b, v = map(int, sys.stdin.readline().split())

dayCnt = ((v - a) // (a - b)) + 1

if (dayCnt * a - (dayCnt - 1) * b < v) :
    dayCnt += 1
        
print (dayCnt)