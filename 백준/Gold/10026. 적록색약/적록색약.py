import sys
sys.setrecursionlimit(1000000)

N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(str, input())))
visited = [[0] * N for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [-0, 0, -1, 1]
    
two_cnt = 0
three_cnt = 0

def dfs(a, b):    
    visited[a][b] = 1
    current_color = arr[a][b]
    
    for i in range(4):
        ny = dy[i] + b
        nx = dx[i] + a

        if(0 <= nx < N) and (0 <= ny < N):
            if visited[nx][ny] == 0:
                if arr[nx][ny] == current_color:
                    dfs(nx, ny)
# 색약 x
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j)
            three_cnt += 1
            
                
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'
            
#visited = [[0]*N]*N
visited = [[0] * N for _ in range(N)]

# 색약
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j)
            two_cnt += 1
            
print(three_cnt, two_cnt)
