import sys
input = sys.stdin.readline

def rotate(n, d, matrix):
    # 45면 1번 회전, 90이면 2번 회전...
    rotations = d // 45 % 8

    for r in range(rotations):
        # 주대각선, 부대각선, 가운데 행, 가운데 열
        main_diag = [matrix[i][i] for i in range(n)]
        sub_diag = [matrix[i][n-i-1] for i in range(n)]
        mid_row = matrix[n//2]
        mid_col = [matrix[i][n//2] for i in range(n)]

        for i in range(n):
            matrix[i][n//2] = main_diag[i]  # 주대각선 -> 가운데 열
            matrix[i][n-i-1] = mid_col[i]   # 가운데 열 -> 부대각선
            matrix[i][i] = mid_row[i]       #가운데 행 -> 주대각선
            matrix[n//2][i] = sub_diag[n-i-1]   # 부대각선 -> 가운데 행

    return matrix

t = int(input())

for tc in range(t):
    n, d = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    rotate_arr = rotate(n, d, arr)

    for i in rotate_arr:
        print(*i)