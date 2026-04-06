import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
g = [list(map(int,input().rstrip())) for _ in range(n)]
v = [[[False]*(k+1) for _ in range(m)] for _ in range(n)]
d = [(-1,0),(1,0),(0,1),(0,-1)]

def in_range(y, x):
    return 0<=y<n and 0<=x<m

def bfs():
    global v
    q = deque([(0, 0, 0, 1)])
    v[0][0][0] = True

    while q:
        a, b, c, dist = q.popleft()

        if a == n-1 and b == m-1:
            return dist

        for dy, dx in d:
            ny, nx = dy + a, dx + b

            if not in_range(ny, nx):
                continue
            # 벽이 없는데 방문하지 않은 경우
            if g[ny][nx] == 0 and not v[ny][nx][c]:
                v[ny][nx][c] = True
                q.append((ny, nx, c, dist+1))

            # 벽이 있는데 뚫을 수 있을 때
            elif g[ny][nx] == 1 and c < k and not v[ny][nx][c+1]:
                v[ny][nx][c+1] = True
                q.append((ny, nx, c+1, dist+1))
    return -1

print(bfs())