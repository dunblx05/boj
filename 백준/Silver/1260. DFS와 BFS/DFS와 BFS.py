from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, node, visited):
  queue = deque()
  queue.append(node)
  visited[node] = True

  while queue:
    x = queue.popleft()
    print(x, end = ' ')
    for i in graph[x]:
      if visited[i] == False:
        queue.append(i)
        visited[i] = True

def dfs_recursion(graph, node, visited):
  visited_dfs[node] = True
  
  print(node, end = ' ')

  for i in graph[node]:
    if not visited[i]:
      dfs_recursion(graph, i, visited)

def dfs_stack(graph, node, visited):
  stack = [node]

  while stack:
    x = stack.pop()
    if visited[x] == True:
      continue
    
    visited[x] = True
    print(x, end = ' ')
    
    # 거꾸로 탐색해야함
    for i in reversed(graph[x]):
      if visited[i] == False:
        stack.append(i)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited_bfs = [False] * (n + 1)
visited_dfs = [False] * (n + 1)

for i in range(m):
  s, e = map(int, input().split())

  # 양방향 그래프
  graph[s].append(e)
  graph[e].append(s)

# 작은 정점 먼저 출력
for i in graph:
  i.sort()

dfs_stack(graph, v, visited_dfs)
# dfs_recursion(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)