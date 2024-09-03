import sys

input = sys.stdin.readline

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def spread():
    temp_house = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if house[i][j] > 0:
                temp = 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx < 0 or ny < 0 or nx >= r or ny >= c:
                        continue
                    if house[nx][ny] == -1:
                        continue
                    temp_house[nx][ny] += house[i][j] // 5
                    temp += house[i][j] // 5

                house[i][j] -= temp

    for i in range(r):
        for j in range(c):
            house[i][j] += temp_house[i][j]


def air_up():
    # 우 -> 상 -> 좌 -> 하
    x, y = cleaner[0][0], 1
    dir = 1
    temp = 0

    while 1:
        nx = x + dx[dir]
        ny = y + dy[dir]

        if nx >= r or ny >= c or nx < 0 or ny < 0:
            dir = (dir - 1) % 4
            continue
        if x == cleaner[0][0] and y == 0:
            break
        house[x][y], temp = temp, house[x][y]
        x, y = nx, ny


def air_down():
    # 우 -> 하 -> 좌 -> 상
    x, y = cleaner[1][0], 1
    dir = 1
    temp = 0

    while 1:
        nx = x + dx[dir]
        ny = y + dy[dir]

        if nx >= r or ny >= c or nx < 0 or ny < 0:
            dir = (dir + 1) % 4
            continue
        if x == cleaner[1][0] and y == 0:
            break
        house[x][y], temp = temp, house[x][y]
        x, y = nx, ny


r, c, t = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(r)]
cleaner = []
ans = 0

for i in range(r):
    for j in range(c):
        if house[i][j] == -1:
            cleaner.append((i, j))

for _ in range(t):
    spread()
    air_up()
    air_down()

for i in range(r):
    ans += sum(house[i])

print(ans + 2)
