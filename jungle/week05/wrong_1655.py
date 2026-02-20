#우선순위 큐 두개를 써서 중간값 두개가 항상 앞에 오게끔 만들어서 푸는 문제
    #작은 수들을 담는 우선순위큐 -> 단, max heap으로 구현
    #큰 수들을 담는 우선순위큐 -> 단, min heap으로 구현

# 우선순위 큐에 들어가는 기준 
    # size 비교해서 작은 쪽에 넣기
        # 그냥 넣지 말고... 값비교해서 바꿔야 하면 바꾸자 
    # 같으면 smallAreaTop, bigAreaTop, cur 값 비교 


import sys, heapq

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    smallArea = [] # maxHeap
    bigArea = [] # minHeap

    val = int(sys.stdin.readline().strip())
    heapq.heappush(bigArea, val)
    print(val)
    
    for _ in range(n - 1):
        val = int(sys.stdin.readline().strip())

        if (len(smallArea) < len(bigArea)):
            if (bigArea[0] < val):
                res = bigArea[0]
                heapq.heappush(smallArea, -1 * heapq.heappop(bigArea))
                heapq.heappush(bigArea, val)
            else:
                heapq.heappush(smallArea, -val)
                res = -1 * smallArea[0]
        elif (len(smallArea) > len(bigArea)):
            if (val < -1 * smallArea[0]):
                heapq.heappush(bigArea, -1 * heapq.heappop(smallArea))
                heapq.heappush(smallArea, -val)
            else:
                heapq.heappush(bigArea, val)
            res = -1 * smallArea[0]
        else:
            if (val <= -1 * smallArea[0]):
                res = -1 * smallArea[0]
                heapq.heappush(smallArea, -val)
            elif (bigArea[0] <= val):
                res = bigArea[0]
                heapq.heappush(bigArea, val)
            else:
                res = val
                heapq.heappush(bigArea, val)
        
        print(res) 
        
