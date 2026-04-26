def solution(m, n, puddles):
    answer = 0
    MOD = 1000000007
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    # dp에 puddles 등록
    for x, y in puddles:
        dp[y][x] = -1
    
    # dp 계산
    dp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if (i==1 and j == 1) or dp[i][j] == -1:
                continue

            if dp[i-1][j] != -1:
                dp[i][j] += dp[i-1][j] % MOD
            
            if dp[i][j-1] != -1:
                dp[i][j] += dp[i][j-1] % MOD
            
            dp[i][j] %= MOD
    
    answer = dp[n][m]
    
    return answer