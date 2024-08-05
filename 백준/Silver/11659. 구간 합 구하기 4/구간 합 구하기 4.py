import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
sum = 0

# 더한 값을 미리 저장할 배열
pre_sum = [0]

for i in num:
  sum += i
  pre_sum.append(sum)

for _ in range(m):
  l, r = map(int, input().split())
  # 구간 합 계산
  print(pre_sum[r] - pre_sum[l - 1])