import sys

n = int(sys.stdin.readline())
numlist = list(map(int, sys.stdin.readline().split()))
stack = []
res = [-1 for _ in range(n)]

stack.append(0)

for i in range(1, n):
    while len(stack) != 0 and numlist[stack[-1]] < numlist[i]:
        res[stack.pop()] = numlist[i]
    stack.append(i)

print(*res)