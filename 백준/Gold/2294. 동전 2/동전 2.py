n, k = map(int, input().split())

coin = []
for _ in range(n):
  coin.append(int(input()))

d = [100001 for _ in range(k+1)]
d[0] = 0

for c in coin:
  for i in range(c, k+1):
    d[i] = min(d[i], d[i-c] + 1) # 동전 개수의 최솟값 업데이트
  
if d[k] == 100001:
  print(-1)
else:
  print(d[k])