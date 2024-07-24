
from collections import deque

N, M, V = map(int, input().split())

visited = [0] * (N+1)
graph = [[0]*(N+1) for _ in range(N+1)]


for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n2][n1] = 1
    graph[n1][n2] = 1

def dfs(V):
    visited[V] = 1
    print(V, end=" ")
    for i in range(1, N+1):
        if visited[i] == 0 and graph[V][i]:
            dfs(i)

def bfs(V):
    q = deque([V])
    visited[V] = 1

    while q:
        V = q.popleft()
        print(V, end=" ")
        for i in range(1, N+1):
            if visited[i] == 0 and graph[V][i]:
                q.append(i)
                visited[i] = 1

    
dfs(V)

print()
visited = [0] * (N+1)

bfs(V)