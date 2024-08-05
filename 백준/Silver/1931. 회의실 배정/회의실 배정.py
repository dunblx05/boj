import sys
input = sys.stdin.readline

n = int(input())
info = []

for _ in range(n):
  info.append(list(map(int, input().split())))

# 회의 시간 정보를 끝나는 시간 순으로 정렬(같으면 시작 시간 순으로)
info.sort(key = lambda x : (x[1], x[0]))

count = 1

# 첫번째 회의 끝나는 시간 값 저장
end_time = info[0][1]

for i in range(1, n):
  # 회의 시간 중 끝나는 시간 보다 뒤에 시작하는 회의가 있으면
  if info[i][0] >= end_time:

    # 새로운 끝나는 시간 저장
    end_time = info[i][1]

    # 횟수 +1
    count += 1
    
print(count)