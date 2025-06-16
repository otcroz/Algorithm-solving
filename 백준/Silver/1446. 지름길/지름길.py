N, D = map(int, input().split())

fast_load = []
for _ in range(N):
  start, end, distance = map(int, input().split())
  if end - start > distance:
    fast_load.append((start, end, distance))
fast_load.sort()

dp = [i for i in range(D+1)]

for start, end, distance in fast_load:
  for i in range(1, D+1):
    if end == i: # 지름길 이용한 경우
      dp[i] = min(dp[i], dp[start] + distance)
    else: # 지름길의 도착지점이 아닌 경우
      dp[i] = min(dp[i], dp[i-1] + 1)

print(dp[D])