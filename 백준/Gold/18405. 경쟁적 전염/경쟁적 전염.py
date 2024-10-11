from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    queue = deque(virus)
    time = 0
    while queue:
        if time == s:
            break
        for _ in range(len(queue)):
            cx, cy, cv = queue.popleft()
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue

                if arr[nx][ny] == 0:
                    arr[nx][ny] = cv
                    queue.append((nx, ny, cv))

        time += 1


n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

virus = []

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            virus.append((i, j, arr[i][j]))

virus.sort(key=lambda v: v[2])

bfs()

print(arr[x - 1][y - 1])
