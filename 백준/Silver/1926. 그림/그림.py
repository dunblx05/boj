from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, visited, i, j):
  queue = deque()
  queue.append((i, j))
  visited[i][j] = True
  count = 1

  while queue:
    x, y = queue.popleft()

    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

      if graph[nx][ny] == 1 and visited[nx][ny] == False:
        count += 1
        visited[nx][ny] = True
        queue.append((nx, ny))

  return count
        

n, m = map(int, input().split())
pic = [list(map(int, input().split())) for _ in range(n)]
pic_area = []

visited = [[False] * m for _ in range(n)]
visited_1 = [[False] * m ] * n

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
  for j in range(m):
    if pic[i][j] == 1 and visited[i][j] == False:
      pic_area.append(bfs(pic, visited, i, j))

print(len(pic_area))
print(max(pic_area) if pic_area else 0)