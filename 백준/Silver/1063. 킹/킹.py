import sys
input = sys.stdin.readline

pos = {"A": 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H": 7}
move = {'R' : [0, 1], 'L' : [0, -1], 'B' : [1, 0], 'T' : [-1, 0], 
        'RT' : [-1, 1], 'LT' : [-1, -1], 'RB' : [1, 1], 'LB' : [1, -1]}

reverse_pos = {v:k for k, v in pos.items()}

king, stone, n = input().split()
n = int(n)

k = [8 - int(king[1]), pos[king[0]]]
s = [8 - int(stone[1]), pos[stone[0]]]

for i in range(n):
    command = input().strip()
    c = move[command]

    nx = k[0] + c[0]
    ny = k[1] + c[1]
    
    if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
        continue
    
    if nx == s[0] and ny == s[1]:
        nx_s = s[0] + c[0]
        ny_s = s[1] + c[1]
    
        if nx_s < 0 or ny_s < 0 or nx_s >= 8 or ny_s >= 8:
            continue
        
        else:
            k = [nx, ny]
            s = [nx_s, ny_s]
    
    else:
        k = [nx, ny]

print(f"{reverse_pos.get(k[1])}{8 - k[0]}")
print(f"{reverse_pos.get(s[1])}{8 - s[0]}")