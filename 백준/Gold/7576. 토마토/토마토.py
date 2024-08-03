from collections import deque

w, h = map(int, input().split(' '))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
day = 1
queue = deque([])

arr = []
for i in range(h):
    temp = list(map(int, input().split(' ')))
    arr.append(temp)

def bfs():
    global day
    while queue:
        bh, bw = queue.popleft()
        for i in range(4):
            nx = dx[i] + bw
            ny = dy[i] + bh

            if nx >= 0 and nx < w and ny >= 0 and ny < h:
                if arr[ny][nx] == 0:
                    arr[ny][nx] = arr[bh][bw] + 1
                    day = arr[ny][nx]
                    queue.append([ny, nx])
                    


for i in range(h):
    for j in range(w):
        if arr[i][j] == 1:
            queue.append([i, j])

bfs()

for i in range(h):
    for j in range(w):
        if arr[i][j] == 0:
            print(-1)
            exit(0)

print(day - 1)