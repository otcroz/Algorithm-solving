n, m = map(int, input().split())
res = []

def back(k):
  if len(res) == m:
    print(' '.join(map(str, res)))
    return
  
  for i in range(k, n+1):
      res.append(i)
      back(i)
      res.pop()

back(1)