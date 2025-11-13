
#빨리 끝나는 순서대로 .. 

import sys
import heapq

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    myPQ = []
    for _ in range(n):
        startTime, endTime = map(int, sys.stdin.readline().split())
        heapq.heappush(myPQ, (endTime, startTime))

    lastTime = 0
    meetingCnt = 0
    while (myPQ):
        curr = heapq.heappop(myPQ)
        if (lastTime <= curr[1]):
            meetingCnt += 1
            lastTime = curr[0]
    
    print(meetingCnt)

