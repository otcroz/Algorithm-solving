from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cnt = 0 # 빙산의 개수
year = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

g = [list(map(int, input().split(' '))) for _ in range(n)]

def bfs(i, j):
    q = deque([(i, j)])
    v[i][j] = 1

    while q:
        a, b = q.popleft()
        sea_count = 0

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0<= nx < n and 0<= ny < m:
                if g[nx][ny] == 0:
                    sea_count += 1
                elif g[nx][ny] > 0 and v[nx][ny] == 0:
                    v[nx][ny] = 1
                    q.append((nx, ny))

        melt_list.append((a, b, sea_count))

while True:
    v = [[0] * m for _ in range(n)]
    melt_list = []
    cnt = 0

    for i in range(n):
        for j in range(m):
            if g[i][j] > 0 and v[i][j] == 0:
                bfs(i, j)
                cnt += 1
    
    # 빙산 덩어리 검사
    if cnt == 0:
        print(0)
        break
    if cnt >= 2:
        print(year)
        break

    # 빙산이 녹음
    for x, y, melt in melt_list:
        g[x][y] = max(0, g[x][y] - melt)

    year += 1