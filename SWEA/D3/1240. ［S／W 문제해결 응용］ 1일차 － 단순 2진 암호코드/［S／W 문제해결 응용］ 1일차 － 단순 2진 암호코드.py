binary = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4,
          '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}

t = int(input())

for tc in range(1, t + 1):
  n, m = map(int, input().split())
  password = [list(map(int, (input().strip()))) for _ in range(n)]
  newCode = []
  ans = []
  validity = 0

  for i in range(n):
    if 1 in password[i]:
      code = password[i]
      break

  for i in range(m - 1, -1, -1):
    if code[i] == 1:
      newCode = code[i - 55 :i + 1]
      break
  
  for i in range(0, 56, 7):
    strCode = "".join(map(str,newCode[i:i+7]))
    ans.append(binary[strCode])
  
  for i in range(len(ans)):
    if i % 2 == 0:
      validity += ans[i] * 3
    else:
      validity += ans[i]
  
  print(f"#{tc}", end = ' ')

  if validity % 10 == 0:
    print(sum(ans))
  else:
    print(0)
