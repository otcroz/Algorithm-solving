from collections import deque

N = int(input())
g = [list(map(int, input().split())) for _ in range(N)]

node = [[] for _ in range(N+1)]

for i in range(N):
  for j in range(N):
    if g[i][j] == 1:
      node[i+1].append(j+1)

def func(i, j):
  v = [0] * (N+1)
  q = deque([i])

  while q:
    root = q.popleft()
    v[root] = 1

    for n in node[root]:
      if j == n:
        return 1
      if v[n] == 0:
        q.append(n)
  return 0
  

for i in range(1, N+1):
  for j in range(1, N+1):
    print(func(i, j), end =' ')
  print()