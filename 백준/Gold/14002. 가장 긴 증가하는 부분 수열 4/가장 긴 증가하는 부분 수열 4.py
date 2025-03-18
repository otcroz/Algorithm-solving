N = int(input())

arr = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
    temp = []
    dp[i] = 1
    for j in range(i):
        if arr[i] > arr[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1
            temp.append(arr[j])

x = max(dp)
print(x)
res = []
for i in range(N-1, -1, -1):
    if dp[i] == x:
        res.append(arr[i])
        x -= 1

res.reverse()
print(' '.join(map(str,res)))