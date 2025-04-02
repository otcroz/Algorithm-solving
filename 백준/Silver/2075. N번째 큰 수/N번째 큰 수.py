import heapq

q = []

n = int(input())

for _ in range(n):
  temp = list(map(int, input().split(' ')))
  
  if not q:
    for num in temp:
      heapq.heappush(q, num)
  else:
    for num in temp:
      if q[0] < num:
        heapq.heappop(q)
        heapq.heappush(q, num)
print(q[0])