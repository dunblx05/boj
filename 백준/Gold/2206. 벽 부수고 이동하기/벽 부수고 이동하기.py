from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited_no_break[0][0] = 1

    while queue:
        x, y, break_wall = queue.popleft()

        if x == n - 1 and y == m - 1:
            if break_wall == 0:
                return visited_no_break[x][y]
            else:
                return visited_break[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 벽을 부수지 않고 방문하는 경우
            if break_wall == 0 and visited_no_break[nx][ny] == 0 and board[nx][ny] == 0:
                visited_no_break[nx][ny] = visited_no_break[x][y] + 1
                queue.append((nx, ny, 0))

            # 벽을 부수고 방문하는 경우
            if break_wall == 1 and visited_break[nx][ny] == 0 and board[nx][ny] == 0:
                visited_break[nx][ny] = visited_break[x][y] + 1
                queue.append((nx, ny, 1))

            # 벽을 부수는 경우 (한 번도 부수지 않았을 때만)
            if break_wall == 0 and board[nx][ny] == 1 and visited_break[nx][ny] == 0:
                visited_break[nx][ny] = visited_no_break[x][y] + 1
                queue.append((nx, ny, 1))

    return -1


n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
visited_no_break = [[0] * m for _ in range(n)]  # 벽을 부수지 않고 방문했을 때
visited_break = [[0] * m for _ in range(n)]     # 벽을 부수고 방문했을 때

print(bfs())
