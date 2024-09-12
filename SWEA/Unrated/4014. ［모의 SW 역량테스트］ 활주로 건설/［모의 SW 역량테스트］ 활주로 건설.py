def check(line):
    count = 1
    for i in range(n - 1):
        # 높이가 같은 경우
        if line[i] == line[i + 1]:
            count += 1

        # 높이가 다른 경우
        elif line[i] != line[i + 1]:
            # 높이가 1 낮아지는 경우
            if line[i] - line[i + 1] == 1 and count >= 0:
                count = -x + 1
            # 높이가 1 높아지는 경우
            elif line[i + 1] - line[i] == 1 and count >= x:
                count = 1
            else:
                return 0

    if count >= 0:
        return 1

    return 0


t = int(input())

for tc in range(1, t + 1):
    n, x = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for i in range(n):
        ans += check(field[i])

    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(field[j][i])

        ans += check(temp)

    print(f"#{tc} {ans}")