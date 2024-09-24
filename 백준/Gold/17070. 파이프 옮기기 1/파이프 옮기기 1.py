import sys
input = sys.stdin.readline


def dfs(x, y, pipe):
    global ans
    
    if x == n -1 and y == n - 1:
        ans += 1
        return
    
    if pipe == garo:
        if y + 1 < n:
            if home[x][y + 1] == 0:
                dfs(x, y + 1, garo)
        
        if x + 1 < n and y + 1 < n:
            if home[x][y + 1] == 0 and home[x + 1][y] == 0 and home[x + 1][y + 1] == 0:
                dfs(x + 1, y + 1, daegak)
    
    if pipe == sero:
        if x + 1 < n:
            if home[x + 1][y] == 0:
                dfs(x + 1, y, sero)
        
        if x + 1 < n and y + 1 < n:
            if home[x][y + 1] == 0 and home[x + 1][y] == 0 and home[x + 1][y + 1] == 0:
                dfs(x + 1, y + 1, daegak)
                
    if pipe == daegak:
        if y + 1 < n:
            if home[x][y + 1] == 0:
                dfs(x, y + 1, garo)
                
        if x + 1 < n:
            if home[x + 1][y] == 0:
                dfs(x + 1, y, sero)

        if x + 1 < n and y + 1 < n:
            if home[x][y + 1] == 0 and home[x + 1][y] == 0 and home[x + 1][y + 1] == 0:
                dfs(x + 1, y + 1, daegak)

n = int(input())
home = [list(map(int, input().split())) for _ in range(n)]
ans = 0

garo = 0
sero = 1
daegak = 2

dfs(0, 1, garo)

print(ans)