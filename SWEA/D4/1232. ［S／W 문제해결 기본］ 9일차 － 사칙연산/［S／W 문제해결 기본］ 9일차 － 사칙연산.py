def postorder(root):
  if len(tree[root - 1]) == 2:
    return int(tree[root - 1][1])
  
  else:
    left = postorder(int(tree[root - 1][2]))
    right = postorder(int(tree[root - 1][3]))

    if tree[root - 1][1] == '+':
      return left + right
    
    elif tree[root - 1][1] == '-':
      return left - right
    
    elif tree[root - 1][1] == '*':
      return left * right
    
    elif tree[root - 1][1] == '/':
      return left / right

for tc in range(1, 11):
  n = int(input())
  tree = [input().split() for _ in range(n)]

  for i in range(n):
    tree[i][0] = int(tree[i][0])

  ans = postorder(1)

  print(f"#{tc} {int(ans)}")