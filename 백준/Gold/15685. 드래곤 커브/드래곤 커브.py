import sys
input = sys.stdin.readline

n = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]
result = 0

# 우 상 좌 하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(n):
    sy, sx, d, g = map(int, input().split())

    # 시작좌표 저장
    curve = [(sx, sy)]

    # 0세대 좌표 저장
    curve.append((sx + dx[d], sy + dy[d]))

    # 세대만큼 반복
    for _ in range(g):
        ex, ey = curve[-1]
        #curve의 끝 좌표 기준으로 90도 회전
        for i in range(len(curve) - 2, -1, -1):
            cx, cy = curve[i]
            curve.append((ex-(ey-cy), ey+(ex-cx)))

    # 좌표리스트에서 좌표 확인 후 board에 표시
    for i, j in curve:
        board[i][j] = 1

# 정사각형 검사
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            result += 1

print(result)