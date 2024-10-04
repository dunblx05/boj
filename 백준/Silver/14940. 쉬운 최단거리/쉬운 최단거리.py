import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(sx, sy):
    queue = deque()
    queue.append((sx, sy))

    visited[sx][sy] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if visited[nx][ny] == 0 and board[nx][ny] != 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            x2, y2 = i, j

bfs(x2, y2)

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and board[i][j] != 0:
            visited[i][j] = -1

visited[x2][y2] = 0

for i in visited:
    print(*i)
