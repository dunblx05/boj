from collections import deque
import sys
input = sys.stdin.readline

# 왼쪽 검사
def check_left(wh_num, x):
  if wh_num < 0:
    return
  # 이미 왼쪽에 도착해있다고 생각
  if wheels[wh_num][2] != wheels[wh_num + 1][6]:
    check_left(wh_num - 1, -x)
    wheels[wh_num].rotate(x)
  
# 오른쪽 검사
def check_right(wh_num, x):
  if wh_num > 3:
    return
  # 이미 오른쪽에 도착해 있다고 생각
  if wheels[wh_num - 1][2] != wheels[wh_num][6]:
    check_right(wh_num + 1, -x)
    wheels[wh_num].rotate(x)
  

wheels = []

for i in range(4):
  wheels.append(deque(list(map(int, input().rstrip()))))
k = int(input())

for i in range(k):
  num, dir = map(int, input().split())
  # 인덱스
  num -= 1
  
  # 왼쪽, 오른쪽 검사 -> 조건에 맞으면 반대방향으로 회전
  check_left(num - 1, -dir)
  check_right(num + 1, -dir)
  
  # 본인 돌려주기
  wheels[num].rotate(dir)

score = 0
  
for i in range(4):
  if wheels[i][0] == 1:
    if i == 0:
      score += 1
    elif i == 1:
      score += 2
    elif i == 2:
      score += 4
    elif i == 3:
      score += 8

print(score)