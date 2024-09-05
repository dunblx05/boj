from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline


def bfs(c):
    queue = deque()
    queue.append(c[0])

    visited = [False for _ in range(n + 1)]
    visited[c[0]] = True

    total = 0
    count = 1

    while queue:
        node = queue.popleft()
        total += population[node]

        for i in cityInfo[node]:
            if visited[i] is False and i in c:
                queue.append(i)
                visited[i] = True
                count += 1

    return total, count


n = int(input())
population = [0] + list(map(int, input().split()))
cityInfo = [[]]
for i in range(1, n + 1):
    tempInput = list(map(int, input().split()))
    cityInfo.append(tempInput[1:])

cities = [i for i in range(1, n + 1)]
ans = sys.maxsize

for i in range(1, n // 2 + 1):
    for comb in list(combinations(cities, i)):
        pop1, cnt1 = bfs(comb)
        pop2, cnt2 = bfs([i for i in range(1, n + 1) if i not in comb])

        if cnt1 + cnt2 == n:
            res = abs(pop1 - pop2)
            if res < ans:
                ans = res

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
