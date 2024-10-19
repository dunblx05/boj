import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    queue = deque()
    queue.append([n, ''])
    visited[n] = True
    
    while queue:
        num, command = queue.popleft()
        
        if  num == b:
            return command
        
        d = (num * 2) % 10000
        
        if visited[d] == False:
            queue.append([d, command + 'D'])
            visited[d] = True
        
        if num == 0:
            s = 9999
        else:
            s = num - 1
            
        if visited[s] == False:
            queue.append([s, command + 'S'])
            visited[s] = True
            
        l = (num % 1000) * 10 + (num // 1000)
        
        if visited[l] == False:
            queue.append([l, command + 'L'])
            visited[l] = True
            
        r = (num % 10) * 1000 + (num // 10)
        
        if visited[r] == False:
            queue.append([r, command + 'R'])
            visited[r] = True
        

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    visited = [False for _ in range(10001)]
    
    ans = bfs(a)
    
    print(ans)
    