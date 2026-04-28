import math

h, w, n, m = map(int, input().split())

width = math.ceil(w / (m + 1))
height = math.ceil(h / (n + 1))
answer = width * height
print(answer)