import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append(1)

    visited[1] = True

    while queue:
        x = queue.popleft()

        if x == 100:
            return

        for dice in range(1, 7):
            nx = x + dice

            if nx > 100:
                continue

            if visited[nx]:
                continue

            if nx in ladder:
                nx = ladder[nx]

            if nx in snake:
                nx = snake[nx]

            if not visited[nx]:
                visited[nx] = True
                board[nx] = board[x] + 1
                queue.append(nx)


n, m = map(int, input().split())
ladder = {}
snake = {}
board = [0 for _ in range(101)]
visited = [False for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v

bfs()

print(board[100])
