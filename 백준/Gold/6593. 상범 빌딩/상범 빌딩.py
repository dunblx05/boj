from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(graph, s_z, s_x, s_y, visited):
  queue = deque()
  queue.append((s_z, s_x, s_y))
  
  while queue:
    z, x, y = queue.popleft()
    
    if z == ez and x == ex and y == ey:
      return f"Escaped in {visited[z][x][y]} minute(s)."
    
    for i in range(6):
      nz = z + dz[i]
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or ny < 0 or nz < 0 or nx >= r or ny >= c or nz >= l:
        continue
      if graph[nz][nx][ny] == '#':
        continue
      if (graph[nz][nx][ny] == '.' or graph[nz][nx][ny] == 'E') and visited[nz][nx][ny] == 0:
        visited[nz][nx][ny] = visited[z][x][y] + 1
        queue.append((nz, nx, ny))
  return "Trapped!"


while 1:
  # 층, 세로, 가로
  l, r, c = map(int, input().split())
  
  if l == 0 and r == 0 and c == 0:
    break
  
  building = [[] * r for _ in range(l)]
  visited = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
  
  for i in range(l):
    for j in range(r):
      building[i].append(list(map(str, input().strip())))
    temp = input()
    
  for i in range(l):
    for j in range(r):
      for k in range(c):
        if building[i][j][k] == 'S':
          sz = i
          sx = j
          sy = k
        
        if building[i][j][k] == 'E':
          ez = i
          ex = j
          ey = k
  
  print(bfs(building, sz, sx, sy, visited))