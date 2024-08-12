import sys
input = sys.stdin.readline

def check(arr):
  # 모음 개수, 자음 개수
  count_v, count_e = 0, 0

  for i in arr:
    if i in vowel:
      count_v += 1
    else:
      count_e += 1

  if count_v >= 1 and count_e >= 2:
    return True
  else:
    return False
  
def backtracking(arr):
  # 종료조건
  # 길이가 l이고
  if len(arr) == l:
    # 조건에 맞으면 출력
    if check(arr):
      print(''.join(arr))
    
    return

  # 재귀
  for i in range(len(arr), c):
    if arr[-1] < words[i]:
      arr.append(words[i])
      backtracking(arr)
      arr.pop()

l, c = map(int, input().split())
words = list(input().split())
words.sort()

vowel = ['a', 'e', 'i', 'o', 'u']

for i in range(c):
  backtracking([words[i]])