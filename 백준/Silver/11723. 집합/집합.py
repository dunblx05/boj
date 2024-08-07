import sys
input = sys.stdin.readline

s = []
m = int(input())

for _ in range(m):
  command = list(input().split())
  
  op = command[0]
  if len(command) > 1:
    num = int(command[1])

  if op == 'add':
    if num not in s:
      s.append(num)

  elif op == 'remove':
    if num in s:
      s.remove(num)

  elif op == 'check':
    if num in s:
      print('1')
    else:
      print('0')  
  
  elif op == 'toggle':
    if num in s:
      s.remove(num)
    else:
      s.append(num)
    
  elif op == 'all':
    s = [i for i in range(1, 21)]
  
  elif op == 'empty':
    s = []