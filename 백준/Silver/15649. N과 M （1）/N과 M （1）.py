import sys
import copy
input = sys.stdin.readline

pers = []

def backtracking(n, m):
  if len(per) == m:
    pers.append(copy.deepcopy(per))

  for i in range(1, n + 1):
    if i not in per:
      per.append(i)
      backtracking(n, m)
      per.pop()

n, m = map(int, input().split())
per = []

backtracking(n, m)

for i in range(len(pers)):
  print(*pers[i])