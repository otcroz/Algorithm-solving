from collections import deque


n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
visited = [0] * (n + 1)


for i in range(m):
  a, b = map(int, input().split(" "))
  graph[a].append(b)
  graph[b].append(a)

def bfs(n):
  depth = 0
  answer = 0
  queue = deque()
  queue.append(n)
  visited[n] = 1

  while queue:
    depth += 1
    for _ in range(len(queue)):
      node = queue.popleft()
      for item in graph[node]:
        if visited[item] == 0:
          queue.append(item)
          visited[item] = 1
          answer += 1
    if depth == 2:
      break

  return answer

print(bfs(1))