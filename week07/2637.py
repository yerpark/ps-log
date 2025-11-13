import sys
from collections import deque

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    
    indegree = [0] * (n + 1) #0 base 1base로 맞추려고
    adjList = { i:[] for i in range(1, n + 1)}
    componentsList = [ [0] * (n + 1) for _ in range(n + 1) ]
    myQueue = deque()

    for _ in range(m):
        x, y, k = map(int, sys.stdin.readline().split())
        adjList[y].append((x, k))
        indegree[x] += 1
    
    for i in range(1, n + 1):
        if (indegree[i] == 0):
            componentsList[i][i] = 1
            myQueue.append(i)
    
    while (myQueue):
        cur = myQueue.popleft()

        for dest in adjList[cur]:
            indegree[dest[0]] -= 1

            for i in range(1, n + 1):
                componentsList[dest[0]][i] += componentsList[cur][i] * dest[1]


            if (indegree[dest[0]] == 0):
                myQueue.append(dest[0])

    for i in range(1, n + 1):
        if (componentsList[n][i] != 0):
            print(f"{i} {componentsList[n][i]}")
        

