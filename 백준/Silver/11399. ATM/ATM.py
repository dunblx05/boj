import sys

n = int(sys.stdin.readline())
time = list(map(int, input().split()))
time.sort()

acc_time = [0 for _ in range(n)]
acc_time [0] = time[0]

for i in range(1, n):
    acc_time[i] = acc_time[i-1] + time[i]

print(sum(acc_time))