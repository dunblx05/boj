from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append(s)
    count[s] = 1
    
    while queue:
        x = queue.popleft()
        # 도착했으면 출력
        if x == g:
            return count[x] - 1
        
        else:
            # 위로 아래로 이동하면서
            for i in (x + u, x - d):
                # 방문하지 않았으면
                if i > 0 and i <= f and count[i] == 0:
                    # 이동횟수 표시하고 탐색
                    count[i] = count[x] + 1
                    queue.append(i)

f, s, g, u, d = map(int, input().split())
count = [0 for _ in range(f + 1)]

ans = bfs()

if s == g:
    print(0)
elif ans:
    print(ans)
else:
    print("use the stairs")