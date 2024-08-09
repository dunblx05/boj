from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start_x, start_y, visited):
  count = 1
  queue = deque()
  queue.append((start_x, start_y))
  visited[start_x][start_y] = True

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
        count += 1
        queue.append((nx, ny))
  
  return count

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
picture =[]
picture_area = []
visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
  picture.append(list(map(int, input().split())))


for i in range(n):
  for j in range(m):
    if picture[i][j] == 1 and visited[i][j] == False:
      area = bfs(picture, i, j, visited)
      picture_area.append(area)

if picture_area:
  print(len(picture_area))
  print(max(picture_area))
else:
  print(0)
  print(0)