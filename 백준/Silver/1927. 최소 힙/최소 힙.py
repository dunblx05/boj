import sys
import heapq
from collections import deque

heap = []
n = int(sys.stdin.readline())

for _ in range(n):
    command = int(sys.stdin.readline().rstrip())
    if command == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, command)