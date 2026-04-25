def solution(triangle):
    answer = 0
    LEN = len(triangle[-1])
    dp = [[0] * LEN for _ in range(LEN)]
    
    dp[0][0] = triangle[0][0]
    for i in range(1, LEN):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] +  triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    
    answer = max(dp[-1])
    
    return answer