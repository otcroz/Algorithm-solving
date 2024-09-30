import sys
from collections import deque
input = sys.stdin.readline

cnt = 0
arr = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

T = int(input())

def bfs(a, b):
    global cnt
    dq = deque([(a, b)])
    cnt += 1

    while dq:
        a, b = dq.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if (nx >= 0 and nx < m and ny >= 0 and ny < n):
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    dq.append([nx, ny])

for _ in range(T):
    n, m, k = map(int, input().split())
    arr = [[0] * n for _ in range(m)]

    for i in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                bfs(i, j)
    print(cnt)
    cnt = 0
    arr = []