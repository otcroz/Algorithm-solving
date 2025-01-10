n = int(input())
m = int(input())

graph = [[100000]*(n+1) for _ in range(n+1)]
path = [[()]*(n+1) for _ in range(n+1)]

# 같은 노드의 비용
for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j:
      graph[i][j] = 0

# 그래프에 값 입력(방향 그래프)
for _ in range(m):
  a, b, c = map(int, input().split(" "))
  graph[a][b] = min(c, graph[a][b])
  path[a][b] = (a, b)

# 최단값 확인하기
for node in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      cal_cost = graph[i][node] + graph[node][j]
      
      if graph[i][j] > cal_cost:
        graph[i][j] = cal_cost
        path[i][j] = path[i][node] + path[node][j][1:] # 경로 삽입

# 값 출력
for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j] == 100000:
      print(0, end=" ")
    else:
      print(graph[i][j], end=" ")
  print()

# 경로 출력
for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j] == 0 or graph[i][j] == 100000:
      print(0)
    else:
      print(len(path[i][j]), *path[i][j])