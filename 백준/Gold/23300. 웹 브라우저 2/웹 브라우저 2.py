from collections import deque
import sys

input = sys.stdin.readline

n, q = map(int, input().split())

back = deque()
forward = deque()
cur = 0

for i in range(q):
    command = list(input().split())

    op = command[0]

    if len(command) == 2:
        page = int(command[1])

    if op == 'B':
        if len(back) == 0:
            continue
        else:
            forward.appendleft(cur)
            cur = back.pop()
  
    elif op == 'F':
        if len(forward) == 0:
            continue
        else:
            back.append(cur)
            cur = forward.popleft()

    elif op == 'A':
        forward = deque()
        if cur != 0:
            back.append(cur)
            cur = page
        else:
            cur = page
  
    elif op == 'C':
        if back:
            new = [back[0]]
            for j in range(1, len(back)):
                if new[len(new) - 1] == back[j]:
                    continue
                new.append(back[j])
        
            back = deque(new)

print(cur)

if len(back) == 0:
    print(-1)
else:
    for i in range(len(back) - 1, -1, -1):
        print(back[i], end = ' ')
    print()
  
if len(forward) == 0:
    print(-1)
else:
    print(*forward)