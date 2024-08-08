from collections import deque

def topological_sort():
  result = []
  queue = deque([])

  # 만약 진입차수가 0이면 queue에 노드 추가
  for i in range(1, v + 1):
    if indegree[i] == 0:
      queue.append(i)

  while queue:
    # 큐에서 노드 제거
    x = queue.popleft()

    # 출력 배열에 저장
    result.append(x)

    # 연결된 노드의 간선 제거
    for i in graph[x]:
      indegree[i] -= 1

      # 진입 차수가 0이 되면 큐에 해당 노드 추가
      if indegree[i] == 0:
        queue.append(i)
  
  return result


for tc in range(1, 11):
  v, e = map(int, input().split())
  lst = list(map(int, input().split()))

  graph = [[] for _ in range (v + 1)]
  indegree = [0] * (v + 1)

  # 인접그래프 만들면서 노드별 진입차수 기록
  for i in range(e):
    start = lst[i * 2]
    end = lst[i * 2 + 1]
    graph[start].append(end)
    indegree[end] += 1

  # 위상 정렬 실행
  res = topological_sort()

  print(f"#{tc}", end = ' ')
  print(*res)