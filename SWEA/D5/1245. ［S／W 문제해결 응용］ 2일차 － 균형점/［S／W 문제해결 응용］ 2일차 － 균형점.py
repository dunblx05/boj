def binary_search(idx, left, right):
    global ans
    limit = 1e-12

    while right - left > limit:
        mid = (left + right) / 2
        point = 0

        for i in range(idx + 1):
            point += weight[i] / (pos[i] - mid) ** 2

        for i in range(n - 1, idx, -1):
            point -= weight[i] / (pos[i] - mid) ** 2

        if point > 0:
            left = mid
        elif point < 0:
            right = mid
        else:
            break

    ans.append(mid)


t = int(input())


for tc in range(1, t + 1):
    n = int(input())
    magnetic = list(map(int, input().split()))
    ans = []

    pos = magnetic[:n]
    weight = magnetic[n:]

    for i in range(n - 1):
        binary_search(i, pos[i], pos[i+1])

    print(f"#{tc}", end = ' ')
    for a in ans:
        print("%0.10f"%a, end = ' ')
    print()