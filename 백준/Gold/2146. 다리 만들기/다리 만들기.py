import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs_island(sx, sy, index):
    queue = deque()
    queue.append((sx, sy))

    visited[sx][sy] = True   
    pos = [(sx, sy)]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            if visited[nx][ny] == False and country[nx][ny] == 1:
                pos.append((nx, ny))
                queue.append((nx, ny))
                visited[nx][ny] = True
                
    for p in pos:
        country[p[0]][p[1]] = index


def bfs_bridge(index):
    queue = deque()
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if country[i][j] == index:
                dist[i][j] = 0
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            if country[nx][ny] != 0 and country[nx][ny] != index:
                return dist[x][y]

            elif country[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    
n = int(input())
country = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

num = 1
ans = 10e9

for i in range(n):
    for j in range(n):
        
        if country[i][j] == 1 and visited[i][j] == False:
            bfs_island(i, j, num)
            num += 1
            
for i in range(1, num):
    ans = min(ans, bfs_bridge(i))

print(ans)