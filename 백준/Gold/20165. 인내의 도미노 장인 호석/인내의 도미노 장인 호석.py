import sys
import copy

input = sys.stdin.readline

# N, E, S, W
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
origin_board = copy.deepcopy(board)
score = 0


def attack(x, y, d):
    global score
    
    if board[x][y] == -1:
        return
    
    domino = board[x][y]
    
    while domino > 0:
        
        if x < 0 or y < 0 or x >= n or y >= m:
            break
            
        if board[x][y] != -1:
            domino = max(domino, board[x][y])
            board[x][y] = -1
            score += 1
        
        x += dx[d]
        y += dy[d]
        
        domino -= 1
            
    


def defense(x, y):
    board[x][y] = origin_board[x][y]
    

for _ in range(r):
    ax, ay, d = input().split()
    ax, ay = int(ax) - 1, int(ay) - 1
    
    if d == 'N':
        attack(ax, ay, 0)
    elif d == 'E':
        attack(ax, ay, 1)
    elif d == 'S':
        attack(ax, ay, 2)
    elif d == 'W':
        attack(ax, ay, 3)
    
    dfx, dfy = map(int, input().split())
    dfx, dfy = dfx - 1, dfy - 1

    defense(dfx, dfy)
    
print(score)

for i in range(n):
    for j in range(m):
        if board[i][j] == -1:
            print("F", end = ' ')
        else:
            print("S", end = ' ')
    
    print()