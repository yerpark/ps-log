import sys, heapq

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    weightHq = []
    heightHq = []
    infoList = []
    rankList = [0] * (n)

    for _ in range(n):
        weight, height = map(int, sys.stdin.readline().split())
        infoList.append([weight, height])
        heapq.heappush(weightHq, [-1 * weight, height])
        heapq.heappush(heightHq, [-1 * height, weight])

    rankCnt = 0
    while weightHq and heightHq :
        weightRankFront = heapq.heappop(weightHq)
        weightRankFront[0] *= -1
        heightRankFront = heapq.heappop(heightHq)
        heightRankFront[0] *= -1
        if (weightRankFront[0] == heightRankFront[1] and weightRankFront[1] == heightRankFront[0]):
            rankCnt += 1
            for i in range(n):
                if (infoList[i] == weightRankFront):
                    rankList[i] = rankCnt
                    break
        else:
            foundCnt = 0
            for i in range(n):
                if (infoList[i] == weightRankFront):
                    rankList[i] = rankCnt
                    foundCnt += 1
                elif (infoList[i][0] == heightRankFront[1] and infoList[i][1] == heightRankFront[0]):
                    rankList[i] = rankCnt
                    foundCnt += 1
                if (foundCnt == 2):
                    break
    
    while weightHq:
        weightRankFront = heapq.heappop(weightHq)
        weightRankFront[0] *= -1
        rankCnt += 1
        for i in range(n):
            if (infoList[i] == weightRankFront):
                rankList[i] = rankCnt
                break

    while heightHq:
        heightRankFront = heapq.heappop(heightHq)
        heightRankFront[0] *= -1
        rankCnt += 1
        for i in range(n):
            if (infoList[i][0] == heightRankFront[1] and infoList[i][1] == heightRankFront[0]):
                rankList[i] = rankCnt
                break

    for a in rankList:
        print(f"{a}", end="")
        
    
    #어떻게 하면 불필요한 반복을 줄이면서 원래 순서는 유지하고 등수를 구할 수 있을까