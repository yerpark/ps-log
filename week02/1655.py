import sys

n = int(sys.stdin.readline())

inputVal = [ int(sys.stdin.readline()) for _ in range(n)]

heapList = []

def heapPop():
    if (len(heapList) == 0):
        return (0)
    else :
        heapList[0], heapList[len(heapList) - 1] = heapList[len(heapList) - 1], heapList[0]
        res = heapList.pop()
        myHeapify(0)
        return (res)

def myHeapify(idx):
    if (idx >= 0 and len(heapList) // 2 >= idx):

        largestIdx = idx
        leftIdx = 2 * idx + 1
        rightIdx = 2 * idx + 2
        
        if (leftIdx < len(heapList) and heapList[largestIdx] < heapList[leftIdx]):
            largestIdx = leftIdx
        if (rightIdx < len(heapList) and heapList[largestIdx] < heapList[rightIdx]):
            largestIdx = rightIdx
        
        if (largestIdx != idx):
            heapList[largestIdx], heapList[idx] = heapList[idx], heapList[largestIdx]
            myHeapify(largestIdx)


def insertHeap(val):
    heapList.append(val)
    idx = len(heapList) - 1
    while idx > 0:
        parentIdx = (idx - 1) // 2
        if (heapList[parentIdx] < heapList[idx]) :
            heapList[parentIdx], heapList[idx] = heapList[idx], heapList[parentIdx]
            idx = parentIdx
        else :
            break

def getMidVal(midRank):
    if (len(heapList) == 1 or len(heapList) == 2) :
        return (heapList[len(heapList) - 1])
    
    rank = 1 
    currIdx = 0

    while (True):
        




for i in inputVal :
    insertHeap(i)
