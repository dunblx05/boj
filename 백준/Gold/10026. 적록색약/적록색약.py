from collections import deque
import sys
import copy
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(graph, s_x, s_y, visited, color):
  queue = deque()
  queue.append((s_x, s_y))
  visited[s_x][s_y] = True
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
      
      if color == graph[nx][ny] and visited[nx][ny] == False:
        queue.append((nx, ny))
        visited[nx][ny] = True

n = int(input())
picture = [list(input().rstrip()) for _ in range(n)]
picture_blind = copy.deepcopy(picture)

visited = [[0 for _ in range(n)] for _ in range(n)]
visited_blind = [[0 for _ in range(n)] for _ in range(n)]

count = 0
count_blind = 0

for i in range(n):
  for j in range(n):
    if visited[i][j] == False:
      bfs(picture, i, j, visited, picture[i][j])
      count += 1

print(count, end = ' ')

for i in range(n):
  for j in range(n):
    if picture_blind[i][j] == 'R':
      picture_blind[i][j] = "G"
      
for i in range(n):
  for j in range(n):
    if visited_blind[i][j] == False:
      bfs(picture_blind, i, j, visited_blind, picture_blind[i][j])
      count_blind += 1

print(count_blind)