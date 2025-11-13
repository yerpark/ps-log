import sys
from collections import deque

class graph():
    def __init__(self, n):
        self.citys = []
        for i in range(1, n+1):
            self.citys.append(i)
        
        self.adjList = {}

        for i in range(1, n+1):
            self.adjList[i] = []

    
    def makeConnection(self, start, end, cost):
        self.adjList[start].append([end, cost])

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    myGraph = graph(n)

    for _ in range(m):
        start, end, cost = map(int, sys.stdin.readline().split())
        myGraph.makeConnection(start, end, cost)
    
    startCity, destCity = map(int, sys.stdin.readline().split())
    
    if (startCity == destCity):
        print(0)
    else:
        myQueue = deque()

        for a in myGraph.adjList[startCity]:
            myQueue.append(a)

        minCost = float('inf')

        while (myQueue):
            cur = myQueue.popleft()

            if (cur[0] == destCity):
                minCost = min(minCost, cur[1])
                continue

            for a in myGraph.adjList[cur[0]]:
                tmp = [a[0], a[1]]
                tmp[1] += cur[1]
                myQueue.append(tmp)
        
        print(minCost)




    