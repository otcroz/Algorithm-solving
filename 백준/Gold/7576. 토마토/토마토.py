from collections import deque
import sys
input = sys.stdin.readline

arr = []
day = 1
nx = [0, 0, -1, 1]
ny = [1, -1, 0, 0]
dq = deque([])

def bfs():
    global day
    
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]

            if dx >= 0 and dx < m and dy >=0 and dy < n:
                if arr[dx][dy] == 0:
                    arr[dx][dy] = arr[x][y] + 1
                    day = arr[dx][dy]
                    dq.append([dx, dy])

n, m = map(int, input().split())

for _ in range(m):
    arr.append(list(map(int, input().split())))

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            dq.append([i, j])

bfs()

# check
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            print(-1)
            exit(0)

print(day-1)