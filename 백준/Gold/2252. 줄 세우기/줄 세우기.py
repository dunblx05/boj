from collections import deque
import sys
input = sys.stdin.readline

def topological_sort():
  result = []
  queue = deque([])

  for i in range(1, n + 1):
    if indegree[i] == 0:
      queue.append(i)
  
  while queue:
    x = queue.popleft()

    result.append(x)

    for i in graph[x]:
      indegree[i] -= 1

      if indegree[i] == 0:
        queue.append(i)
  
  return result

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
ans  = []


for _ in range(m):
  start, end = map(int, input().split())
  indegree[end] += 1
  graph[start].append(end)

ans = topological_sort()

print(*ans)