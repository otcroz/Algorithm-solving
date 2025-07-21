# m, n, k = 행, 열, 직사각형 수
# 직사각형 꼭짓점 좌표(왼, 오 순서)
from collections import deque

m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cnt = 0 # 분리 영역 개수수
space_list = []

for i in range(k):
    lx, ly, rx, ry = map(int, input().split())

    # 그래프에 직사각형 채우기
    for j in range(lx, rx): # 열
        for k in range(ly, ry): # 행
            #print(m-k, n-j)
            graph[m-k-1][j] = 1 # 업데이트

#print(graph)

def in_range(x, y):
    if 0 <= x < m and 0 <= y <n:
        return True

def bfs(a, b):
    global graph, cnt, space_list
    q = deque([(a, b)])
    space = 1

    while q:
        a, b = q.popleft()
        
        for i in range(4):
            nx, ny = a + d[i][0], b + d[i][1]

            if not in_range(nx, ny) or graph[nx][ny] == 1:
                continue

            graph[nx][ny] = 1
            space += 1
            q.append((nx, ny))
    cnt += 1
    space_list.append(space)

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = 1
            bfs(i, j)

print(cnt)
space_list.sort()
print(" ".join(map(str, space_list)))