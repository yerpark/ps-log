# 노드 val, 노드 실내 실외 값을 다 저장해야 할 듯
# 노드를 가지고 딕셔너리의 adj list를 구성해야 함
# 노드의 실내/실외 여부를 넣을 때 실내 리스트를 구성해서 만들어두기
# 실내 리스트에서 하나씩 꺼내면서 탐색 시작
    # 실내에서 바로 실내로 이어지면
    # 실내에서 실외로 이어지면 
        # 실내를 만나는 순간 탐색 종료 (cnt + 1)
        # 실내를 못만나면 0 반환 (cnt X)

import sys
from collections import deque

class graph():
    def __init__(self):
        self.nodes = {}
        self.adjList = {}
        self.indoorList = []
    
    def makeNodes(self, n, inputStr):
        for i in range(1, n+1):
            indoor = int(inputStr[i - 1])
            self.nodes[i] = indoor
            if (indoor == 1):
                self.indoorList.append(i)
            self.adjList[i] = []

    def makeEdge(self, val1, val2):
        self.adjList[val1].append(val2)
        self.adjList[val2].append(val1)

    def myDfs(self, start, path):
        res = 0
    
        for neighbor in self.adjList[start]:
            if neighbor in path:
                continue
            if neighbor not in self.indoorList:
                path = path + [neighbor]
                res += self.myDfs(neighbor, path)
            else:
                res += 1

        return res
    
    def searchIndoorToIndoor(self):
        # 재귀로 가야 .. 
        cnt = 0
        for a in self.indoorList:
            cnt += self.myDfs(a, [a])
        print(cnt)

    




if __name__ == "__main__":
    myGraph = graph()
    n = int(sys.stdin.readline().strip())
    inputStr = sys.stdin.readline().strip()

    myGraph.makeNodes(n, inputStr)
    
    for _ in range(n - 1):
        val1, val2 = map(int, sys.stdin.readline().split())
        myGraph.makeEdge(val1, val2)

    myGraph.searchIndoorToIndoor()


        