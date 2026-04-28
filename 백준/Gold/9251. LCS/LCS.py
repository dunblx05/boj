import sys

str1 = input()
str2 = input()

len1 = len(str1)
len2 = len(str2)

lcs = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i-1] == str2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[-1][-1])