n = int(input()) # 도시 수
m = int(input()) # 버스 수

INF = int(1e9)
dist = [[INF]*n for _ in range(n)]

# 같은 값일 때 0으로 업데이트
for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0

# 값 업데이트
for _ in range(m):
    start, end, c = map(int, input().split())
    dist[start-1][end-1] = min(dist[start-1][end-1], c)

for i in range(n):
    for j in range(n):
        for k in range(n):
            dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print(0, end= ' ')
        else:
            print(dist[i][j], end=' ')
    print()