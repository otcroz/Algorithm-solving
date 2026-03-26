import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
max_res = 0
draw = 0

def in_range(y, x):
    if 0 <= y < n and 0<= x < m:
        return True

def bfs(i, j):
    global v, max_res
    q = deque([(i,j)])
    v[i][j] = 1
    cnt = 1

    while q:
        a, b = q.popleft()
        for dy, dx in d:
            ny, nx = a + dy, b + dx

            if not in_range(ny, nx):
                continue
            if v[ny][nx] == 1:
                continue
            if g[ny][nx] == 1:
                q.append((ny, nx))
                cnt += 1
                v[ny][nx] = 1
    
    max_res = max(max_res, cnt)

for i in range(n):
    for j in range(m):
        if g[i][j] == 1 and v[i][j] == 0:
            bfs(i, j)
            draw += 1

print(draw)
print(max_res)