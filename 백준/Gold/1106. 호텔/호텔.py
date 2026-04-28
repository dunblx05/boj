import sys

c, n = map(int, input().split())
ad = []

# i명의 고객을 구할 때 드는 최소비용
dp = [0]

for i in range(1, 2001):
    dp.append(sys.maxsize)

for i in range(n):
    ad.append(list(map(int, input().split())))

for price, customer in ad:
    for cur_customer in range(customer, 2001):
        dp[cur_customer] = min(dp[cur_customer], dp[cur_customer - customer] + price)

print(min(dp[c : 2001]))