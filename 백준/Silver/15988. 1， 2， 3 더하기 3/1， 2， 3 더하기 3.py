import sys
input = sys.stdin.readline
MOD = 1000000009
T = int(input())
nums = [int(input()) for _ in range(T)]
MAX = max(nums)
dp = [0] * (MAX+1)
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, MAX+1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD

print("\n".join(str(dp[n]) for n in nums))