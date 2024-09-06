import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
classroom = [[0 for _ in range(n)] for _ in range(n)]
info = []
ans = 0

for _ in range(n * n):
    info.append(list(map(int, input().split())))

for student in info:
    stNum = student[0]
    position = []
    for i in range(n):
        for j in range(n):
            # 자리가 비어있으면
            if classroom[i][j] == 0:
                # 선호도와 주변 빈곳
                favor = 0
                empty = 0
                # 해당 칸 주변 4개 확인
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    # 범위체크
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    # 주변 자리가 비어있으면 비어있는칸 + 1
                    if classroom[nx][ny] == 0:
                        empty += 1
                    # 누군가 앉아있으면 선호도 + 1
                    elif classroom[nx][ny] in student[1:]:
                        favor += 1
                # 앉을 수 있는 좌표 선호도와 비어있는 칸 수 저장
                position.append([favor, empty, i, j])

    position.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    classroom[position[0][2]][position[0][3]] = stNum

info.sort(key=lambda x: (x[0]))
like = []

for i in range(n):
    for j in range(n):
        count = 0
        stNum = classroom[i][j]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if classroom[nx][ny] in info[stNum - 1][1:]:
                count += 1

        like.append(count)

for i in like:
    if i == 0:
        ans += 0
    elif i == 1:
        ans += 1
    elif i == 2:
        ans += 10
    elif i == 3:
        ans += 100
    elif i == 4:
        ans += 1000

print(ans)
