from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(graph):
  
  while queue:
    z, x, y = queue.popleft()
    
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
      
      if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
        continue
      if graph[nz][nx][ny] == -1:
        continue
      if graph[nz][nx][ny] == 0:
        queue.append((nz, nx, ny))
        graph[nz][nx][ny] = graph[z][x][y] + 1
  

m, n, h = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
answer = 0

queue = deque()

for k in range(h):
  for i in range(n):
    for j in range(m):
      if tomatoes[k][i][j] == 1:
        queue.append((k, i, j))
      
bfs(tomatoes)

for i in tomatoes:
  for j in i:
    for k in j:
      if k == 0:
        print(-1)
        
        exit(0)
    answer = max(answer, max(j))

print(answer-1)