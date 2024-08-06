import sys
input = sys.stdin.readline

def calc(a, s, m, d, i, calc_num):
  global min_res, max_res

  if i == n:
    max_res = max(calc_num, max_res)
    min_res = min(calc_num, min_res)
  
  else:
    if a:
      calc(a-1, s, m, d, i + 1, calc_num + num_list[i])
    if s:
      calc(a, s-1, m, d, i + 1, calc_num - num_list[i])
    if m:
      calc(a, s, m-1, d, i + 1, calc_num * num_list[i])
    if d:
      calc(a, s, m, d-1, i + 1, int(calc_num / num_list[i]))


min_res = 10E9
max_res = -10E9

n = int(input())
num_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

calc(add, sub, mul, div, 1, num_list[0])

print(max_res)
print(min_res)