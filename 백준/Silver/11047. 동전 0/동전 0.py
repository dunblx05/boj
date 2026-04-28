import sys

n, k = map(int, input().split())

coin = []
count = 0

for i in range(n):
    coin.append(int(input()))

for i in range(n - 1, -1, -1):
    if coin[i] <= k:
        while k >= 0 and k >= coin[i]:
            k -= coin[i]
            count += 1

print(count)