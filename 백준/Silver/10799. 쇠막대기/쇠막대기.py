import sys
input = sys.stdin.readline

lst = list(input().rstrip())
stack = []
ans = 0

for i in range(len(lst)):
  
  if lst[i] == '(':
    stack.append(lst[i])
  else:
    # 레이저
    if lst[i - 1] == '(':
      stack.pop()
      ans += len(stack)
    # 일반 막대기
    else:
      stack.pop()
      ans += 1

print(ans)