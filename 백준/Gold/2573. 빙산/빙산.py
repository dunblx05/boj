from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(s_x, s_y, visited):
  queue = deque()
  queue.append((s_x, s_y))
  
  visited[s_x][s_y] = True
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if ice[nx][ny] != 0 and visited[nx][ny] == False:
        visited[nx][ny] = True
        queue.append((nx, ny))
      elif ice[nx][ny] == 0:
        count[x][y] += 1
  
  return 1      
        
        
n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]
time = 0

while 1:
  count_ice = []
  count = [[0 for _ in range(m)] for _ in range(n)]
  visited = [[False for _ in range(m)] for _ in range (n)]
  
  for i in range(n):
    for j in range(m):
      if visited[i][j] == False and ice[i][j] != 0:
        count_ice.append(bfs(i, j, visited))
        
  for i in range(n):
    for j in range(m):
      if count[i][j] != 0:
        ice[i][j] -= count[i][j]
        if ice[i][j] < 0:
          ice[i][j] = 0
  
  if len(count_ice) == 0:
    print(0)
    break
  elif len(count_ice) >= 2:
    print(time)
    break
  
  time += 1