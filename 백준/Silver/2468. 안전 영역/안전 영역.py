from collections import deque

n = int(input())

mx = 0
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

    for j in range(n):
        if mx < graph[i][j]:
            mx = graph[i][j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(j, k, value, visited):
    q = deque([(j, k)])
    visited[j][k] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

result = 0
for i in range(mx): # 깊이마다 계산
    visited = [[0]*n for _ in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                cnt += 1

    result = max(result, cnt)
    
print(result)