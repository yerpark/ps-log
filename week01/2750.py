import sys

n = int(input())
arr = [int(sys.stdin.readline()) for _ in range(n)]

minIdx = 0
for i in range(n) :
    for j in range(i, n) :
        if (arr[minIdx] > arr[j]) :
            minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]

for i in range(n):
    print(arr[i])



