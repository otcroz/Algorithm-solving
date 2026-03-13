import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[int(1e9)] * (n+1) for _ in range(n+1)]
for i in range(n+1):
  g[i][i] = 0

for _ in range(m):
  a, b, t = map(int, input().split())
  g[a][b] = t

cnt = int(input())
friends = list(map(int, input().split()))

# 플로이드 워셜
for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      g[i][j] = min(g[i][j], g[i][k] + g[k][j])

# 각 지역 왕복시간들을 더한 최솟값
res = []
min_time = int(1e9)
for i in range(1, n+1):
  tmp = 0
  for f in friends:
    tmp = max(tmp, g[i][f] + g[f][i])

  if tmp < min_time:
    res = [i]
    min_time = tmp
  elif tmp == min_time:
    res.append(i)

print(*res)