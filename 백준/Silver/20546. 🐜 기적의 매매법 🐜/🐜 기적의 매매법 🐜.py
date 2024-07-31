import sys

input = sys.stdin.readline

money = int(input())
stock = list(map(int, input().split()))

money_bnp = money
count_bnp = 0

money_timing = money
count_timing = 0

# bnp 계산
for num, price in enumerate(stock):
  
  count_bnp += (money_bnp // price)
  money_bnp %= price

# timing 계산
for i in range(3, len(stock)):

  # 매수
  if stock[i-3] > stock[i-2] > stock[i-1] > stock[i]:
    count_timing += (money_timing // stock[i])
    money_timing %= stock[i]

  # 매도
  if stock[i-3] < stock[i-2] < stock[i-1] < stock[i] and count_timing >= 1:
    money_timing += stock[i] * count_timing
    count_timing = 0

bnp = money_bnp + stock[-1] * count_bnp
timing = money_timing + stock[-1] * count_timing

if (bnp > timing):
  print("BNP")

elif (bnp < timing):
  print("TIMING")
  
else:
  print("SAMESAME")