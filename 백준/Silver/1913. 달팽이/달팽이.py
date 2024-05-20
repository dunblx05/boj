import sys
input = sys.stdin.readline

n = int(input())
t = int(input())

snail = [[0]*n for _ in range(n)]
x, y = n//2, n//2

# 상, 좌, 하, 우
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 배열에 넣을 숫자
num = 1
# 방향 전환 인덱스
dir = 0
# 해당 방향으로 얼마나 이동할지
move = 1

while num <= n ** 2:
    for _ in range(2):
        for _ in range(move):
            # 마지막은 우측방향으로 채울 필요가 없음
            if  num > n ** 2:
                break
            snail[y][x] = num
            if num == t:
                x_t, y_t = x, y
            num += 1
            x += dx[dir]
            y += dy[dir]
        dir = (dir+1) % 4
    move += 1

for _ in range(n):
    print(*snail[_])
print(y_t + 1, x_t + 1)