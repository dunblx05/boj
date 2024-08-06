from collections import deque

def bfs(graph, node, visited):
  queue = deque([node])
  visited[node] = True
  
  while queue:
    v = queue.popleft()

    for i in graph[v]:
      if visited[i] == False:
        queue.append(i)
        visited[i] = True

for tc in range(1, 11):
  t, n = map(int, input().split())
  lst = list(map(int, input().split()))
  graph = [[] for _ in range(100)]
  visited = [False] * 100

  for i in range(n):
    start = lst[i * 2]
    end = lst[i * 2 + 1]
    graph[start].append(end)

  bfs(graph, 0, visited)

  if visited[-1]:
    print(f"#{tc} 1")
  else:
    print(f"#{tc} 0")