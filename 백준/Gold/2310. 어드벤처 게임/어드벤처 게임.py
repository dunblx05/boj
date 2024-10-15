import sys
from collections import deque
input = sys.stdin.readline

def dfs(num, money):
    global flag
    
    if flag == 1:
        return
    
    if maze[num][0] == 'L':
        if maze[num][1] > money:
            money = maze[num][1]
    
    elif maze[num][0] == 'T':
        if maze[num][1] > money:
            return
        else:
            money -= maze[num][1]
            
    if num == n - 1:
        flag = 1
        return 
            
    visited[num] = True
    
    for i in maze[num][2]:
        if visited[i] == False:
            dfs(i, money)
            
    visited[num] = False
    

while 1:
    n = int(input())
    if n == 0:
        break
    
    maze = []
    visited = [False for _ in range(n)]
    flag = 0
    
    for _ in range(n):
        info, money, *door = input().split()
        door = list(map(lambda x: int(x) - 1, door[:-1]))
        maze.append([info, int(money), door])
    
    dfs(0, 0)
    
    if flag == 1:
        print("Yes")
    else:
        print("No")