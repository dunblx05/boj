for tc in range(1, 11):
  rec = int(input())

  magnet = [list(map(int, input().split())) for _ in range(100)]
  
  
  count = 0

  for i in range(rec):
    # flag 설정
    lock = 0
    for j in range(rec):
      # 만약 빨간 자석이 있다면 flag 1 설정
      if magnet[j][i] == 1:
        lock = 1

      # 파란 자석이고 이전에 빨간 자석을 발견했다면 교착 상태 증가 및 flag 0설정
      elif magnet[j][i] == 2:
        if lock == 1:
          count += 1
          lock = 0

  print(f"#{tc} {count}")