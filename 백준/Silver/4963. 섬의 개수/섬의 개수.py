import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]
cnt = 0

def dfs(a, b):
  if a < 0 or a >= h or b < 0 or b >= w:
    return  
  if graph[a][b] == 1:
    graph[a][b] = 0
    for i in range(8):
      nx = dx[i] + a
      ny = dy[i] + b
      dfs(nx, ny)


while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  graph = []
  for _ in range(h):
    graph.append(list(map(int, input().split())))

  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1:
        cnt += 1
        dfs(i, j)

  print(cnt)
  cnt = 0