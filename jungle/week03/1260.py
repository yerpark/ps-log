import sys
from collections import deque
sys.setrecursionlimit(10**6)

# 그래프를 adjacent list 로 구현합시다. 
# 간선을 받으면 양방향이기 때문에 두 원소의 리스트에다가 각각 두개 추가 


class   Graph():
        def __init__(self):
            self.nodes = []
            self.edgeList = {}

        def addNode(self, val):
            if val not in self.nodes:
                self.nodes.append(val)
        
        def addEdges(self, val1, val2):
            self.edgeList[val1].append(val2)
            self.edgeList[val2].append(val1)

        def makeNodeWithN(self, n):
            for i in range(1, n + 1):
                self.addNode(i)
                self.edgeList[i] = []
                


def     printDFS(myGraph, node, visitedList):
        if len(myGraph.edgeList[node]) == 0:
            return None
        
        for next in myGraph.edgeList[node]:
            if next not in visitedList:
                visitedList.append(next)
                print(f"{next} ", end="")
                printDFS(myGraph, next, visitedList)


def     printBFS(myGraph, node):
        visited = [node]
        myQueue = deque()
        myQueue.append(node)

        while (len(myQueue) != 0):
            currnode = myQueue.popleft()
            for child in myGraph.edgeList[currnode]:
                if child not in visited:
                    visited.append(child)
                    myQueue.append(child)
                    print(f"{child} ", end="")
             

if      __name__ == "__main__":
        n, m, v = map(int, sys.stdin.readline().split())
        myGraph = Graph()
        myGraph.makeNodeWithN(n)

        for _ in range(m):
            val1, val2 = map(int, sys.stdin.readline().split())
            myGraph.addEdges(val1, val2)
        
        myGraph.nodes.sort()

        for node in myGraph.nodes:
            myGraph.edgeList[node].sort()

        print(f"{v} ", end="")
        printDFS(myGraph, v, [v])
        print("")
        print(f"{v} ", end="")
        printBFS(myGraph, v)
        print("")




