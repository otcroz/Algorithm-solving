import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

arr = []
res = []
cnt = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N = int(input())

visited = [[0] * N for _ in range(N)]

def dfs(a, b):
    cur_c = arr[a][b]

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if nx >= 0 and nx < N and ny >=0 and ny < N:
            if visited[nx][ny] == 0 and arr[nx][ny] == cur_c:
                visited[nx][ny] = 1
                dfs(nx, ny)
                    

arr = [list(map(str, input().rstrip('\n'))) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j)
            cnt += 1

res.append(cnt)

# 적록 색약의 경우
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

cnt = 0
visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j)
            cnt += 1

res.append(cnt)

print(res[0], res[1])