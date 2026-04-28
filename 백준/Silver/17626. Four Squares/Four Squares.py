# 1 4 9 16 25 36 49 64...

import sys

n = int(sys.stdin.readline())

dp = [0 for _ in range(n + 1)]
square = [0 for _ in range(318)]

for i in range(1, 318):
    square[i] = pow(i,2)

for i in range(1, n + 1):
    temp = []
    for j in range(1, n + 1):
        if square[j] > i:
            break
        temp.append(dp[i - square[j]])
    dp[i] = min(temp) + 1

print(dp[n])