#일단 그래프 만들고 
# 그 다음에 1부터 순회 돌면서 출력

import sys
sys.setrecursionlimit(10**6)

class graph():
    def __init__(self):
        self.nodes = []
        self.adjList = {}
        self.parent = {}
        self.visited = [False] * n
    
    def makeNodes(self, n):
        for i in range(1, n + 1):
            self.nodes.append(i)
            self.adjList[i] = []
            self.parent[i] = []

    def makeEdge(self, val1, val2):
        self.adjList[val1].append(val2)
        self.adjList[val2].append(val1)

    def doDFS(self, start):
        self.visited[start - 1] = True

        for a in self.adjList[start]:
            if self.visited[a - 1] != True:
                self.parent[a].append(start)
                self.doDFS(a)

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    myGraph = graph()
    myGraph.makeNodes(n)

    for _ in range(n - 1):
        val1, val2 = map(int, sys.stdin.readline().split())
        myGraph.makeEdge(val1, val2)
    
    myGraph.doDFS(1)
    
    for i in range(2, n + 1):
        print(myGraph.parent[i][0])