import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if lab[i][j] == 9:
            queue.append((i, j))
            visited[i][j] = 1


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            while 0 <= nx < n and 0 <= ny < m:
                visited[nx][ny] = 1

                if lab[nx][ny] == 9:
                    break

                if lab[nx][ny] == 3:
                    if i == 0:
                        i = 1
                    elif i == 1:
                        i = 0
                    elif i == 2:
                        i = 3
                    elif i == 3:
                        i = 2

                elif lab[nx][ny] == 4:
                    if i == 0:
                        i = 3
                    elif i == 1:
                        i = 2
                    elif i == 2:
                        i = 1
                    elif i == 3:
                        i = 0

                elif lab[nx][ny] == 1 and (i == 1 or i == 3):
                    break

                elif lab[nx][ny] == 2 and (i == 0 or i == 2):
                    break

                nx += dx[i]
                ny += dy[i]


bfs()

ans = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] == True:
            ans += 1

print(ans)
