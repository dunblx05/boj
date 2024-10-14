import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def spring():
    for i in range(n):
        for j in range(n):
            temp_tree = deque()
            
            while tree[i][j]:
                t = tree[i][j].popleft()
                
                if field[i][j] >= t:
                    field[i][j] -= t
                    temp_tree.append(t + 1)
                
                else:
                    dead_tree[i][j].append(t)
            
            tree[i][j] = temp_tree
            
def summer():
    for i in range(n):
        for j in range(n):
            while dead_tree[i][j]:
                field[i][j] += dead_tree[i][j].pop() // 2
                
def fall():
    for i in range(n):
        for j in range(n):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] % 5 == 0:
                    for l in range(8):
                        nx = i + dx[l]
                        ny = j + dy[l]
                        
                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            continue
                        
                        tree[nx][ny].appendleft(1)
                        
def winter():
    for i in range(n):
        for j in range(n):
            field[i][j] += a[i][j]

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
tree = [[deque() for _ in range(n)] for _ in range(n)]
dead_tree = [[list() for _ in range(n)] for _ in range(n)]

ans = 0

for _ in range(m):
    # (x, y, z) -> 나무의 위치 (x, y) + 나무의 나이 z
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)

field = [[5 for _ in range(n)] for _ in range(n)]            

for i in range(k):
    spring()
    summer()
    fall()
    winter()
    
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j])
        
print(ans)