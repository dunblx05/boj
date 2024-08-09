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

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= h or ny >= w:
        continue

      if graph[nx][ny] == 0:
        continue

      if graph[nx][ny] == 1 and visited[nx][ny] == False:
        count += 1
        visited[nx][ny] = True
        queue.append((nx, ny))

  return count
  
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

while 1:
  w, h = map(int, input().split())

  if w == 0 and h == 0:
    break

  map_lst = []
  visited = [[False for _ in range(w)] for _ in range(h)]
  islands = []

  for i in range(h):
    map_lst.append(list(map(int, input().split())))

  for i in range(h):
    for j in range(w):
      if map_lst[i][j] == 1 and visited[i][j] == False:
        island = bfs(map_lst, i, j, visited)
        islands.append(island)
  
  print(len(islands))