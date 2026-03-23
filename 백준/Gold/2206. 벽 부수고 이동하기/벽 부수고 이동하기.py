import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, (input().split()))

g = [list(map(int, input().rstrip())) for _ in range(n)]
v = [[[0, 0] for _ in range(m)] for _ in range(n)]
d = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def in_range(y, x):
    if 0 <= y < n and 0 <= x < m:
        return True

def bfs():
    global break_wall, v
    q = deque([(0, 0, 0)])
    v[0][0][0] = 1

    while q:
        a, b, wall = q.popleft()

        if a == n-1 and b == m-1:
            return v[a][b][wall]

        for dx, dy in d:
            ny, nx = dy + a, dx + b

            if not in_range(ny, nx):
                continue
            
            # 벽 X, 방문 X
            if g[ny][nx] == 0 and v[ny][nx][wall] == 0:
                q.append((ny, nx, wall))
                v[ny][nx][wall] = v[a][b][wall] + 1
            
            # 벽 있는 상태    
            if g[ny][nx] == 1 and wall == 0:
                q.append((ny, nx, 1))
                v[ny][nx][1] = v[a][b][wall] + 1
    return -1
            

print(bfs())