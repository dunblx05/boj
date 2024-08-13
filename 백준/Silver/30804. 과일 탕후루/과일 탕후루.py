import sys
input = sys.stdin.readline

n = int(input())
tang = list(map(int, input().split()))

fruitDict = {}
start, end = 0, 0
ans = 0

#여기서 기록을 해줘야돼 즉, 딕셔너리
while 1:
  kind = 0
  
  if end == n:
    break

  #그 여기서 갯수를 기록...
  if tang[end] in fruitDict:
    fruitDict[tang[end]] += 1
  else:
    fruitDict[tang[end]] = 1
    
  #     fruitDict
  #     key들만 가져오는 
  
  # while 1:  
  while len(fruitDict) > 2:
    fruitDict[tang[start]] -= 1
    if fruitDict[tang[start]] == 0:
      del fruitDict[tang[start]]
    
    start += 1
  
  ans = max(ans, end - start + 1)
  
  end += 1

print(ans)