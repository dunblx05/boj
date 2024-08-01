import sys

input = sys.stdin.readline
alphabet = [0 for _ in range(26)]
word = input().rstrip()

for i in range(len(word)):
  index = ord(word[i]) - 97
  alphabet[index] += 1

print(*alphabet)