for t in range(1, 11):
    t_num = int(input())
    n = 100
    arr = [list(map(int, input().split())) for _ in range(n)]
    col_sum = []
    row_sum = []
    diag_right_sum = 0
    diag_left_sum = 0
    for i in range(n):
        col_sum.append(sum(arr[i]))

    for i in range(n):
        temp_sum = 0
        for j in range(n):
            temp_sum += arr[j][i]
        row_sum.append(temp_sum)

    for i in range(n):
        for j in range(n):
            if i == j:
                diag_right_sum += arr[i][j]
            if i + j == n - 1:
                diag_left_sum += arr[i][j]
    max_col = max(col_sum)
    max_row = max(row_sum)
    total = max(max_col, max_row, diag_left_sum, diag_right_sum)

    print(f"#{t_num} {total}")