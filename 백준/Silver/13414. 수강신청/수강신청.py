import sys
input = sys.stdin.readline

k, l = map(int, input().split())
studentInput = {}

for i in range(l):
  s = input().strip()

  studentInput[s] = i


res = sorted(studentInput.items(), key = lambda x : x[1])

if k > len(res):
  k = len(res)

for i in range(k):
  print(res[i][0])