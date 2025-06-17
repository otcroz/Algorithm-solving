T = int(input())

for _ in range(T):
  N = int(input())
  dp = []
  for i in range(2):
    dp.append(list(map(int, input().split())))
  if N == 1:
    print(*max(dp))
  elif N > 1:
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]
    for i in range(2, N):
      dp[0][i] += max(dp[1][i-1], dp[1][i-2])
      dp[1][i] += max(dp[0][i-1], dp[0][i-2])
    
    print(max(dp[0][N-1], dp[1][N-1]))