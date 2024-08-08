import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
reception = [0 for _ in range(n)]
stack = []

for i in range(n):
  # 스택이 있다면
  while stack:
    # 스택의 맨 위 높이가 현재 높이 이상이면
    if h[stack[-1]] >= h[i]:
      # 정답 배열에 인덱스 저장
      reception[i] = stack[-1] + 1
      # 더 탐색할 필요 없이 break
      break
    # 현재 높이 보다 작다면 비교 안해도 되므로
    else:
      # 스택에서 인덱스 삭제 후 계속 맨 위 확인
      stack.pop()
  # 스택에 인덱스를 넣어줌
  stack.append(i)

print(*reception)