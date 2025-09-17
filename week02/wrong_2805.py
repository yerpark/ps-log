#일단 입력받은 나무 길이에 대해 정렬 필요
#필요 길이를 m 
#나무 자른 합을 sum이라고 두자
#max값에서 얼마나 부족한지 확인
#h를 하나씩 줄여나가면서 탐색 (초기:가장 큰 트리의 높이에서 하나 뺀 값)
#h 초과하는 bound idx를 이분탐색으로 받기
#그럼 거기서부터 반복문 돌면서 sum구하고 같거나 초과하면 반복 종료

import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

trees.sort()

def getCutStartIdx(trees, height, n):
    leftIdx = 0
    rightIdx = n - 1
    minIdx = n
    while (leftIdx <= rightIdx) :
        midIdx = (leftIdx + rightIdx) // 2
        
        if (trees[midIdx] > height) :
            rightIdx = midIdx - 1
            minIdx = min(minIdx, midIdx)
        else :
            leftIdx = midIdx + 1
    
    return (minIdx)

h = trees[n - 1] - 1

while (True) :
    sum = 0
    cutStartIdx = getCutStartIdx(trees, h, n)

    for i in range(cutStartIdx, n):
        sum += trees[i] - h
    
    if (sum >= m):
        break
    else:
        h -= 1

print(h)


# 시 간 초 과
    # h를 어떻게든 잘 줄여나가야 할 것 같은데 .. 
    # m / (전체 원소 개수)