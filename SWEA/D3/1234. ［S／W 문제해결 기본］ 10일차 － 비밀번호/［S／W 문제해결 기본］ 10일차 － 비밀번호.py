for tc in range(1, 11):
  n, p = map(str, input().split())

  n = int(n)
  pwd = list(map(int, p))
  stack = []

  for i in range(n):
    if len(stack) == 0:
      stack.append(pwd[i])
    else:
      if pwd[i] == stack[-1]:
        stack.pop()
      else:
        stack.append(pwd[i])
  
  print(f"#{tc}", end = ' ')
  print(*stack, sep = '')