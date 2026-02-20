
import sys, heapq

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())

    for _ in range(t):
        n = int(sys.stdin.readline().strip())

        cvRanks = []

        for _ in range(n):
            cvScore, interviewScore = map(int, sys.stdin.readline().split())

            heapq.heappush(cvRanks, (cvScore, interviewScore))
        
        lastCvRank = sys.maxsize
        lastInterviewRank = sys.maxsize
        cnt = 0
        while(cvRanks):
            curr = heapq.heappop(cvRanks)

            if (curr[0] < lastCvRank or curr[1] < lastInterviewRank):
                cnt += 1
                lastCvRank = min(lastCvRank, curr[0])
                lastInterviewRank = min(lastInterviewRank, curr[1])

        print(cnt)