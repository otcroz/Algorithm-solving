from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque([]) # 큐 선언

m, n, h = map(int, input().split())

arr = []
day = 1

for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
    arr.append(temp)
    temp = []

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    global day
    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if arr[nz][ny][nx] == 0:
                    arr[nz][ny][nx] = arr[z][y][x] + 1
                    day = arr[nz][ny][nx]
                    queue.append([nz, ny, nx])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
               queue.append([i, j, k])
                
bfs()


for k in range(h):
    for i in range(n):
        if 0 in arr[k][i]:
            print(-1)
            exit(0)

print(day - 1)
