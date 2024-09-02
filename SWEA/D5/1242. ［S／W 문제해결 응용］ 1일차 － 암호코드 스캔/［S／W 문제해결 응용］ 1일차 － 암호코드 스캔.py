rule = {(2, 1, 1) : 0, (2, 2, 1) : 1, (1, 2, 2) : 2, (4, 1, 1) : 3, (1, 3, 2) : 4, (2, 3, 1) : 5,
        (1, 1, 4) : 6, (3, 1, 2) : 7, (2, 1, 3) : 8, (1, 1, 2) : 9}

t = int(input())

for tc in range(1, t + 1):
  n, m = map(int, input().split())
  password = list(set([input().strip() for _ in range(n)]))
  password = sorted(password)[1:]
  dup = []
  ans = 0

  for p in password:
    code = format(int(p, 16), 'b').lstrip('0') + '0'

    n1, n2, n3 = 0, 0, 0
    count = 0
    validity = 0
    temp = ''

    for i in range(len(code)):
      if code[i] == '1' and n2 == 0:
        n1 += 1
      elif code[i] == '0' and n1 != 0 and n3 == 0:
        n2 += 1
      elif code[i] == '1' and n1 != 0 and n2 != 0:
        n3 += 1
      elif n3 != 0:
        count += 1
        
        ratio = min(n1, n2, n3)
        key = (n1//ratio, n2//ratio, n3//ratio)
        valid = rule[key]
        temp += str(valid)

        if count == 8:
          validity += valid

          if validity % 10 == 0 and temp not in dup:
            ans += sum(map(int, list(temp)))

          dup.append(temp)
          validity = 0
          count = 0
          temp = ''
        
        elif count % 2 == 0:
          validity += valid
        else:
          validity += valid * 3

        n1, n2, n3 = 0, 0, 0

  print(f"#{tc} {ans}")