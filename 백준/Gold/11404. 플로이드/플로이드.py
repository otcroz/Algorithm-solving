n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

# 같은 값일 때 0으로 초기화하기
for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j:
      graph[i][j] = 0

# 그래프에 값 업데이트
for _ in range(m):
  a, b, c = map(int, input().split(" "))
  graph[a][b] = min(c, graph[a][b])

# 최단 경로 구하기
for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 출력: 최단 경로 값
for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j] == INF:
      print(0, end = " ")
    else:
      print(graph[i][j], end=" ")
  print()