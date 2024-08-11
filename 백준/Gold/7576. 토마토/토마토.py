from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(graph):
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if graph[nx][ny] == -1:
        continue
      if graph[nx][ny] == 0:
        queue.append((nx, ny))
        graph[nx][ny] = graph[x][y] + 1
  

m, n = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

queue = deque()


for i in range(n):
  for j in range(m):
    if tomatoes[i][j] == 1:
      queue.append((i, j))
      
bfs(tomatoes)

if all(0 not in l for l in tomatoes):
  print(max(map(max, tomatoes)) - 1)
else:
  print(-1)