N = int(input())
a, b = map(int, input().split())
E = int(input())

edges = []
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = []

for _ in range(E):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(v, num):
    num += 1
    visited[v] = True
    if v == b:
        result.append(num)
        return

    for item in graph[v]:
        if not visited[item]:
            dfs(item, num)
        

dfs(a, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)