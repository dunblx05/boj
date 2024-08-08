from collections import deque

for tc in range(1, 11):
  t = int(input())
  pwd = list(map(int, input().split()))

  queue = deque(pwd)
  cycle = 1

  while 1:
    check = queue.popleft() - cycle

    if check <= 0:
      queue.append(0)
      break
    else:
      queue.append(check)

    cycle += 1

    if cycle > 5:
      cycle = 1


  print(f"#{t}", end = ' ')
  print(*queue)