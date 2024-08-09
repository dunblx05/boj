def inorder(root):
  # 왼쪽 자식은 루트 * 2, 오른쪽 자식은 루트 * 2 + 1
  # 노드 개수를 넘어가면 실행 X
  if root <= n:
    inorder(root * 2)
    answer.append(tree[root - 1][1])
    inorder(root * 2 + 1)


for tc in range(1, 11):
  answer = []
  n = int(input())
  tree = [input().split() for _ in range(n)]
  
  inorder(1)

  print(f"#{tc}", end = ' ')
  print(''.join(answer))