import sys
input = sys.stdin.readline

n = int(input())
count = 0

while 1:
  # 5로 나누어 떨어지면 자루 수에 몫만큼 더하기
  if n % 5 == 0:
    count = count + n // 5
    print(count)
    break

  # 5로 나누어 떨어질 때까지 3만큼 뺀 후 자루 수 1 더하기
  n -= 3
  count += 1

  # 3을 뺏을 때 0 보다 작아지면 -1 출력
  if n < 0:
    print(-1)
    break