from collections import deque
import sys

input = sys.stdin.readline


def bfs(v):
    queue = deque()
    queue.append(v)

    visited = [False for _ in range(n + 1)]
    visited[v] = True

    count = 1

    while queue:
        node = queue.popleft()
        for i in computer[node]:
            if visited[i] == False:
                count += 1
                queue.append(i)
                visited[i] = True

    return count


n, m = map(int, input().split())
computer = [[] for _ in range(n + 1)]
ans = []

for i in range(m):
    a, b = map(int, input().split())
    computer[b].append(a)

for i in range(1, n + 1):
    ans.append(bfs(i))

for i in range(len(ans)):
    if ans[i] == max(ans):
        print(i + 1, end=' ')
