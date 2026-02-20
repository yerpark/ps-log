n, m = 7, 8
edges = [ [] for _ in range(n + 1) ]
visited = [False] * (n + 1)
reversed_order = []

# 주어진 간선 정보 (x,y)
# x -> y로 향하는 간선이 있다는 뜻

given_edges = [
    (-1, -1),
    (1, 2),
    (1, 3),
    (1, 4),
    (3, 6),
    (3, 5),
    (6, 2),
    (2, 5),
    (5, 7)
]

#그래프를 인접리스트로 표현
for i in range(1, m + 1):
    x, y = given_edges[i]
    edges[x].append(y)

#DFS 탐색을 진행합니다.
def dfs(x):
    # x에서 갈 수 있는 모든 곳을 탐색합니다.
    # 단, 방문한 적이 없는 경우에만 진행합니다.
    for y in edges[x]:
        if not visited[y]:
            visited[y] = True
            dfs(y)
    
    #퇴각 직전에 현재 노드 번호를 넣어줍니다.
    reversed_order.append(x)

#DFS 탐색을 진행합니다.
#단, 방문표시가 되지 않은 모든 곳을 시작으로 하여 DFS를 진행해야 합니다.
for i in range(1, n + 1):
    if not visited[i]:
        visited[i] = True
        dfs(i)

#위상정렬 순서대로 출력합니다.
#거꾸로 출력해주면 됩니다.
for num in reversed_order[::-1]:
    print(num, end="")
