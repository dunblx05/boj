from collections import deque
import sys
import copy
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def makeWall(count):
  if count == 3:
    bfs()
    return
  
  for i in range(n):
    for j in range(m):
      if lab[i][j] == 0:
        lab[i][j] = 1
        makeWall(count + 1)
        lab[i][j] = 0

def bfs():
  global ans
  safe = 0
  queue = deque()
  visited = [[False for _ in range(m)] for _ in range(n)]

  tmp_arr = copy.deepcopy(lab)

  for i in range(n):
    for j in range(m):
      if tmp_arr[i][j] == 2:
        queue.append((i,j))
        visited[i][j] = True

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if visited[nx][ny] == False and tmp_arr[nx][ny] == 0:
        queue.append((nx, ny))
        visited[nx][ny] = True
        tmp_arr[nx][ny] = 2

  for i in range(n):
    safe += tmp_arr[i].count(0)
  
  ans = max(ans, safe)

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
ans = 0

makeWall(0)

print(ans)