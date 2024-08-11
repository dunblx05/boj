from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
  queue = deque([i])
  count[i] = 1
  
  while queue:
    x = queue.popleft()
    
    if x == j:
      return
    
    # 2*x, x-1, x+1  순서로 해야함, 그러지 않으면 틀림
    # 참조 : https://www.acmicpc.net/board/search/all/problem/13549/138387
    
    for nx in (x * 2, x - 1, x + 1):
      if nx < 0 or nx > 100000:
        continue
      
      if count[nx]:
        continue
      
      if nx == x * 2:
        count[nx] = count[x]
        
      else:
        count[nx] = count[x] + 1

      queue.append(nx)
          
n, k = map(int, input().split())
count = [0] * 100001

bfs(n, k)

print(count[k] - 1)