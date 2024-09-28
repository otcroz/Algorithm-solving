from collections import deque
import sys
input = sys.stdin.readline

arr = []
nx = [-1, 1, 0 ,0]
ny = [0, 0, -1, 1]
dq = deque([(0, 0)])

n, m = map(int, input().split())

for _ in range(n):
    arr.append(list(map(int, input().rstrip('\n'))))

while(dq):
    x, y = dq.popleft()

    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]

        if dx >= 0 and dx < n and dy >=0 and dy < m:
            if arr[dx][dy] == 1: 
                dq.append([dx, dy])
                arr[dx][dy] = arr[x][y] + 1

print(arr[n-1][m-1])