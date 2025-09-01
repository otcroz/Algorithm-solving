import sys
sys.setrecursionlimit(10**9)
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
dp = [[-1] * m for _ in range(n)] # 도착점까지 도달할 경우의 수 저장

def in_range(x, y):
    if 0<=x<n and 0<=y<m:
        return True

def dfs(i, j):
    # 도달한 경우
    if i == n-1 and j == m-1:
        return 1
    if dp[i][j] != -1: # 이미 계산한 경우 그대로 반환
        return dp[i][j]
    
    dp[i][j] = 0
    for x, y in d:
        nx, ny = x + i, y + j
        if in_range(nx, ny) and arr[i][j] > arr[nx][ny]:
            dp[i][j] += dfs(nx, ny)
    
    return dp[i][j]

print(dfs(0, 0))