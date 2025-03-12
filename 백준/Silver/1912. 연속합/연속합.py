N = int(input())

arr = list(map(int, input().split()))
dp = [0] * 100000

dp[0] = arr[0]
result = arr[0]

for i in range(1, N):
    dp[i] = max(arr[i], arr[i] + dp[i-1])
    result = max(dp[i], result)
    
print(result)