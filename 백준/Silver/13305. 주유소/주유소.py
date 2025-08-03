n = int(input())
load = list(map(int, input().split()))
cost = list(map(int, input().split()))

c = cost[0]
min_cost = 0
for i in range(n-1):
  if c > cost[i]:
    c = cost[i]
  min_cost += c*load[i]
print(min_cost)