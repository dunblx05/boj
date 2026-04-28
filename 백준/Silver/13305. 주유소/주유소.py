import sys

n = int(sys.stdin.readline())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

cost = 0
min_oil = oil[0]

for i in range(n - 1):
    if oil[i] < min_oil:
        min_oil = oil[i]
    cost += min_oil * road[i]

print(cost)