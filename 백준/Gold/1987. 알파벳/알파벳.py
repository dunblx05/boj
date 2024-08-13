import sys
input = sys.stdin.readline

def promising(arr, x):
  if x in arr:
    return False
  return True


def dfs(graph, s_x, s_y, count):
  global answer
  answer = max(answer, count)

  for i in range(4):
    nx = s_x + dx[i]
    ny = s_y + dy[i]

    if nx < 0 or ny < 0 or nx >= r or ny >= c:
      continue
    if promising(check, graph[nx][ny]):
      check.add(graph[nx][ny])
      dfs(graph, nx, ny, count + 1)
      check.remove(graph[nx][ny])


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r, c = map(int, input().split())

board = [list(input().rstrip()) for _ in range(r)]

check = set()
check.add(board[0][0])

answer = 0

dfs(board, 0, 0, 1)
print(answer)