import sys
import copy
input = sys.stdin.readline

def dist(h_x, h_y, c_x, c_y):
  return abs(h_x - c_x) + abs(h_y - c_y)

# 뽑을 개수, 담을 배열, 인덱스
def combinations(count, i):
  global chick_comb
  if count == m:
    chick_comb.append(copy.deepcopy(chick_list))
    return
  
  for j in range(i, len(chicken)):
    chick_list[count] = chicken[j]
    combinations(count + 1, j + 1)

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

chick_list = [0 for _ in range(m)]
chick_comb = []
chicken = []
house = []

answer = sys.maxsize

for i in range(n):
  for j in range(n):
    if city[i][j] == 1:
      house.append((i, j))
    elif city[i][j] == 2:
      chicken.append((i, j))

combinations(0, 0)

for combs in chick_comb:
  res = 0

  for x1, y1 in house:
    chick_distance = sys.maxsize
    
    for x2, y2 in combs:
      chick_distance = min(chick_distance, dist(x1, y1, x2, y2))
    
    res += chick_distance
  answer = min(answer, res)


print(answer)