from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())
inning = [list(map(int, input().split())) for _ in range(n)]

order = [i for i in range(1, 9)]
ans = 0

for per in permutations(order, 8):
    per = list(per)
    # 타순 정하기
    batter = per[:3] + [0] + per[3:]
    score = 0
    # 타순
    hit_number = 0

    # 한 이닝마다
    for i in range(n):
        # 이닝마다 아웃카운트, 1 2 3루 초기화
        out = 0
        base1, base2, base3 = 0, 0, 0
        
        while out < 3:
            # 아웃
            if inning[i][batter[hit_number]] == 0:
                out += 1
            # 1루타
            elif inning[i][batter[hit_number]] == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            # 2루타
            elif inning[i][batter[hit_number]] == 2:
                score += base2 + base3
                base1, base2, base3 = 0, 1, base1
            # 3루타
            elif inning[i][batter[hit_number]] == 3:
                score += base1 + base2 + base3
                base1, base2, base3 = 0, 0, 1
            # 홈런
            elif inning[i][batter[hit_number]] == 4:
                score += base1 + base2 + base3 + 1
                base1, base2, base3 = 0, 0, 0
            # 다음 타순
            hit_number += 1
            # 다 쳤으면 처음부터
            if hit_number == 9:
                hit_number = 0

    if score > ans:
        ans = score

print(ans)
