import sys
from heapq import heappop, heappush

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dijkstra(sx, sy):
    heap = []
    heappush(heap, (0, sx, sy))
    visited[sx][sy] = True
    
    while heap:
        b_w, x, y = heappop(heap)
        
        if x == n - 1 and y == n - 1:
            return b_w
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            if visited[nx][ny] == True:
                continue
            
            if maze[nx][ny] == 1:
                heappush(heap, (b_w, nx, ny))
                visited[nx][ny] = True
            
            else:
                heappush(heap, (b_w + 1, nx, ny))
                visited[nx][ny] = True

n = int(input())
maze = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

ans = dijkstra(0, 0)

print(ans)