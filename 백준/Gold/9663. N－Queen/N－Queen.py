import sys
input = sys.stdin.readline

n = int(input())
ans = 0
col = [0] * n

def promising(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[x] - col[i]) == abs(x - i):
            return False

    return True

def queens(x):
    global ans

    if x == n:
        ans += 1
    else:
        for i in range(n):
            col[x] = i
            if promising(x):
                queens(x + 1)

queens(0)
print(ans)