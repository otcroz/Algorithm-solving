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
Q = deque([1])

while Q:
  c = Q.popleft()
  for node in graph[c]:
    if visited[node] == 0:
      Q.append(node)
      visited[node] = 1

print(sum(visited) -1)