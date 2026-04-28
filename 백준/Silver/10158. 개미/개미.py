import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x = (p + t) // w
y = (q + t) // h

if x % 2 == 0:
  nx = (p + t) % w
else:
  nx = w - ((p + t) % w)

if y % 2 == 0:
  ny = (q + t) % h
else:
  ny = h - ((q + t) % h)

print(nx, ny)  