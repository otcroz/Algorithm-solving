def solution(alp, cop, problems):
    answer = 0
    INF = float('inf')
    
    max_alp, max_clp = 0, 0
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp = max(max_alp, alp_req)
        max_clp = max(max_clp, cop_req)
    
    # 이미 목표치를 넘은 경우
    alp = min(alp, max_alp)
    cop = min(cop, max_clp)
    
    dp = [[INF]*(max_clp+1) for _ in range(max_alp+1)]
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp+1):
        for j in range(cop, max_clp+1):
            # 알고력
            if i < max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            # 코딩력
            if j < max_clp:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req: # 문제 만족 시
                    # 인덱스 초과 방지
                    ni = min(max_alp, i + alp_rwd)
                    nj = min(max_clp, j + cop_rwd)

                    dp[ni][nj] = min(dp[ni][nj], dp[i][j]+cost)
    
    return dp[max_alp][max_clp]