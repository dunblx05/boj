import sys
from collections import deque

input = sys.stdin.readline


def dist(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def bfs():
    queue = deque()
    queue.append((home[0][0], home[0][1]))

    while queue:
        x, y = queue.popleft()

        if dist(x, fest[0][0], y, fest[0][1]) <= 1000:
            print("happy")
            return

        for i in range(n):
            if visited[i] == True:
                continue

            if dist(x, con[i][0], y, con[i][1]) <= 1000:
                queue.append((con[i][0], con[i][1]))
                visited[i] = True

    return print("sad")


t = int(input())

for tc in range(t):
    n = int(input())
    home = [list(map(int, input().split()))]
    con = []
    for _ in range(n):
        con.append(list(map(int, input().split())))
    fest = [list(map(int, input().split()))]

    visited = [False for _ in range(n)]
    bfs()
