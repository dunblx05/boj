from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(s_x, s_y):
  queue = deque()
  queue.append((s_x, s_y))
  visited = [[0 for _ in range(m)] for _ in range(n)]
  visited[s_x][s_y] = 1
  
  time = 0
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if visited[nx][ny] == 0 and treasure[nx][ny] == 'L':
        queue.append((nx, ny))
        visited[nx][ny] = visited[x][y] + 1
  # print(visited)
  return max(map(max, visited)) - 1

n, m = map(int, input().split())
# 육지 L, 바다 W
treasure = [list(input().strip()) for _ in range(n)]

res = []
ans = sys.maxsize

for i in range(n):
  for j in range(m):
    if treasure[i][j] == 'L':
      res.append(bfs(i, j))

print(max(res))