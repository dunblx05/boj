import sys

def change(number):
  if switches[number] == 0:
    switches[number] = 1

  else:
    switches[number] = 0

  return

input = sys.stdin.readline

n = int(input())
switches = [-1] + list(map(int, input().split()))
students = int(input())

for _ in range(students):
  sex, num = map(int, input().split())

  if sex == 1:
    for i in range(num, n+1, num):
      change(i)

  else:
    change(num)
    for j in range(n // 2):
      if num + j > n or num - j < 1 :
        break
      if switches[num + j] == switches[num - j]:
        change(num + j)
        change(num - j)
      else:
        break

for i in range(1, n + 1):
  print(switches[i], end = ' ')
  if i % 20 == 0:
    print()