import sys
import heapq

class   Graph:
    def __init__(self, n):
        self.adjList = { i: [] for i in range(1, n + 1) }
    
    def makeConnection(self, start, end, cost):
        self.adjList[start].append((end, cost))
    
def     dijkstra(graph, start, n):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        curCost, curNode = heapq.heappop(pq)

        if dist[curNode] < curCost:
            continue

        for neighbor, cost in graph.adjList[curNode]:
            newCost = curCost + cost
            if newCost < dist[neighbor]:
                dist[neighbor] = newCost
                heapq.heappush(pq, (newCost, neighbor))
        
    return dist

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    m = int(input())
    myGraph = Graph()

    for _ in range(m):
        start, end, cost = map(int, input().split())
        myGraph.makeConnection(start, end, cost)

    startCity, destCity = map(int, input().split())

    dist = dijkstra(myGraph, startCity, n)
    print(dist[destCity])

