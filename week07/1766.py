import sys, heapq

# 그냥 위상정렬 순서대로 탐색하고 그 순서대로 출력하면 되는 문제 

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    edges = [ map(int, sys.stdin.readline().split()) for _ in range(m) ]
    adjList = { key:[] for key in range(1, n + 1) }
    indegree = [0] * (n + 1)
    pq = []

    for i in range(m):
        start, dest = edges[i]
        adjList[start].append(dest)
        indegree[dest] += 1
    
    for i in range(1, n + 1):
        if (indegree[i] == 0):
            heapq.heappush(pq, i)
        adjList[i].sort()
    
    while(pq):
        cur = heapq.heappop(pq)
        
        for dest in adjList[cur]:
            indegree[dest] -= 1
            if (indegree[dest] == 0):
                heapq.heappush(pq, dest)

        print(f"{cur} ", end="")
    