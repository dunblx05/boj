from itertools import combinations

def dfs(l, x, y, now, cost):
    global ans
    if now > c:
        return

    if l == m:
        ans = max(ans, cost)

    else:
        dfs(l + 1, x, y + 1, now + board[x][y], cost + board[x][y] ** 2)
        dfs(l + 1, x, y + 1, now, cost)


t = int(input())

for tc in range(1, t + 1):
    n, m, c = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    work1 = 0
    work2 = 0
    total = 0

    for i in range(n):
        for j in range(n - m + 1):
            ans = 0
            dfs(0, i, j, 0, 0)
            work1 = ans

            for k in range(i, n):
                start = 0
                if i == k:
                    start = j + m
                for p in range(start, n - m + 1):
                    ans = 0
                    dfs(0, k, p, 0, 0)
                    work2 = ans
                    total = max(total, work1 + work2)

    print(f"#{tc} {total}")
