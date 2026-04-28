import sys

a, b = map(int, sys.stdin.readline().split())

def gcd(x, y):
    while y:
        x, y = y, x % y
    
    return x

def lcm(x, y):
    res = (x * y) // gcd(x, y)
    return res

print(gcd(a,b), lcm(a, b), sep = "\n")