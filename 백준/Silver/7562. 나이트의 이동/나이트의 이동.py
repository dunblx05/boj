from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start_x, start_y, visited):
  queue = deque()
  queue.append((start_x, start_y))
  visited[start_x][start_y] = True
  
  while queue:
    x, y = queue.popleft()
      
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or ny < 0 or nx >= l or ny >= l:
        continue
      
      if graph[nx][ny] == 0 and visited[nx][ny] == False:
        queue.append((nx, ny))
        visited[nx][ny] = True
        graph[nx][ny] = graph[x][y] + 1
        
  return graph[e_x][e_y]

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

t = int(input())

for _ in range(t):
  l = int(input())
  s_x, s_y = map(int, input().split())
  e_x, e_y = map(int, input().split())
  
  chess = [[0 for _ in range(l)] for _ in range(l)]
  visited = [[False for _ in range(l)] for _ in range(l)]
  
  ans = bfs(chess, s_x, s_y, visited)
  print(ans)