import sys
from collections import deque
input = sys.stdin.readline
d = [(-1,0),(1,0),(0,1),(0,-1)]
n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
res = int(1e9)
inum = 2 # 대륙 넘버링에 사용

def in_range(y, x):
    if 0<=y<n and 0<=x<n:
        return True
    
# 대륙 넘버링
def land(i, j):
    q = deque([(i, j)])

    while q:
        a, b = q.popleft()
        g[a][b] = inum
        for dy, dx in d:
            ny, nx = dy + a, dx + b
            if in_range(ny, nx) and g[ny][nx] == 1:
                g[ny][nx] = inum
                q.append((ny, nx))

# 다리 짓기
def bfs(inum):
    v = [n*[-1] for _ in range(n)] # 방문 여부
    q = deque([])

    for i in range(n):
        for j in range(n):
            if g[i][j] == inum:
                v[i][j] = 0
                q.append((i, j))
    while q:
        a, b = q.popleft()
        for dy, dx in d:
            ny, nx = dy + a, dx + b
            if in_range(ny, nx):
                if g[ny][nx] == 0 and v[ny][nx] == -1: # 방문하지 않은 바다
                    v[ny][nx] = v[a][b] + 1
                    q.append((ny, nx))

                elif g[ny][nx] > 0 and g[ny][nx] != inum: # 다른 대륙에 도착
                    return v[a][b]
    
    return int(1e9)

for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            land(i, j)
            inum += 1

for num in range(2, inum):
    temp = bfs(num)
    res = min(res, temp)

print(res)