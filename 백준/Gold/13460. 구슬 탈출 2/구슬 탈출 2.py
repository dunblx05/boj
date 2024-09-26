from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def roll(x, y, d):
    canGo = False
    
    while True:
        x += dx[d]
        y += dy[d]
        
        if board[x][y] == '#':
            x -= dx[d]
            y -= dy[d]
            break
        
        if board[x][y] == 'O':
            canGo = True
            break
    
    return x, y, canGo


def bfs(red, blue):
    global count
    
    queue = deque()
    queue.append([red, blue, 0])
    
    while queue:
        r, b, c = queue.popleft()
        
        if c > 10:
            continue
        
        for i in range(4):
            nxr, nyr, redGo = roll(r[0], r[1], i)
            nxb, nyb, blueGo = roll(b[0], b[1], i)
            
            if nxr == nxb and nyr == nyb:
                if r[0] * dx[i] + r[1] * dy[i] > b[0] * dx[i] + b[1] * dy[i]:
                    nxb -= dx[i]
                    nyb -= dy[i]
                else:
                    nxr -= dx[i]
                    nyr -= dy[i]
            
            if blueGo == True:
                continue
            
            if redGo == True:
                count = min(count, c + 1)
                return
        
            if (nxr, nyr, nxb, nyb) not in visited:
                visited.add((nxr, nyr, nxb, nyb))
                queue.append([[nxr, nyr], [nxb, nyb], c + 1])
            
    return


n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = set()
count = 10e9

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            redPos = [i, j]
        if board[i][j] == 'B':
            bluePos = [i, j]
            
bfs(redPos, bluePos)

if count <= 10:
    print(count)
else:
    print(-1)