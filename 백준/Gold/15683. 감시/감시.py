import copy
import sys

input = sys.stdin.readline

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def fill(x, y, dir, board):
    for i in dir:
        nx = x
        ny = y

        while True:
            nx += dx[i]
            ny += dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = -1

    return


def dfs(depth, board):
    global ans
    # 종료조건 : 모든 cctv 확인했다면
    if depth == len(info):
        count = 0
        for i in range(n):
            count += board[i].count(0)
        if count < ans:
            ans = count
        return

    x, y, cctv_num = info[depth]
    new_board = copy.deepcopy(board)

    for i in cctv[cctv_num]:
        fill(x, y, i, new_board)
        dfs(depth + 1, new_board)
        new_board = copy.deepcopy(board)


n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
info = []
ans = sys.maxsize

# cctv 방향 정보
cctv = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [1, 2, 3], [0, 2, 3], [0, 1, 3]],
    [[0, 1, 2, 3]]
]

for i in range(n):
    for j in range(m):
        if 1 <= office[i][j] <= 5:
            info.append([i, j, office[i][j]])

dfs(0, office)

print(ans)
