import sys
input = sys.stdin.readline

n = int(input())
mine = [list(input().strip()) for _ in range(n)]
board = [list(input().strip()) for _ in range(n)]
new_board = [['.' for _ in range(n)] for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(n):
    for j in range(n):
        count = 0
        if mine[i][j] != '*' and board[i][j] == 'x':
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]

                if (nx < 0 or nx >= n) or (ny < 0 or ny >= n):
                    continue
                if mine[nx][ny] == '*':
                    count += 1
            new_board[i][j] = count

for i in range(n):
    for j in range(n):
        if mine[i][j] == '*' and board[i][j] == 'x':
            for k in range(n):
                for l in range(n):
                    if mine[k][l] == '*':
                        new_board[k][l] = '*'

for i in range(n):
    print(''.join(map(str, new_board[i])))