#실외 area에 실내의 노드가 몇개 연결되어있는지를 확인해보자 
#실내->실외->실내를 경로 순서대로 탐색하는게 아님
#결국 path라는건 실내 -> 연결된 실외 area -> 실내기 때문에 
#실외 area에 연결된 실내 장소들을 알아내면 경로를 구할 수 있음

import sys
sys.setrecursionlimit(10**6)

def dfs(start, adjList, placeInfo, visited):
    #goal : 연결된 실내 장소 cnt
        #하면서 연결된 실외도 visited 바꿔주기 -> 다음 탐색에서 탐색안하게
    visited[start] = True
    cnt = 0

    for neighbor in adjList[start]:
        if (visited[neighbor] == True):
            continue
        
        if (placeInfo[neighbor - 1] == '0'):
            cnt += dfs(neighbor, adjList, placeInfo, visited)
        else:
            cnt += 1 #해도 되는 이유?? 트리로 연결되어있으니까. 만약에 간선이 n - 1개가 아니면 이러면 안됨
    return cnt


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    placeInfo = sys.stdin.readline().strip()
    adjList = {i:[] for i in range(1, n + 1)}
    visited = [False] * (n + 1)

    for _ in range(n - 1):
        start, dest = map(int, sys.stdin.readline().split())
        adjList[start].append(dest)
        adjList[dest].append(start)
    
    pathCnt = 0 

    #실내-실내 연결된 애들 먼저 확인해줌
        #why?우리가 볼 실외area에 연결된 경로랑은 다른 케이스니까
        #visited 처리 X - 인접한 경로만 확인하면 됨 
    #실외 area 확인 

    for i in range(1, n + 1):
        #실내 - 실내
        if (placeInfo[i - 1] == '1'):
            for neighbor in adjList[i]:
                if (placeInfo[neighbor - 1] == '1'):
                    pathCnt += 1
        #실외 area에 붙어 있는 실내 
        elif (placeInfo[i - 1] == '0' and visited[i] != True):
            indoor = dfs(i, adjList, placeInfo, visited)
            pathCnt += (indoor * (indoor - 1))

    print(pathCnt)