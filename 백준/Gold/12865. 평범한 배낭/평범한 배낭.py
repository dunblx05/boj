import sys

n, k = map(int,input().split())

# D.P 배열
profit = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

# 물건 배열
object = [[0 for _ in range(2)] for _ in range(n)]

for i in range(n):
    object[i] = list(map(int,(input().split())))


for i in range(1, n + 1):
    for j in range(1, k + 1):
            if object[i-1][0] <= j:
                profit[i][j] = max(profit[i-1][j], object[i-1][1] + profit[i-1][j-object[i-1][0]])
            else:
                profit[i][j] = profit[i-1][j]

print(profit[n][k])