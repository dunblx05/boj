from collections import deque
from itertools import combinations
import copy
import sys

input = sys.stdin.readline

dx = [0, -1, 0]
dy = [-1, 0, 1]


def bfs(archer):
   tempBoard = copy.deepcopy(board)
   visited = [[0 for _ in range(m)] for _ in range(n)]
   count = 0

   for i in range(n - 1, -1, -1):
      kill = []
      
      for j in archer:
         queue = deque()
         queue.append((i, j, 1))

         while queue:
            x, y, reach = queue.popleft()

            if tempBoard[x][y] == 1:
               kill.append((x, y))

               if visited[x][y] == 0:
                  visited[x][y] = 1
                  count += 1
               break

            if reach < d:
               for k in range(3):
                  nx = x + dx[k]
                  ny = y + dy[k]

                  if 0 <= nx < n and 0 <= ny < m:
                     queue.append((nx, ny, reach + 1))

      for x, y in kill:
         tempBoard[x][y] = 0

   return count


n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

ans = 0
archer = list(combinations([i for i in range(m)], 3))

for a in archer:
   ans = max(ans, bfs(a))

print(ans)
