for t in range(1, 11):
    dump = int(input())
    height = list(map(int, input().split()))

    for i in range(dump):

        max_i = height.index(max(height))
        min_i = height.index(min(height))

        height[max_i] -= 1
        height[min_i] += 1

    print(f"#{t} {max(height) - min(height)}")