for t in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))
    total = 0
    for i in range(2, n-2):
        left_check1 = building[i] - building[i-1]
        left_check2 = building[i] - building[i-2]
        
        right_check1 = building[i] - building[i+1]
        right_check2 = building[i] - building[i+2]
    
        if left_check1 > 0 and  left_check2 > 0 and right_check1 > 0 and right_check2 > 0:
            total += min(left_check1, left_check2, right_check1, right_check2)

    print(f"#{t} {total}")