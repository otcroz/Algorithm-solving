import sys
from collections import deque
input = sys.stdin.readline
d = [(0,1),(0,-1),(1,0),(-1,0)]

R, C = map(int, input().split())
g = [list(input().rstrip()) for _ in range(R)]
v = [[0]* C for _ in range(R)]
q = deque([])

def in_range(y, x):
    if 0 <= y < R and 0<= x < C:
        return True

def move(q):
    while q:
        a, b, t = q.popleft()
        for dy, dx in d:
            ny, nx = dy + a, dx + b
            
            if in_range(ny, nx):
                # 이동
                if v[ny][nx] == 0 and g[ny][nx] == '.':
                    q.append((ny, nx, t))
                    v[ny][nx] = v[a][b] + 1
                
            else:
                if t == 'J':
                    return v[a][b]

for i in range(R):
    for j in range(C):
        if g[i][j] == 'J':
            v[i][j] = 1
            q.append((i, j ,'J'))
        if g[i][j] == 'F':
            v[i][j] = 1
            q.appendleft((i, j ,'F'))

res = move(q)
if res:
    print(res)
else:
    print('IMPOSSIBLE')