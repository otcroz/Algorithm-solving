n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []

def back(k):
  if len(res) == m:
    print(' '.join(map(str, res)))
    return
  
  for i in range(k, len(arr)):
      if arr[i] not in res:
        res.append(arr[i])
        back(i+1)
        res.pop()

back(0)