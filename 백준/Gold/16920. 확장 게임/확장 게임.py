import sys
from collections import deque
input = sys.stdin.readline

n, m, p = map(int, input().split())
s = list(map(int, input().split()))
g = [list(input().rstrip()) for _ in range(n)]
cnt = [0]*p
d = [(0,1),(0,-1),(1,0),(-1,0)]

def in_range(ny, nx):
    return 0<=ny<n and 0<=nx<m

# 플레이어를 각 큐에 관리
qs = [deque() for _ in range(p)]

# 플레이어 큐에 추가
for i in range(n):
    for j in range(m):
        if g[i][j] not in '.#':
            player = int(g[i][j]) - 1
            qs[player].append((i, j))
            cnt[player] += 1

while True:
    moved = False

    for i in range(p):
        q = qs[i]
        step = s[i]

        for _ in range(step):
            if not q: # 큐가 비어있을 때
                break

            for _ in range(len(q)):
                a, b = q.popleft()
                
                for dy, dx in d:
                    ny, nx = a + dy, b + dx

                    if not in_range(ny, nx):
                        continue
                    if g[ny][nx] != '.':
                        continue

                    g[ny][nx] = str(i+1)
                    cnt[i] += 1
                    q.append((ny, nx))
                    moved = True
    if not moved:
        break
            
# 개수 출력
print(*cnt)