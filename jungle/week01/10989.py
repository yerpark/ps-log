import sys

n = int(input())

arr = [int(sys.stdin.readline()) for x in range(n)]

def     heapify(startIdx, size) :

    largestIdx = startIdx

    leftIdx = startIdx * 2 + 1
    rightIdx = startIdx * 2 + 2

    if (leftIdx < size and arr[leftIdx] > arr[largestIdx]) :
        largestIdx = leftIdx
    
    if (rightIdx < size and arr[rightIdx] > arr[largestIdx]):
        largestIdx = rightIdx
    
    if (largestIdx != startIdx) :
        arr[startIdx], arr[largestIdx] = arr[largestIdx], arr[startIdx]
        heapify(largestIdx, size)

def     heap_sort():
    
    for i in range(n // 2 - 1, -1, -1) :
        heapify(i, n)

    size = n
    for i in range(n-1, 0, -1): 
        arr[0], arr[i] = arr[i], arr[0]
        size -= 1
        heapify(0, size)   

heap_sort()

for i in range(n) :
    print(arr[i])