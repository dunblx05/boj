def check(row):
    for i in range(row):
        if col[row] == col[i] or row - i == abs(col[row] - col[i]):
            return False
    return True

def dfs(row):
    global res
    if row == n:
        res += 1
    else:
        for c in range(n):
            col[row] = c
            if check(row):
                dfs(row + 1)


T = int(input())

for t in range(1, T + 1):
    n = int(input())
    col = [0] * n
    res = 0

    dfs(0)

    print(f"#{t} {res}")