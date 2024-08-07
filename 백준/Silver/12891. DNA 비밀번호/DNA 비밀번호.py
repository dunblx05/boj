import sys
input = sys.stdin.readline

s, p = map(int, input().split())
dna = input().rstrip()
a, c, g, t = map(int, input().split())
check = {"A":0, "C":0, "G":0, "T":0}

ans = 0

# 시작 상태 체크
sl = dna[:p]

for i in sl:
  check[i] += 1

if check["A"] >= a and check["C"] >= c and check["G"] >= g and check["T"] >= t:
  ans += 1

start = 0
end = start + p

# 슬라이싱 시작
for i in range(len(dna) - p):
  # 왼쪽 끝 인덱스 삭제하면서 없어지는 문자 체크
  check[dna[start + i]] -= 1

  # 오른쪽 끝 인덱스 늘려주면서 생기는 문자 체크
  check[dna[end + i]] += 1

  # 딕셔너리 확인 후 조건 맞으면 수 증가
  if check["A"] >= a and check["C"] >= c and check["G"] >= g and check["T"] >= t:
    ans += 1

print(ans)