def dfs2(s_x, s_y, h, pathl):
  global ans
  global usedK
  ans = max(ans, pathl)

  for i in range(4):
    nx = s_x + dx[i]
    ny = s_y + dy[i]

    if nx < 0 or ny < 0 or nx >= n or ny >= n:
      continue
    
    if visited[nx][ny] == True:
      continue

    visited[nx][ny] = True
    
    if mountain[nx][ny] < h:
      dfs2(nx, ny, mountain[nx][ny], pathl + 1)

    elif usedK == False and mountain[nx][ny] - k < h:
      usedK = True
      dfs2(nx, ny, h - 1, pathl + 1)
      usedK = False
    
    visited[nx][ny] = False

t = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

usedK = False

for tc in range(1, t + 1):
  ans = 0
  n, k = map(int, input().split())
  mountain = [list(map(int, input().split())) for _ in range(n)]
  visited = [[False for _ in range(n)] for _ in range(n)]

  max_height = max(map(max, mountain))

  for i in range(n):
    for j in range(n):
      if mountain[i][j] == max_height:
        visited[i][j] = True
        dfs2(i, j, max_height, 1)
        visited[i][j] = False
  
  print(f"#{tc} {ans}")