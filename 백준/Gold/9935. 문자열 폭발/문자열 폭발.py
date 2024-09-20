import sys

input = sys.stdin.readline

words = input().rstrip()
bomb = input().rstrip()
stack = []

for i in range(len(words)):
    stack.append(words[i])

    if ''.join(stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print(*stack, sep='')
