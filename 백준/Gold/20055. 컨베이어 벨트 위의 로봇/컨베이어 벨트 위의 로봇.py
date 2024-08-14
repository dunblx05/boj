from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = deque(map(int, input().split()))
robot = deque(0 for _ in range(n))

res = 0

while 1:
  # 현재 단계
  res += 1

  # 1. 벨트 회전
  a.rotate(1)
  robot.rotate(1)
  # 회전하고 내리는 자리에 로봇이 있으면 내린다.
  robot[-1] = 0

  # 2. 먼저 올라간 로봇부터 이동
  for i in range(n - 2, -1, -1):
    # 다음 자리가 비어있고 내구도가 0이 아니면 이동
    if robot[i] == 1 and robot[i + 1] == 0 and a[i + 1] > 0:
      robot[i] = 0
      robot[i + 1] = 1
      a[i + 1] -= 1
  # 이동했는데 내리는 자리에 있으면 내린다
  robot[-1] = 0
  
  # 3. 로봇을 올리는 자리에 올림
  if a[0] != 0:
    robot[0] = 1
    a[0] -= 1

  if a.count(0) >= k:
    break

print(res)