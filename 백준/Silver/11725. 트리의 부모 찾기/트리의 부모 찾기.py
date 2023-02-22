import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for i in range(N-1):
  a, b = map(int, input().split())
  graph[a] += [b]
  graph[b] += [a]

def dfs(i):
  for node in graph[i]:
    if visited[node] == 0:
      visited[node] = i
      dfs(node)

dfs(1) # 1번 노드가 루트

for i in range(2, N+1):
  print(visited[i])