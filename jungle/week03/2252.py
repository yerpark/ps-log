
# 진입차수 줄이고
    #진입차수 0인에들만 큐에 추가하기

import sys
from collections import deque

class graph():
    def __init__(self):
        self.nodes = []
        self.adjList = {}
        self.indegree = []

    def makeNodes(self, n):
        for i in range(1, n + 1):
            self.nodes.append(i)
            self.adjList[i] = []
        self.indegree = [0] * n
    
    def makeEdge(self, val1, val2):
        self.adjList[val1].append(val2)
        self.indegree[val2 - 1] += 1

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())

    myGraph = graph()
    myGraph.makeNodes(n)

    for _ in range(m):
        val1, val2 = map(int, sys.stdin.readline().split())
        myGraph.makeEdge(val1, val2)

    myQueue = deque()
    res = []

    for i in range(1, n + 1):
        if (myGraph.indegree[i - 1] == 0):
            myQueue.append(i)
    
    while (myQueue):
        curr = myQueue.popleft()
        res.append(curr)

        for neighbor in myGraph.adjList[curr]:
            if neighbor not in res:
                myGraph.indegree[neighbor - 1] -= 1
                if (myGraph.indegree[neighbor - 1] == 0):
                    myQueue.append(neighbor)
    
    print(" ".join(map(str, res)))