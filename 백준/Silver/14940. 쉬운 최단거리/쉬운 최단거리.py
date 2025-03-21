from collections import deque

n, m = map(int, input().split())
arr = []
for _ in range(n):
  temp = list(map(int, input().split()))
  arr.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[-1] * m for _ in range(n)]

def bfs(start):

  q = deque([start])
  
  while q:
    y, x = q.popleft()
    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]
      if nx >= 0 and nx < m and ny >= 0 and ny < n:
        if visited[ny][nx] == -1 and arr[ny][nx] == 1:
          visited[ny][nx] = visited[y][x] + 1
          q.append((ny, nx))

for i in range(n):
  for j in range(m):
    if arr[i][j] == 2:
      start = (i, j)
      visited[i][j] = 0
    elif arr[i][j] == 0:
      visited[i][j] = 0

bfs(start)

for item in visited:
  print(' '.join(map(str, item)))