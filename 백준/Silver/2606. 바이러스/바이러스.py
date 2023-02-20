from collections import deque

N = int(input())
v = int(input())
graph = [[] for i in range(N+1)]
visited = [0]*(N+1)
for i in range(v):
  a, b = map(int, input().split())
  graph[a] += [b]
  graph[b] += [a]

visited[1] = 1

def dfs(v):
  visited[v] = 1
  for node in graph[v]:
    if visited[node] == 0:
      dfs(node)
dfs(1)
print(sum(visited)-1)