# 거리 구하는 함수
def dist(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def dfs(x, y, path):
    global ans
    # 만약 현재 경로가 답보다 커지면 종료
    if path > ans:
        return

    # 모두 다 방문 했으면 거리에 집까지의 거리 추가후 정답보다 작으면 반환
    if 0 not in visited:
        path += dist(x, home[0], y, home[1])
        if path < ans:
            ans = path
        return

    for i in range(n):
        c_x = pos[i][0]
        c_y = pos[i][1]

        if visited[i] == 0:
            visited[i] = 1
            d = dist(c_x, x, c_y, y)
            dfs(c_x, c_y, path + d)
            visited[i] = 0


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    lst = list(map(int, input().split()))

    company = [lst[0], lst[1]]
    home = [lst[2], lst[3]]
    pos = []
    visited = [0 for _ in range(n)]
    ans = 10e9

    for i in range(4, len(lst) - 1, 2):
        pos.append((lst[i], lst[i + 1]))

    dfs(company[0], company[1], 0)

    print(f"#{tc} {ans}")
