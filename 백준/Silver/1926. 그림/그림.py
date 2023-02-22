from collections import deque

n, m = map(int, input().split())

graph = []
link = 0
cnt = 0
res = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
  global cnt
  Q = deque([(a,b)])
  graph[a][b] = 0
  cnt = 1
  
  while Q:
    x, y = Q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0<= ny < m:
        if graph[nx][ny] == 1:
          graph[nx][ny] = 0
          cnt += 1
          Q.append([nx, ny])

for _ in range(n):
  graph.append(list(map(int, input().split())))
  
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      link += 1
      bfs(i, j)
      res.append(cnt)

print(link)
if len(res) == 0:
  print(0)
else:
  print(max(res))