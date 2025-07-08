import heapq

N, M = map(int, input().split())
score = list(map(int, input().split()))
hq = []
for i in range(N):
  heapq.heappush(hq, score[i])

for _ in range(M):
  first = heapq.heappop(hq)
  second = heapq.heappop(hq)
  sum_score = first + second

  for _ in range(2):
    heapq.heappush(hq, sum_score)

print(sum(hq))