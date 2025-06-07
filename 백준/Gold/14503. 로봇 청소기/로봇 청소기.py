import sys

input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

g = [list(map(int, input().split()))for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(i, j, d):
    cnt = 0 # 청소 카운트

    while True:
        if g[i][j] == 0:
            g[i][j] = -1
            cnt += 1

        cleaned = False

        for _ in range(4):
            d = (d - 1) % 4
            nx, ny = i + dx[d], j + dy[d]

            if in_range(nx, ny) and g[nx][ny] == 0:
                i, j = nx, ny
                cleaned = True
                break
            
        if not cleaned:
            i, j = i + dx[d] * (-1), j + dy[d] * (-1) # 후진
            if in_range(i, j) and g[i][j] == 1 or not in_range(i, j):
                print(cnt)
                return
bfs(x, y, d)