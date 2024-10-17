import sys
from collections import deque

n = int(input())
e = int(input())
network = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for i in range(e):
    a, b = map(int, input().split())
    
    network[a].append(b)
    network[b].append(a)

def dfs(node):
    visited[node] = True
    
    for net in network[node]:
        if visited[net] == False:
            dfs(net)

dfs(1)

ans = 0

for v in visited:
    if v == True:
        ans += 1
        
print(ans - 1)