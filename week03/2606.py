import sys
from collections import deque

#connected components 문제

class graph():
    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.ccSet = []
    
    def addNodes(self, n):
        for i in range(1, n + 1):
            self.nodes.append(i)
            self.edges[i] = []
    
    def addEdge(self, val1, val2):
        self.edges[val1].append(val2)
        self.edges[val2].append(val1)
    
    def makeCCSet(self):
        mySet = None
        for a in self.nodes:
            isThereMySetFlag = False
            for iSet in self.ccSet:
                if a in iSet:
                    mySet = iSet
                    isThereMySetFlag = True
                    break
            if isThereMySetFlag == False:
                self.ccSet.append(set([a]))
                mySet = self.ccSet[-1]
            
            q = deque()

            for neighbor in self.edges[a]:
                if neighbor not in mySet:
                    q.append(neighbor)
                    mySet.add(neighbor)
            
            while (len(q) != 0):
                curr = q.popleft()

                for neighbor in self.edges[curr]:
                    if neighbor not in mySet:
                        q.append(neighbor)
                        mySet.add(neighbor)

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())

    myGraph = graph()
    myGraph.addNodes(n)

    for _ in range(m):
        val1, val2 = map(int, sys.stdin.readline().split())
        myGraph.addEdge(val1, val2)
        
    myGraph.makeCCSet()

    print(len(myGraph.ccSet[0]) - 1)    