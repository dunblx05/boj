# import copy

def connectWire(x, y, i, graph):
   connect = True
   nx = x
   ny = y
   
   while 1:
      nx += dx[i]
      ny += dy[i]
      
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
         break
      if graph[nx][ny] != 0:
         connect = False
         break

   if connect:
      count = 0
      nx = x
      ny = y
      
      while 1:
         nx += dx[i]
         ny += dy[i]
         
         if nx < 0 or ny < 0 or nx >= n or ny >= n:
            break
         
         graph[nx][ny] = 2
         count += 1
      return count
   
   else:
      return -1

def backTracking(index, cnt, minWire, graph):
   global ansCore
   global ansWire
   
   if index == len(core):
      if ansCore < cnt:
         ansCore = cnt
         ansWire = minWire
         
      elif ansCore == cnt:
         ansWire = min(minWire, ansWire)
         
      return
   
   tempGraph1 = [i[:] for i in graph]
   
   for i in range(4):
      tempGraph2 = [i[:] for i in graph]
      wire = connectWire(core[index][0], core[index][1], i, tempGraph2)
      
      if wire != -1:
         backTracking(index + 1, cnt + 1, minWire + wire, tempGraph2)
   
   backTracking(index + 1, cnt, minWire, tempGraph1)
   
   return
   
t = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for tc in range(1, t + 1):
   n = int(input())
   arr = [list(map(int, input().split())) for _ in range(n)]
   
   visited = [[False for _ in range(n)] for _ in range(n)]
   
   core = []
   ansCore = 0
   ansWire = 0
   
   for i in range(1, n - 1):
      for j in range(1, n - 1):
         if arr[i][j] == 1:
            core.append((i, j))
   
   backTracking(0, 0, 0, arr)
   
   print(f"#{tc} {ansWire}")