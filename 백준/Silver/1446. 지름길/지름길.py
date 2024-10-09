import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(s):
    heap = []
    distance[s] = 0
    heappush(heap, (distance[s], s))
    
    while heap:
        cur_dist, cur_node = heappop(heap)
        
        if cur_dist > distance[cur_node]:
            continue
        
        for node in highway[cur_node]:
            cost = cur_dist + node[1]

            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heappush(heap, (cost, node[0]))


n, d = map(int, input().split())
highway = [[] for _ in range(d + 1)]
INF = 10e9
distance = [INF for _ in range(d + 1)]

for i in range(d):
    highway[i].append((i + 1, 1))
    
for i in range(n):
    s, e, l = map(int, input().split())
    if e > d:
        continue
    highway[s].append((e, l))
    
dijkstra(0)

print(distance[d])