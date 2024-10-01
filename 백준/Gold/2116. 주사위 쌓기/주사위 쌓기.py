import sys
input = sys.stdin.readline

def find_max(down, dice:list):
    idx = dice.index(down)
    
    if idx == 0:
        side_max = max(dice[1], dice[2], dice[3], dice[4])
        top = dice[5]
    elif idx == 1:
        side_max = max(dice[0], dice[2], dice[4], dice[5])
        top = dice[3]
    elif idx == 2:
        side_max = max(dice[0], dice[1], dice[3], dice[5])
        top = dice[4]
    elif idx == 3:
        side_max = max(dice[0], dice[2], dice[4], dice[5])
        top = dice[1]
    elif idx == 4:
        side_max = max(dice[0], dice[1], dice[3], dice[5])
        top = dice[2]
    elif idx == 5:
        side_max = max(dice[1], dice[2], dice[3], dice[4])
        top = dice[0]
    
    return top, side_max   

n = int(input())
dice_list = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(1, 7):
    bottom = i
    total = 0
    
    for j in range(n):
        bottom, side = find_max(bottom, dice_list[j])
        total += side
        
    if ans < total:
        ans = total

print(ans)