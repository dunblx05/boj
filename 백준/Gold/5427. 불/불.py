import sys
from collections import deque

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def burn():
    for _ in range(len(fire)):
        x, y = fire.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue

            if building[nx][ny] != '*' and building[nx][ny] != '#':
                fire.append((nx, ny))
                building[nx][ny] = '*'


def move():
    escape = False
    
    for _ in range(len(sang_guen)):
        x, y = sang_guen.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                return visited[x][y]
            
            if building[nx][ny] == '.' and visited[nx][ny] == 0:
                escape = True
                visited[nx][ny] = visited[x][y] + 1
                sang_guen.append((nx, ny))
    
    if escape is False:
        return 'IMPOSSIBLE'


t = int(input())

for tc in range(1, t + 1):
    w, h = map(int, input().split())
    building = [list(input().strip()) for _ in range(h)]

    fire = deque()
    sang_guen = deque()

    visited = [[0 for _ in range(w)] for _ in range(h)]
    ans = 0

    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                fire.append((i, j))

            if building[i][j] == '@':
                sang_guen.append((i, j))
                visited[i][j] = 1
                
    while 1:
        burn()
        ans = move()
        if ans:
            break
    
    print(ans)
