def dfs(change):
    global ans

    if change == k:
        ans = max(ans, int("".join(map(str, price))))
        return

    for i in range(len(price)):
        for j in range(i + 1, len(price)):
            price[i], price[j] = price[j], price[i]
            cur_price = int("".join(map(str, price)))

            if (cur_price, change) not in check:
                check.append((cur_price, change))
                dfs(change + 1)

            price[j], price[i] = price[i], price[j]


t = int(input())

for tc in range(1, t + 1):
    ans = 0
    check = []

    n, k = map(int, input().split())
    price = list(map(int, str(n)))

    dfs(0)

    print(f"#{tc} {ans}")