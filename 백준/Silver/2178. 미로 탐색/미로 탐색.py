import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int ,input().split())
g = [list(map(int, input().rstrip())) for _ in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
v = [[0]*m for _ in range(n)]

def in_range(y, x):
    if 0 <= y < n and 0 <= x < m:
        return True

def bfs(i, j):
    global v
    q = deque([(i, j)])
    v[i][j] = 1
    
    while q:
        a, b = q.popleft()

        for dy, dx in d:
            ny, nx = a + dy, b + dx
            if not in_range(ny, nx):
                continue
            if g[ny][nx] == 1 and v[ny][nx] == 0:
                q.append((ny, nx))
                v[ny][nx] = v[a][b] + 1

bfs(0, 0)
print(v[n-1][m-1])