import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, K = map(int, input().split())

graph = [[] for _ in range(N+1)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

for i in range(N+1):
  for _ in range(M+1):
    graph[i].append(int('0'))
    
for i in range(K):
  a, b = map(int, input().split())
  graph[a][b] = 1

def dfs(a, b):
  global cnt
  if a < 0 or a > N or b < 0 or b > M:
    return 0
    
  if graph[a][b] == 1:
    graph[a][b] = 0
    cnt += 1
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      dfs(nx, ny)
          
    return cnt

max = 0
for i in range(1, N+1):
  for j in range(1, M+1):
    if graph[i][j] == 1:
      cnt = dfs(i, j)
      if max < cnt:
        max = cnt
      cnt = 0
      
print(max)