import copy
import sys
input = sys.stdin.readline

def fill(board, mode, x, y):
    for i in mode:
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

def dfs(depth, board):
    global ans
    
    if depth == len(cctv):
        count_area = 0
        for i in range(n):
            count_area += board[i].count(0)
        ans = min(ans, count_area)
        return

    new_office = copy.deepcopy(board)
    cctv_num, x, y = cctv[depth]

    for i in mode[cctv_num]:
        fill(new_office, i, x, y)
        dfs(depth + 1, new_office)
        new_office = copy.deepcopy(board)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = sys.maxsize
n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]

cctv = []

# cctv의 방향 정보
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

for i in range(n):
    for j in range(m):
        if office[i][j] in [1, 2, 3, 4, 5]:
            cctv.append([office[i][j], i, j])

dfs(0, office)
print(ans)