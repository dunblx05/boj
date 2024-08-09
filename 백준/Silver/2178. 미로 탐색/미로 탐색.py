from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start_x, start_y):
  queue = deque()
  queue.append((start_x, start_y))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      
      if graph[nx][ny] == 0:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  
  return graph[n-1][m-1]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
maze = []

for i in range(n):
  maze.append(list(map(int, input().rstrip())))

ans = bfs(maze, 0, 0)

print(ans)