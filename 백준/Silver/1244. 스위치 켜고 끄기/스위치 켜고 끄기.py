import sys

# 스위치 상태 변경 함수
def change(number):
  if switches[number] == 0:
    switches[number] = 1

  else:
    switches[number] = 0

  return

input = sys.stdin.readline

n = int(input())
switches = [-1] + list(map(int, input().split()))
students = int(input())

for _ in range(students):
  # 성별, 받은 숫자
  sex, num = map(int, input().split())

  # 남학생의 경우
  if sex == 1:
    # 배수만큼 배열 돌면서 변경
    for i in range(num, n+1, num):
      change(i)

  # 여학생의 경우
  else:
    # 자기 위치 변경
    change(num)
    # 끝까지 탐색할 필요없이 전체 길이 절반만큼만 반복
    for j in range(n // 2):
      # 범위를 벗어나면 break
      if num + j > n or num - j < 1 :
        break
      # 대칭 검사해서 스위치 변경
      if switches[num + j] == switches[num - j]:
        change(num + j)
        change(num - j)
      # 대칭 아니면 break
      else:
        break

for i in range(1, n + 1):
  print(switches[i], end = ' ')
  # 20개마다 출력하면 줄바꿈
  if i % 20 == 0:
    print()