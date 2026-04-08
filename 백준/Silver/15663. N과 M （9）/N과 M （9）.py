n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []
res_comb = set()
v = [False]*n

def back(res_comb):
  if len(res) == m:
    res_tuple = tuple(res)
    if res_tuple not in res_comb:
      res_comb.add(res_tuple)
      return
  
  for i in range(len(arr)):
    if not v[i]:
      v[i] = True
      res.append(arr[i])
      back(res_comb)
      res.pop()
      v[i]= False

back(res_comb)
for res in sorted(res_comb):
  print(' '.join(map(str, res)))