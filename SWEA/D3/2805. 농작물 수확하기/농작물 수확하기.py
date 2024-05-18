T = int(input())

for t in range(1, T+1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    profit = 0

    start = n // 2
    end = n // 2

    for i in range(n):
        for j in range(start, end + 1):
            profit += farm[i][j]
        if i < (n // 2):
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print(f"#{t} {profit}")