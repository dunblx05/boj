from itertools import combinations
import sys
input = sys.stdin.readline

while 1:
  num_list = list(map(int, input().split()))
  k = num_list[0]
  s = []

  for i in range(1, len(num_list)):
    s.append(num_list[i])

  combs = list(combinations(s, 6))
  
  for comb in combs:
    print(*comb)

  print()
  
  if k == 0:
    break
