import sys

arr = list(map(int, sys.stdin.readline().split()))

min = arr[0]

if (arr[1] < min) :
    min = arr[1]

if (arr[3] - arr[1] < min) :
    min = arr[3] - arr[1]

if (arr[2] - arr[0] < min) :
    min = arr[2] - arr[0]

print (min)