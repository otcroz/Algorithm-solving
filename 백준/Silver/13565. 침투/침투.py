import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = []

for i in range (N):
  graph.append(list(map(int, input())))

def dfs(a, b):
  if a < 0 or a >= N or b < 0 or b >= M:
    return
  if graph[a][b] == 0:
    graph[a][b] = 2
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      dfs(nx, ny)

for i in range(M):
  if graph[0][i] == 0:
    dfs(0, i)

def check(): # 격자값 체크
  for j in range(M):
    if graph[N-1][j] == 2:
      return True
  return False

if check(): print('YES')
else: print('NO')