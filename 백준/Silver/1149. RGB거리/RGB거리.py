n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)] # i번째 집을 j색으로 칠했을 때 최소
d = [0] * (n+1) # 각 집을 칠했을 때 최솟값

d = [[0]*3 for _ in range(n)]
d[0] = cost[0] # 첫 번째 집은 주어진 비용 그대로

for i in range(1, n):
    d[i][0] = cost[i][0] + min(d[i-1][1], d[i-1][2])
    d[i][1] = cost[i][1] + min(d[i-1][0], d[i-1][2])
    d[i][2] = cost[i][2] + min(d[i-1][0], d[i-1][1])

print(min(d[n-1]))