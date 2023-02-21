#import sys
#sys.setrecursionlimit(5000)
#input = sys.stdin.readline


N = int(input())

graph = []
cnt = 0
res = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
  graph.append(list(map(int, input())))

def dfs(i, j):
  global cnt

  if i < 0 or i>= N or j < 0 or j >= N:
    return

  if graph[i][j] == 1:
    graph[i][j] = 0
    cnt+=1
  
    for k in range(4):
      nx = i + dx[k]
      ny = j + dy[k]
      dfs(nx, ny)
  
for i in range(N):
  for j in range(N):
      if graph[i][j] == 1:
        dfs(i, j)
        res.append(cnt)
        cnt = 0

res.sort()
print(len(res))
for i in res:
  print(i)