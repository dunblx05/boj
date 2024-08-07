import sys
input = sys.stdin.readline

# 소수 판별 함수
# 에라스토네스의 채 사용하면 num의 제곱근까지만 검사하면됨
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 백트래킹
def backtracking(num):
    # 만약 인자로 들어온 숫자가 n자리수이면
    if len(str(num)) == n:
        # 소수 판별 후 출력
        if is_prime(num):
            print(num)
        return
    
    # 0부터 9까지 돌면서 
    for i in range(10):
        # 자리수를 늘려준다
        k = num * 10 + i
        
        # 만약에 늘린 수가 소수라면
        if is_prime(k):
            
            # 백트래킹하며 탐색
            backtracking(k)
                
n = int(input())

# 첫번째 자리가 2 3 5 7인 경우만 탐색
prime_first = [2, 3, 5, 7]

for i in prime_first:
    backtracking(i)