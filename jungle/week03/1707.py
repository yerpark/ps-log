#아이디어 : 간선에서 분리하고 그걸로 만족하는지 dfs 탐색하자
    #간선을 다 넣어
    # 첫번째 노드의 간선으로부터 분리 작업 실행
    #list 두개 들고 다님
    # 간선을 탐색하면서 조건을 만족하지만 집합 3개를 안만들고도 분리가 되는지 확인
    #맞으면 1 리턴 아니면 0 리턴

import sys

class   graph():
    def __init__(self):
        self.nodes = []
        self.adjList = {}
    
    def makeNodes(self, n):
        for i in range(1, n + 1):
            self.nodes.append(i)
            self.adjList[i] = []
    
    def makeEdge(self, val1, val2):
        self.adjList[val1].append(val2)
        self.adjList[val2].append(val1)

    def doDfs(self, start, mySet, startSetIndex):
        # 종료조건 . . 
        if (len(mySet[0]) + len(mySet[1]) == len(self.nodes)):
            return True

        for neighbor in self.adjList[start]:
            if neighbor not in mySet[0] and neighbor not in mySet[1]:
                for child in self.adjList[neighbor]:
                    if child in mySet[(startSetIndex + 1) % 2]:
                        return False
                mySet[(startSetIndex + 1) % 2].append(neighbor)
                if (self.doDfs(neighbor, mySet, (startSetIndex + 1) % 2) == False):
                    mySet[(startSetIndex + 1) % 2].remove(neighbor)

        return False


if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())

    for _ in range(t):
        v, e = map(int, sys.stdin.readline().split())

        myGraph = graph()
        myGraph.makeNodes(v)

        for _ in range(e):
            val1, val2 = map(int, sys.stdin.readline().split())
            myGraph.makeEdge(val1, val2)

        if (myGraph.doDfs(1, [[1], []], 0) == True):
            print("YES")
        else:
            print("NO")