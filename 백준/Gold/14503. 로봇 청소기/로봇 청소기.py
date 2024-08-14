from collections import deque
import sys
input = sys.stdin.readline

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 북 -> 서, 서 -> 남, 남 -> 동, 동 -> 북
# 0 -> 3, 3 -> 2, 2 -> 1, 1 -> 0
# d = (d + 3) % 4
n, m = map(int, input().split())
r, c, d = map(int, input().split())
place = []
clean = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
  place.append(list(map(int, input().split())))

count = 0

while 1:

  can_move = False

  # 1. 현재 칸이 청소되지 않았으면 청소
  if place[r][c] == 0 and clean[r][c] == False:
    count += 1
    clean [r][c] = True
  
  # 2. 반시계 방향으로 탐색
  for i in range(4):
    d = (d + 3) % 4
    nx = r + dx[d]
    ny = c + dy[d]
    
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
      continue
    # 움직일 수 있으면 
    # 청소 안된 빈칸
    if clean[nx][ny] == False and place[nx][ny] == 0:
      r, c = nx, ny
      can_move = True
      break

  # 못움직는 경우
  if can_move == False:
    # 후진 못하면 중지
    if place[r - dx[d]][c - dy[d]] == 1:
      break
    # 후진 할 수 있으면 이동
    else:
      r, c = r - dx[d], c - dy[d]

print(count)