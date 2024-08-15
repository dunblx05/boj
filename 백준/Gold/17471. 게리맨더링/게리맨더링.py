from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

def bfs(nodes):
  queue = deque()
  visited = [False for _ in range(n + 1)]
  queue.append(nodes[0])
  visited[nodes[0]] = True
  count = 1
  total = 0
  
  while queue:
    x = queue.popleft()
    total += population[x]
    
    for i in info[x]:
      if visited[i] == False and i in nodes:
        queue.append(i)
        visited[i] = True
        count += 1
  
  return total, count

n = int(input())
population = [0] + list(map(int, input().split()))
info = [[]]
city = [i for i in range(1, n + 1)]

ans = sys.maxsize

for i in range(n):
  tmp = list(map(int, input().split()))
  info.append(tmp[1:])

for i in range(1, n // 2 + 1):
  comb = list(combinations(city, i))
  
  for c in comb:
    total1, cnt1 = bfs(c)
    total2, cnt2 = bfs([i for i in range(1, n + 1) if i not in c])
    
    if cnt1 + cnt2 == n:
      ans = min(ans, abs(total1 - total2))
      
if ans == sys.maxsize:
  print(-1)
else:
  print(ans)