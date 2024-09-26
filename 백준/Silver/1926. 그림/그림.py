import sys
from collections import deque
input = sys.stdin.readline

nx = [1, -1, 0, 0]
ny = [0, 0, -1, 1]
cnt = 0
draw = []
arr = []

n, m = map(int,input().split())

def bfs(i, j):
  dq = deque([(i, j)]) # 큐 선언
  max = 1
  arr[i][j] = 0

  while dq:
    x, y = dq.popleft()
    for i in range(4):
      dx = x + nx[i]
      dy = y + ny[i]
      
      if dx >= 0 and dx < n and dy >=0 and dy < m:
        if arr[dx][dy] == 1:
          arr[dx][dy] = 0
          max += 1
          dq.append([dx, dy])
  draw.append(max)

for _ in range(n):
  arr.append(list(map(int, input().split())))

for i in range(n):
  for j in range(m):
    if arr[i][j] == 1:
      cnt += 1
      bfs(i,j)

print(cnt)
if len(draw) == 0:
  print(0)
else:
  print(max(draw))