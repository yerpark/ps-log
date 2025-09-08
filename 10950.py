import sys

t = (int)(sys.stdin.readline().strip())

for _ in range(t) :
    arr = list(map(int, sys.stdin.readline().split()))
    print (arr[0] + arr[1])