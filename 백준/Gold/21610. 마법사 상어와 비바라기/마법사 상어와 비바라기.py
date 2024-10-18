import sys

input = sys.stdin.readline

# 대각선은 1, 3, 5, 7
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

n, m = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(n)]
move = []

for i in range(m):
    d, s = map(int, input().split())
    d = d - 1
    move.append((d, s))

cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]

for d, s in move:

    no_cloud = []
    while cloud:
        x, y = cloud.pop()
        nx = (x + dx[d] * s) % n
        ny = (y + dy[d] * s) % n

        A[nx][ny] += 1

        no_cloud.append((nx, ny))

    for nx, ny in no_cloud:
        count = 0
        for i in range(1, 8, 2):
            nnx = nx + dx[i]
            nny = ny + dy[i]

            if nnx < 0 or nny < 0 or nnx >= n or nny >= n:
                continue

            if A[nnx][nny] > 0:
                count += 1

        A[nx][ny] += count

    for i in range(n):
        for j in range(n):
            if (i, j) not in no_cloud:
                if A[i][j] >= 2:
                    cloud.append([i, j])
                    A[i][j] -= 2

ans = 0

for i in A:
    ans += sum(i)

print(ans)
