from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start_x, start_y, visited):
  queue = deque()
  queue.append((start_x, start_y))
  visited[start_x][start_y] = True
  
  count = 1
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      
      if graph[nx][ny] == 0:
        continue
      
      if graph[nx][ny] == 1 and visited[nx][ny] == False:
        visited[nx][ny] = True
        queue.append((nx, ny))
        count += 1
  
  return count
  
t = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(t):
  m, n, k = map(int, input().split())
  field = [[0 for _ in range(m)] for _ in range(n)]
  visited = [[False for _ in range(m)] for _ in range(n)]
  veg_arr = []
  
  for _ in range(k):
    a, b = map(int, input().split())
    field[b][a] = 1
    
  
  for i in range(n):
    for j in range(m):
      if field[i][j] == 1 and visited[i][j] == False:
        veg = bfs(field, i, j, visited)
        veg_arr.append(veg)
  
  print(len(veg_arr))