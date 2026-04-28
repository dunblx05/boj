import sys

cal = input().split('-')
sumlist = []

for i in cal:
    sum = 0
    numlist = i.split('+')
    for j in numlist:
        sum += int(j)
    sumlist.append(sum)

res = sumlist[0]

for i in range(1, len(sumlist)):
    res -= sumlist[i]

print(res)