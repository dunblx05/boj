from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque([i for i in range(1, n + 1)])
yos = []

while queue:
  for i in range(k - 1):
    queue.append(queue.popleft())
  yos.append(queue.popleft())

print("<", end = '')
print(*yos, sep = ', ', end = '')
print(">")