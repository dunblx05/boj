import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def burn():
    for _ in range(len(fire)):
        x, y = fire.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if maze[nx][ny] != 'F' and maze[nx][ny] != '#':
                fire.append((nx, ny))
                maze[nx][ny] = 'F'


def move():
    escape = False

    for _ in range(len(jihoon)):
        x, y = jihoon.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                return visited[x][y]

            if maze[nx][ny] == '.' and visited[nx][ny] == 0:
                escape = True
                visited[nx][ny] = visited[x][y] + 1
                jihoon.append((nx, ny))

    if escape is False:
        return 'IMPOSSIBLE'


n, m = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]
ans = 0
fire = deque()
jihoon = deque()

for i in range(n):
    for j in range(m):
        if maze[i][j] == 'F':
            fire.append((i, j))

        if maze[i][j] == 'J':
            jihoon.append((i, j))
            visited[i][j] = 1

while 1:
    burn()
    ans = move()
    if ans:
        break

print(ans)
