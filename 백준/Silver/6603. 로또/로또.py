def combi(arr, s, index, cnt):
  if cnt == 6:
    print(*arr)
    return
  
  for i in range(index, len(s)):
    arr[cnt] = s[i]
    combi(arr, s, i+1, cnt+1)

while 1:
  num_list = list(map(int, input().split()))
  k = num_list[0]
  s = [0] * 6

  if k == 0:
    break 

  combi(s, num_list[1:], 0, 0)
  print()