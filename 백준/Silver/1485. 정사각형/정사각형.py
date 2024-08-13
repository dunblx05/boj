import sys
input = sys.stdin.readline

def dist(x1, y1, x2, y2):
  return abs(x2 - x1)**2 + abs(y2 - y1)**2

t = int(input())

for tc in range(t):

  rectangle = []

  for i in range(4):
    x, y = map(int, input().split())
    rectangle.append((x, y))

  distance = []
  rectangle.sort(key = lambda x : (x[0], x[1]))

  for i in range(4):
    for j in range(i + 1, 4):
      distance.append(dist(rectangle[i][0], rectangle[i][1], rectangle[j][0], rectangle[j][1]))
  
  distance.sort()

  if distance[0] == distance[1] == distance[2] == distance[3] and distance[4] == distance[5]:
    print(1)
  else:
    print(0)