N = int(input())
dp = []
for _ in range(N):
    dp.append(list(map(int, input().split())))

for i in range(1, N): # 레벨 2부터 계산
    for j in range(i+1):
        if j == 0: # 맨 왼쪽 노드
            dp[i][j] += dp[i-1][j]
        elif j == i: # 맨 오른쪽 노드
            dp[i][j] += dp[i-1][j-1]
        else: # 2개의 노드 중 최대값 삽입입
            dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[N-1]))