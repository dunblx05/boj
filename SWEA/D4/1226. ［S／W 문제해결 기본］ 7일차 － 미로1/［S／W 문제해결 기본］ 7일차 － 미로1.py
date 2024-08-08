from collections import deque

def bfs(maze, x, y):
  queue = deque()
  queue.append(((x, y)))

  while queue:
    x, y = queue.popleft()
    visited[x][y] = True

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= 16 or ny >= 16:
        continue
      if maze[nx][ny] == 1:
        continue
      if maze[nx][ny] == 0 and visited[nx][ny] == False:
        visited[nx][ny] = True
        queue.append((nx, ny))
      
      if maze[nx][ny] == 3:
        return True

  return False    


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for tc in range (1, 11):
  t = int(input())
  board = [list(map(int, input())) for _ in range(16)]
  visited = [[False for _ in range(16)] for _ in range(16)]

  for i in range(16):
    for j in range(16):
      if board[i][j] == 2:
        start_x = i
        start_y = j

  if bfs(board, start_x, start_y):
    print(f"#{t} 1")
  else:
    print(f"#{t} 0")