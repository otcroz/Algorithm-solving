from collections import deque
import sys
input = sys.stdin.readline

cnt = 0
N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
visited = [0]*(N+1)

for i in range(M):
  a,b = map(int, input().split())
  graph[a] += [b]
  graph[b] += [a]

def bfs(start):
  Q = deque([start])
  visited[start] = 1
  while Q:
    c = Q.popleft()
    for node in graph[c]:
      if visited[node] == 0:
        visited[node] = 1
        Q.append(node)
    

for i in range(1, N+1):
  if visited[i] == 0:
    if not graph:
      cnt += 1
      visited[i] = 1
    else:
      bfs(i) # 해당 노드 방문
      cnt += 1

print(cnt)