N = int(input())

arr = list(map(int, input().split()))
dp = [0] * 1000

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if arr[j] < arr[i] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1
print(max(dp))