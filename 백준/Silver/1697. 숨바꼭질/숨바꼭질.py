from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  queue = deque()
  queue.append(n)
  
  count[n] = 1
  
  while queue:
    x = queue.popleft()
    
    if x == k:
      return count[x] - 1
    else:
      for i in (x + 1, x - 1, x * 2):
        if (0 <= i < 100001) and count[i] == 0:
          count[i] = count[x] + 1
          queue.append(i)
        

n, k = map(int, input().split())
count = [0 for _ in range(100001)]

ans = bfs()

if n == k:
  print(0)
else:
  print(ans)