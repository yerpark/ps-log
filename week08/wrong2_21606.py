import sys

# [문제점] : visited 체크를 안해서 무한 방문 

def dfs(startNode, curNode, adjList, placeInfo):
    cnt = 0

    # 갈 수 있는 경로에 대해서 반복문으로 탐색 시작
    # 해당 노드가 실외면 dfs 진행
    # 실내면 cnt += 1 (단, 이웃노드가 경로의 시작점이 아닌 경우에만)

    for neighbor in adjList[curNode]:
        if (placeInfo[neighbor - 1] == '0'):
            cnt += dfs(startNode, neighbor, adjList, placeInfo)
        elif (neighbor != startNode):
            cnt += 1
    
    return (cnt)

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    placeInfo = sys.stdin.readline().strip()
    adjList = {i:[] for i in range(1, n + 1)}

    for _ in range(n - 1):
        start, dest = map(int, sys.stdin.readline().split())
        adjList[start].append(dest)
        adjList[dest].append(start)
    
    pathCnt = 0

    # 실내인 곳에서만 출발해서 cnt. 탐색은 dfs로
    # 모든 노드에 대해 탐색
        # 실내 장소면
            # dfs 시작 
                # 다른 실내 장소를 만나면 탐색 종료 1 리턴
                # 전체 dfs를 재귀로 돌려서 이 반환값들을 더함 

    for i in range(1, n + 1):
        if (placeInfo[i - 1] == '1'):
            tmp =  dfs(i, i, adjList, placeInfo)
            pathCnt += tmp

    print(pathCnt)