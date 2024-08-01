import sys

input = sys.stdin.readline


n = int(input())
num_list = [0 for _ in range(10)]
answer = 0

while n > 0:
  num_list[n % 10] += 1

  n = n // 10

for i in range(10):
  if i == 6 or i == 9:
    continue
  
  if answer < num_list[i]:
    answer = num_list[i]

six_nine = num_list[6] + num_list[9] + 1

print(max(answer, six_nine // 2))