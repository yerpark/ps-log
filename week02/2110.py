import sys

def isAllocationPossible(minLenToAllocate, n, c, house):
    routerCount = 1
    last = house[0] #첫번째 원소에 라우터를 배치함. 배치 안하면 중간 애들이 좁혀지기 때문임 
    
    for idx in range(1, n) :
        if (minLenToAllocate <= house[idx] - last) :
            routerCount += 1
            last = house[idx]
            if (routerCount >= c):
                return (True)
    return (False)



if __name__ == "__main__" :
    n, c = map(int, sys.stdin.readline().split())
    house = [ int(sys.stdin.readline().strip()) for _ in range(n) ]
    house.sort()

    leftLen = 1 #실제로 직접 구할 수도 있겠지만, 번거롭기 때문에 일반적인 좌표와 좌표 사이의 최소 거리를 가져옴
    rightLen = house[n - 1] - house[0] #적어도 주어진 좌표에서의 최대 간격은 마지막원소에서 첫번째 원소 좌표를 뺀 간격 (정렬했다는 가정하에)
    maxLen = 1

    while (leftLen <= rightLen) :
        midLen = (rightLen + leftLen) // 2
        if (isAllocationPossible(midLen, n, c, house) == True) :
            leftLen = midLen + 1
            maxLen = max(maxLen, midLen)
        else :
            rightLen = midLen - 1
    
    print(maxLen)
        
    
    
