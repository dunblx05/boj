import sys
input = sys.stdin.readline

# 우, 상, 좌, 하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

n = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]
count = 0

for _ in range(n):
    sy, sx, d, g = map(int, input().split())
    curve = [(sx, sy), (sx + dx[d], sy + dy[d])]

    for _ in range(g):
        ex, ey = curve[-1]

        for i in range(len(curve) - 2, -1, -1):
            cx, cy = curve[i]
            curve.append((ex - (ey - cy), ey + (ex - cx)))

    for i, j in curve:
        board[i][j] = 1

for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i+1][j] == 1 and board[i][j+1] == 1 and board[i+1][j+1] == 1:
            count += 1

print(count)