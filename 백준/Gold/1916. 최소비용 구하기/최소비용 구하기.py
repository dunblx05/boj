import sys
import heapq

input = sys.stdin.readline
INF = 10e9


def dijkstra(start):
    heap = []
    # 시작점과 0 큐에 넣음
    heapq.heappush(heap, (0, start))  # 우선순위, 값
    dist[start] = 0

    while heap:
        d, node = heapq.heappop(heap)

        if dist[node] < d:
            continue

        for i in bus_info[node]:
            # 다음 도시까지의 비용이 현재 저장된 비용보다 적으면
            if d + i[1] < dist[i[0]]:
                # 값 갱신하기
                dist[i[0]] = d + i[1]
                heapq.heappush(heap, (d + i[1], i[0]))


n = int(input())
m = int(input())
bus_info = [[] for _ in range(n + 1)]

dist = [INF for _ in range(n + 1)]

for i in range(m):
    start, end, cost = map(int, input().split())
    bus_info[start].append((end, cost))

s, e = map(int, input().split())

dijkstra(s)

print(dist[e])
