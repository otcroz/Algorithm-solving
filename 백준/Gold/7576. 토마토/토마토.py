import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
d = [(1,0),(-1,0),(0,1),(0,-1)]

def in_range(y, x):
    if 0 <= y < n and 0 <= x < m:
        return True

def bfs(tomato):
    global g
    q = deque(tomato)

    while q:
        a, b = q.popleft()
        for dy, dx in d:
            ny, nx = a + dy, b + dx

            if not in_range(ny, nx):
                continue
            if g[ny][nx] == 0:
                g[ny][nx] = g[a][b] + 1
                q.append((ny, nx))

tomato = []

for i in range(n):
    for j in range(m):
        if g[i][j] == 1:
            tomato.append((i, j))

bfs(tomato)

max_day = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            print(-1); exit(0)
        else:
            max_day = max(max_day, g[i][j])

print(max_day-1)