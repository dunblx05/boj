from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(graph, visited, start_x, start_y, height):
  queue = deque()
  queue.append((start_x, start_y))
  visited[start_x][start_y] = True
  
  count = 1
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
      if graph[nx][ny] <= height:
        continue
      if graph[nx][ny] > height and visited[nx][ny] == False:
        visited[nx][ny] = True
        queue.append((nx, ny))
        count += 1
        
  return count
        

n = int(input())
town = [list(map(int, input().split())) for _ in range(n)]

max_h = max(map(max, town))

ans = -sys.maxsize

for h in range(max_h):
  visited = [[False for _ in range(n)] for _ in range(n)]
  safe_arr = []
  
  for i in range(n):
    for j in range(n):
      if visited[i][j] == False and town[i][j] > h:
        safe = bfs(town, visited, i, j, h)
        safe_arr.append(safe)
        ans = max(ans, len(safe_arr))
        
print(ans)