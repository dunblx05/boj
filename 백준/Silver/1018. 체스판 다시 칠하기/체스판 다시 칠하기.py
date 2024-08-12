import sys
input = sys.stdin.readline

n, m = map(int, input().split())
count = 0

chess = [list(input().rstrip()) for _ in range(n)]
min_count = 64

for i in range(n - 7):
    for j in range(m - 7):
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 1:
                    if chess[a][b] == 'W':
                        count += 1
                elif (a + b) % 2 == 0:
                    if chess[a][b] == 'B':
                        count += 1

        if count > 32:
            count = 64 - count

        if min_count > count:
            min_count = count

        count = 0

print(min_count)
