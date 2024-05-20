import sys

n = int(sys.stdin.readline())
cow = [2] * 11
count = 0

for _ in range(n):
    num, pos = map(int, sys.stdin.readline().split())

    if cow[num] == 2:
        cow[num] = pos
    elif cow[num] != 2:
        if cow[num] != pos:
            count += 1
            cow[num] = pos

print(count)