#adj list 구성
#bfs 방식으로 탐색
    #queue에 들어있는 정보는 2개
        # 이전 방문 노드
        # 현재 거리 
    # 거리 == 2 이면 탐색 종료하고 print
#최단거리니까 방문 여부를 확인해야함 

import sys
from collections import deque

class   graph():
    def __init__(self):
        self.nodes=[]
        self.adjList = {}

    def makeNodes(self, n):
        for i in range(1, n + 1):
            self.nodes.append(i)
            self.adjList[i] = []
    
    def makeEdge(self, val1, val2):
        self.adjList[val1].append(val2)
    
if __name__ == "__main__":
    n, m, k, x = map(int, sys.stdin.readline().split())

    myGraph = graph()
    myGraph.makeNodes(n)

    for _ in range(m):
        val1, val2 = map(int, sys.stdin.readline().split())
        myGraph.makeEdge(val1, val2)
    
    myQueue = deque()
    myQueue.append([x, 0])
    resList = []
    visited = [False] * n
    visited[x - 1] = True

    while (myQueue):
        curr = myQueue.popleft()

        if (curr[1] >= k):
            resList.append(curr[0])
            continue

        for a in myGraph.adjList[curr[0]]:
            if (visited[a - 1] == False):
                visited[a - 1] = True
                myQueue.append([a, curr[1] + 1])
    
    if (len(resList) == 0):
        print(-1)
    else:
        resList.sort()
        for city in resList:
            print(city) 
