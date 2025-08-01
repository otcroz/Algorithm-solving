import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
d = [[0]*(n+1) for _ in range(n+1)]

# 부분합
for i in range(n):
    for j in range(n):
        d[i+1][j+1] = graph[i][j] + d[i+1][j] + d[i][j+1] - d[i][j]

# 값 구하기
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    
    res = d[x2][y2] - d[x1-1][y2] - d[x2][y1-1] + d[x1-1][y1-1]
    print(res)