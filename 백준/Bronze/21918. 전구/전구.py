import sys

n, m = map(int, sys.stdin.readline().split())
light = list(map(int, sys.stdin.readline().split()))
command = []

for i in range(m):
    com = list(map(int, sys.stdin.readline().split()))
    command.append(com)

for i in range(m):
    if command[i][0] == 1:
        light[command[i][1] - 1] = command[i][2]
    elif command[i][0] == 2:
        for j in range(command[i][1]-1, command[i][2]):
            if light[j] == 1:
                light[j] = 0
            else:
                light[j] = 1
    elif command[i][0] == 3:
        for j in range(command[i][1]-1, command[i][2]):
            light[j] = 0
    else:
        for j in range(command[i][1]-1, command[i][2]):
            light[j] = 1

print(*light)