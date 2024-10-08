import sys
import heapq

input = sys.stdin.readline
INF = 10e9


def dijkstra(start, index):
    heap = []
    distance[index][start] = 0
    heapq.heappush(heap, (distance[index][start], start))

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)

        if distance[index][cur_node] < cur_dist:
            continue

        for node in field[cur_node]:
            if cur_dist + node[1] < distance[index][node[0]]:
                distance[index][node[0]] = cur_dist + node[1]
                heapq.heappush(heap, (cur_dist + node[1], node[0]))


n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
field = [[] for _ in range(n + 1)]
distance = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

ans = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    field[a].append([b, l])
    field[b].append([a, l])

for i in range(1, n + 1):
    dijkstra(i, i)

for i in range(n + 1):
    res = 0
    for j in range(n + 1):
        if distance[i][j] <= m:
            res += items[j]

    if res > ans:
        ans = res

print(ans)
