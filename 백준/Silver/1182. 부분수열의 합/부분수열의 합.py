import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int, input().split())
num = list(map(int, input().split()))

count = 0

for i in range(1, n + 1):
    comb = combinations(num, i)
    
    for c in comb:
        if sum(c) == s:
            count += 1
    
print(count)