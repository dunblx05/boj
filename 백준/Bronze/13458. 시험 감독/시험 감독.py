from math import ceil
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
judge = [1 for _ in range(len(a))]

for i in range(len(a)):
  rest = a[i] - b

  if(rest > 0):
    if(rest % c == 0):
      judge[i] += rest // c
    else:
      judge[i] += (rest // c) + 1

print(sum(judge))