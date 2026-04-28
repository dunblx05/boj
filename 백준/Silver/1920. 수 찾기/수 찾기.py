import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))

def bin_search(arr, i):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == i:
            return True
        elif arr[mid] < i:
            start = mid + 1
        elif arr[mid] > i:
            end = mid - 1
    
    return False

a.sort()

for i in range(m):
    if bin_search(a, find[i]) == True:
        print('1')
    else:
        print('0')