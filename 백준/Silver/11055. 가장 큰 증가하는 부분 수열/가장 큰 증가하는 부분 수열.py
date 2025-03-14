N = int(input())

arr = list(map(int, input().split()))
dp = [0] * 1000

for i in range(N):
    dp[i] = arr[i]
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + arr[i]:
            dp[i] = dp[j] + arr[i]
print(max(dp))