from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(graph, s_x, s_y, visited):
  population = 0
  queue = deque()
  queue.append((s_x, s_y))

  union = []
  union.append((s_x, s_y))

  visited[s_x][s_y] = True

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
      if visited[nx][ny] == False and (l <= abs(graph[nx][ny] - graph[x][y]) <= r):

        visited[nx][ny] = True
        queue.append((nx, ny))
        union.append((nx, ny))

  if len(union) <= 1:
    return 0
  else:
    for x, y in union:
      population += graph[x][y]
      
    population = int(population / len(union))

    for x, y in union:
      graph[x][y] = population

    return 1



n, l, r = map(int, input().split())
land = [[0 for _ in range(n)] for _ in range(n)]
time = 0

for i in range(n):
  land[i] = list(map(int, input().split()))

visited = [[False for _ in range(n)] for _ in range(n)]

while 1:
  flag = 0
  visited = [[False for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if visited[i][j] == False:
        flag += bfs(land, i, j, visited)
        
  if flag == 0:
    break
  
  time += 1
  
print(time)
