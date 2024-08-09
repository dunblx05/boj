from collections import deque

def bfs(graph, node, visited):
  count = 1
  queue = deque([[node, count]])
  
  visited[node][0] = True

  while queue:
    x, count = queue.popleft()

    for i in graph[x]:
      # 방문처리
      if visited[i][0] == False:
        visited[i][0] = True
        # 방문순서 1 더해주기
        visited[i][1] = count + 1
        queue.append([i, count + 1])


for tc in range(1, 11):
  l, s = map(int, input().split())
  lst = list(map(int, input().split()))
  v = max(lst)
  graph  =[[] for _ in range(101)]
  
  # visited 배열에 방문여부와 방문순서를 같이 저장
  visited = [[False, 0] for _ in range(101)]

  for i in range(l):
    if i % 2 == 0:
      start = lst[i]
      end = lst[i + 1]
      if end not in graph[start]:
        graph[start].append(end)

  bfs(graph, s, visited)

  max_count = 0
  ans = 0

  # visited 순회하면서 제일 나중에 방문되는 노드 찾기
  for i in range(1, 101):
    if max_count <= visited[i][1]:
      max_count = visited[i][1]
      result = i
  
  print(f"#{tc} {result}")