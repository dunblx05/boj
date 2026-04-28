import sys

while 1:
    num = list(map(int, sys.stdin.readline().strip()))
    r_num = list(reversed(num))

    if num[0] == 0:
        break

    if r_num == num:
        print('yes')
    else:
        print('no')