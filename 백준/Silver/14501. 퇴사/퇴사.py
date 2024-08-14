import sys
input = sys.stdin.readline

n = int(input())
t = []
p = []
dp = [0 for _ in range(n + 1)]

for _ in range(n):
  time, profit = map(int, input().split())
  t.append(time)
  p.append(profit)

for i in range(n):
  for j in range(i + t[i], n + 1):
    if dp[j] < dp[i] + p[i]:
      dp[j] = dp[i] + p[i]

print(max(dp))