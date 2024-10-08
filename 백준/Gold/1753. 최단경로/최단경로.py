import sys
import heapq

input = sys.stdin.readline
INF = 10e9


def dijkstra(start):
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (distance[start], start))

    while heap:
        cur_dist, node = heapq.heappop(heap)

        if distance[node] < cur_dist:
            continue

        for next_node in graph[node]:
            if cur_dist + next_node[1] < distance[next_node[0]]:
                distance[next_node[0]] = cur_dist + next_node[1]
                heapq.heappush(heap, (cur_dist + next_node[1], next_node[0]))


V, E = map(int, input().split())
k = int(input())
graph = [[] for _ in range(V + 1)]
distance = [INF for _ in range(V + 1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

dijkstra(k)

for i in distance[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)
