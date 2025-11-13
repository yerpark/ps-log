import sys

def dfs(startNode, adjList, placeInfo):
    cnt = 0

    # 갈 수 있는 경로에 대해서 반복문으로 탐색 시작
    # 해당 노드가 실외면 dfs 진행
    # 실내면 cnt += 1
    
    # [틀린 이유]
        # 처음에는 내가 거친 노드의 수를 다 세게 만들었나?? 했는데 문제는 그게 아니였다
        # 이러면 이게 둘 다 연결되어 있다 보니까 시작점도 카운트가 됨. 
            # 2-> 1->2가 완결된 path라고 잘못 cnt하는 것
    # [해결장법]
        # 그러면 절대적인 시작점을 하나 파라미터로 넘겨서 해당 노드인 경우에는 안가게 막자

    for neighbor in adjList[startNode]:
        if (placeInfo[neighbor - 1] == '0'):
            cnt += dfs(neighbor, adjList, placeInfo)
        else:
            print(f"{startNode}->{neighbor}")
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
            tmp =  dfs(i, adjList, placeInfo)
            print(f"{i}: {tmp}")
            pathCnt += tmp

    print(pathCnt)