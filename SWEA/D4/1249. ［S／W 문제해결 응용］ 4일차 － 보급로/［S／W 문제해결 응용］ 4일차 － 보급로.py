from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

t = int(input())


def bfs():
    queue = deque()
    queue.append((0, 0))
    cost[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if board[nx][ny] + cost[x][y] < cost[nx][ny]:
                cost[nx][ny] = board[nx][ny] + cost[x][y]
                queue.append((nx, ny))


for tc in range(1, t + 1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    cost = [[10e9 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    bfs()

    print(f"#{tc}", cost[n - 1][n - 1])
