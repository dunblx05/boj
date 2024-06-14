import sys
import copy

input = sys.stdin.readline

def warm(r, c, island):
    new_island = copy.deepcopy(island)

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(r):
        for j in range(c):
            if island[i][j] == 'X':
                count = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if (nx < 0 or nx >= r) or (ny < 0 or ny >= c):
                        count += 1
                        continue
                    if island[nx][ny] == '.':
                        count += 1
                if count >= 3:
                    new_island[i][j] = '.'
    return new_island

def minimize(r, c, island):
    start_x, start_y, end_x, end_y = 999, 999, -1, -1

    for i in range(r):
        for j in range(c):
            if island[i][j] == 'X':
                start_x = min(start_x, i)
                start_y = min(start_y, j)
                end_x = max(end_x, i)
                end_y = max(end_y, j)
    
    return start_x, start_y, end_x, end_y


r, c = map(int, input().split())
island = [list(input().strip()) for _ in range(r)]

new_island = warm(r, c, island)
start_x, start_y, end_x, end_y = minimize(r, c, new_island)

for i in range(start_x, end_x + 1):
    print(''.join(new_island[i][start_y : end_y + 1]))