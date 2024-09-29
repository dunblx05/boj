import sys
input = sys.stdin.readline

n, m  = map(int, input().split())
inf = 10e9
friend = [[inf for _ in range(n)] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    
    friend[a - 1][b - 1] = 1
    friend[b - 1][a - 1] = 1
    

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                friend[i][j] = 0
            else:
                friend[i][j] = min(friend[i][j], friend[i][k] + friend[k][j])

bacon = []

for f in friend:
    bacon.append(sum(f))

print(bacon.index(min(bacon)) + 1)