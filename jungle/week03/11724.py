import sys
from collections import deque

class graph():
    def __init__(self):
        self.nodes = []
        self.ccSet = []
        self.edges = {}

    def addNode(self, val):
        if val not in self.nodes:
            self.nodes.append(val)
        
        if val not in self.edges:
            self.edges[val] = []
    
    def addEdge(self, val1, val2):
        self.addNode(val1)
        self.addNode(val2)
        
        self.edges[val1].append(val2)
        self.edges[val2].append(val1)
    
    def makeConnectedComponents(self):
        #노드 집합에서 하나씩 꺼냄
        #만약 그게 ccSet에 있으면
            #그 연결집합을 가지고 탐색 시작
            #아니면, 새로운 연결 집합 만들기
        #일단 다 연결되었는지 아닌지는 나중에 확인
        mySet = None
        for a in self.nodes:
            isItInCCSetflag = False
            for iSet in self.ccSet:
                if a in iSet:
                    mySet = iSet
                    isItInCCSetflag = True
                    break

            if (isItInCCSetflag == False):
                self.ccSet.append(set([a]))
                mySet = self.ccSet[-1]

            q = deque()
            
            for neighbor in self.edges[a]:
                if neighbor not in mySet:
                    q.append(neighbor)
                    mySet.add(neighbor)
            
            while (len(q) != 0):
                x = q.popleft()
                for neighbor in self.edges[x]:
                    if neighbor not in mySet:
                        q.append(neighbor)
                        mySet.add(neighbor)



if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    myGraph = graph()

    for _ in range(m):
        val1, val2 = map(int, sys.stdin.readline().split())
        myGraph.addEdge(val1, val2)

    for num in range(1, n+1):
        myGraph.addNode(num)

    #연결 집합 만들기
    #요소들이 첫번째 원소와 연결되었는지 확인
    # 다른 집합과 연결되지 않은거 확인 - 첫번째 원소끼리 비교.
        #이래도 되는 이유: 각자 연결된게 확실하면 한 원소끼리만 확인하면 됨 
        #연결이 되었다면 어떻게서든 연결이 되었을 것 
    
    myGraph.makeConnectedComponents()

    #연결 요소 확인
    print(len(myGraph.ccSet))