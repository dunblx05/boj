for tc in range(1, 11):
  l = int(input())
  lst = list(map(str, input()))
  stack = []

  for i in range(l):
    if lst[i] == '(' or lst[i] == '{' or lst[i] == '[' or lst[i] == '<':
      stack.append(lst[i])
    
    if lst[i] == ')':
      if stack[-1] == '(':
        stack.pop()
      else:
        stack.append(lst[i])

    if lst[i] == '}':
      if stack[-1] == '{':
        stack.pop()
      else:
        stack.append(lst[i])

    if lst[i] == ']':
      if stack[-1] == '[':
        stack.pop()
      else:
        stack.append(lst[i])
    
    if lst[i] == '>':
      if stack[-1] == '<':
        stack.pop()
      else:
        stack.append(lst[i])

  if len(stack) == 0:
    print(f"#{tc} {1}")
  else:
    print(f"#{tc} {0}")