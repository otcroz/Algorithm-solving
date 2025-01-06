T = int(input())

for i in range(0, T):
  n = int(input())
  stock = list(map(int, input().split(" ")))
  profit = 0
  max_stock = 0

  # 거꾸로
  for i in range(len(stock) - 1, -1, -1):
    if max_stock < stock[i]:
      max_stock = stock[i]
    else:
      profit += max_stock - stock[i]
  print(profit)