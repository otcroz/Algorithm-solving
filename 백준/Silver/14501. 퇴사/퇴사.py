N = int(input())
dp = [0] *(N+1) # 최대 상담 수익

for i in range(1, N+1):
    a, b = map(int, input().split())
    dp[i] = max(dp[i-1], dp[i])
    fin = i+a-1 # 상담이 끝나는 날
    if fin <= N:
        dp[fin] = max(dp[i-1] + b, dp[fin]) # 상담을 받은 경우 vs 상담을 받지 않은 경우
print(max(dp))