def dfs(s_x, s_y):
  global count 
  count += 1
  
  for i in range(4):
    nx = s_x + dx[i]
    ny = s_y + dy[i]

    if nx < 0 or ny < 0 or nx >= n or ny >= n:
      continue
    if rec[nx][ny] - rec[s_x][s_y] == 1:
      dfs(nx, ny)

t = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for tc in range(1, t + 1):
  ans = [0, 10e9]

  n = int(input())
  rec = [list(map(int, input().split())) for _ in range(n)]

  for i in range(n):
    for j in range(n):
      count = 0
      dfs(i, j)
      room_num = rec[i][j]

      if count > ans[0]:
        ans[0] = count
        ans[1] = room_num
      elif count == ans[0]:
        if room_num < ans[1]:
          ans[1] = room_num

  print(f"#{tc} {ans[1]} {ans[0]}")