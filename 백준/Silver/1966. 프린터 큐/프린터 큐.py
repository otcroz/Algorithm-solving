from collections import deque

T = int(input())

for _ in range(T):
  N, num = map(int, input().split())
  q = deque(list(map(int, input().split())))

  cnt = 0
  while q:
    maxImpor = max(q)
    item = q.popleft()
    num -= 1

    if maxImpor == item:
      cnt += 1
      if num < 0:
        print(cnt)
        break
      
    else:
      q.append(item)
      if num < 0:
        num = len(q) - 1