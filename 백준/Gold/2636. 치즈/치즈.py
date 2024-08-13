from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(graph, s_x, s_y, visited):
  queue = deque()
  queue.append((s_x, s_y))
  
  melt = deque()

  visited[s_x][s_y] = True

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if visited[nx][ny] == False:
        visited[nx][ny] = True
        
        if graph[nx][ny] == 0:
          queue.append((nx, ny))
        
        elif graph[nx][ny] == 1:
          melt.append((nx, ny))
    
  for m_x, m_y in melt:
    graph[m_x][m_y] = 0
  
  return len(melt)

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]
time = 0

while 1:

  cheese_count = 0
  visited = [[False for _ in range(m)] for _ in range(n)]
  melted_cheese = bfs(cheese, 0, 0, visited)
  
  time += 1

  for i in range(n):
    for j in range(m):
      if cheese[i][j] == 1:
        cheese_count += 1

  if cheese_count == 0:
    print(time)
    print(melted_cheese)
    break