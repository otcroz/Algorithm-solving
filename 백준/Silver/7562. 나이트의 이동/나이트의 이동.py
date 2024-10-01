from collections import deque
import sys
sys.setrecursionlimit(100000)

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]
visited = []

T = int(input())

def bfs(a, b):
    global visited
    dq = deque([(a, b)])
    
    while dq:
        x, y = dq.popleft()
        if x == target[0] and y == target[1]:
            print(visited[x][y])
            return

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N) and (0 <= ny < N):
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    dq.append([nx, ny])

for _ in range(T):
    N = int(input())
    visited =[[0] * N for _ in range(N)]

    start = list(map(int, input().split()))
    target = list(map(int, input().split()))

    bfs(start[0], start[1])