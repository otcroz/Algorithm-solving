import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
T = int(input()) # 직사각형 범위 수

PS = [[0]*(m+1) for _ in range(n+1)] # (0,0)부터 (a,b)까지의 누적합

# 누적합 계산
for i in range(n):
    for j in range(m):
        PS[i+1][j+1] = graph[i][j] + PS[i+1][j] + PS[i][j+1] - PS[i][j]

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    pre_sum = PS[x2][y2] - (PS[x2][y1-1] + PS[x1-1][y2]) + PS[x1-1][y1-1]
    print(pre_sum)