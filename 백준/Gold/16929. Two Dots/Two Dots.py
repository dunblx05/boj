import sys

input = sys.stdin.readline


def dfs(x, y, start_x, start_y, color):

    if visited[x][y]:
        print("Yes")
        exit(0)

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (nx < 0 or ny < 0 or nx >= n or ny >= m) or board[nx][ny] != color:
            continue

        if (nx, ny) == (start_x, start_y):
            continue

        dfs(nx, ny, x, y, color)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

flag = False

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j, -1, -1, board[i][j])

print("No")
