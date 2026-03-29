import sys
from collections import deque
input = sys.stdin.readline
d = [(0, -1), (0, 1), (1, 0), (-1, 0)]
t = int(input())

def in_range(y, x):
    if 0 <= y < h and 0<= x < w:
        return True

def move():
    global v, q
    
    while q:
        a, b, c = q.popleft()

        for dy, dx in d:
            ny, nx = dy + a, dx + b

            if in_range(ny, nx):
                if v[ny][nx] == 0 and g[ny][nx] == '.':
                    q.append((ny, nx, c))
                    v[ny][nx] = v[a][b] + 1
            else:  
                if c == '@':
                    return v[a][b]

for _ in range(t):
    w, h = map(int, input().split())

    g = [list(input().rstrip()) for _ in range(h)]
    v = [[0]*w for _ in range(h)]
    q = deque([])

    for i in range(h):
        for j in range(w):
            if g[i][j] == '@':
                v[i][j] = 1
                q.append((i, j, '@'))
            if g[i][j] == '*':
                v[i][j] = 1
                q.appendleft((i, j, '*'))
    
    res = move()
    if res:
        print(res)
    else:
        print('IMPOSSIBLE')