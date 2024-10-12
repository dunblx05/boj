import sys
input = sys.stdin.readline

def binary_search(h, start, end):
    global ans
    
    while start <= end:
        mid = (start + end) // 2
        cur = h[0]
        count = 1
        
        for i in range(1, len(h)):
            if h[i] >= cur + mid:
                count += 1
                cur = h[i]
            
        if count >= c:
            
            start = mid + 1
            ans = mid
        else:
            end = mid - 1


n, c = map(int, input().split())
house = [int(input().strip()) for _ in range(n)]
house.sort()

s = 1
e = house[-1] - house[0]
ans = 0

binary_search(house, s, e)

print(ans)