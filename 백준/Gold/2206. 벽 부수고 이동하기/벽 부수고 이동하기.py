from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1

    while queue:
        x, y, break_wall = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][break_wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 방문안했고 0인경우
            if visited[nx][ny][break_wall] == 0 and board[nx][ny] == 0:
                visited[nx][ny][break_wall] = visited[x][y][break_wall] + 1
                queue.append((nx, ny, break_wall))
            # 방문안했는데 벽을 만나고 한번도 안 부숨
            elif break_wall == 0 and board[nx][ny] == 1:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))

    return -1


n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

print(bfs())
