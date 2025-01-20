X = int(input())

# dp에 저장하는 값 == 나누는 횟수
dp = [0] * 1000001

for i in range(2, X+1):
  dp[i] = dp[i-1] + 1 # 1을 빼기

  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i//2] + 1)
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[X]) # 최소 횟수 출력

res = [X]
now = X
temp = dp[X] - 1

for i in range(X, 0, -1):
  if dp[i] == temp and (i+1 == now or i*2 == now or i*3 == now):
    now = i
    temp -= 1
    res.append(i)

print(*res)