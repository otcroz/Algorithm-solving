n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []

def back():
  if len(res) == m:
    print(' '.join(map(str, res)))
    return
  
  for i in range(len(arr)):
    res.append(arr[i])
    back()
    res.pop()

back()