from collections import deque

N = int(input())

graph = []
visited = []
res = []
cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
  graph.append(list(map(int, input())))
  visited.append([0]*N)

def bfs(i, j):
  global cnt
  Q = deque([(i,j)])
  visited[i][j] = 1
  cnt = 1
  
  while Q:
    x, y = Q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < N:
        if graph[nx][ny] == 1 and visited[nx][ny] == 0:
          Q.append([nx, ny])
          visited[nx][ny] = 1
          cnt += 1

for i in range(N):
  for j in range(N):
    if 0 <= i < N and 0 <= j < N:
        if visited[i][j] == 0 and graph[i][j] == 1:
          bfs(i, j)
          res.append(cnt)
          
res.sort()
print(len(res))
for i in res:
  print(i)