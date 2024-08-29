import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
  arr.append(int(input()))

arr = sorted(arr)
print(round(sum(arr) / n))
print(arr[n//2])

count = Counter(arr).most_common(n)

if len(count) > 1:
  if count[0][1] == count[1][1]:
    print(count[1][0])
  elif count[0][1] > count [1][1]:
    print(count[0][0])
else:
  print(count[0][0])

print(abs(arr[0] - arr[-1]))