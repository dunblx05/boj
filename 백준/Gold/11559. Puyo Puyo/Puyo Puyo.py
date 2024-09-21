from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(s_x, s_y):
    queue = deque()
    queue.append((s_x, s_y))
    visited[s_x][s_y] = True
    
    bbuyo = [(s_x, s_y)]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= 12 or ny >= 6:
                continue
            
            if field[nx][ny] == field[x][y] and visited[nx][ny] == False:
                queue.append((nx, ny))
                bbuyo.append((nx, ny))
                visited[nx][ny] = True
    
    return bbuyo

# 뿌요 아래로 내리기 
def down():
    for i in range(6):
        temp_queue = deque()
        
        # 아래에서부터 뿌요가 있으면 큐에 추가
        for j in range(11, -1, -1):
            if field[j][i] != '.':
                temp_queue.append(field[j][i])

        # 아래에서부터 큐에 있는 뿌요로 채움
        for j in range(11, -1, -1):
            if temp_queue:
                field[j][i] = temp_queue.popleft()
            else:
                field[j][i] = '.'
            
field = [list(input().rstrip()) for _ in range(12)]
ans = 0

while 1:
    visited = [[False for _ in range(6)] for _ in range(12)]
    count = 0
    
    # 뿌요 부수기
    for i in range(12):
        for j in range(6):
            if visited[i][j] == False and field[i][j] != '.':
                bbuyo_pos =[]
                bbuyo_pos = bfs(i, j)
                
                if len(bbuyo_pos) >= 4:
                    count += 1
                    for x, y in bbuyo_pos:
                        field[x][y] = '.'

    # 부술 뿌요 없으면 끝
    if count == 0:
        break
    
    # 아래로 내리기
    down()
    
    # 연쇄 횟수 추가
    ans += 1

print(ans)