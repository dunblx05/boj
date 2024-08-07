from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
cook = [list(map(int, input().split())) for _ in range(n)]
cook_list = []
answer = sys.maxsize

# 요리 재료 조합만들기
for i in range(1, n + 1):
  cook_list.append(list(combinations(cook, i)))


for cooks in cook_list:

  for ingredient in cooks:
    #신맛 , 쓴 맛
    c, s = 1, 0

    for x, y in ingredient:
      c *= x
      s += y
      
    answer = min(answer, abs(c - s))

print(answer)