s = list(input())
mobis = ['M', 'O', 'B', 'I', 'S']
g  = [0] * 5 

if len(s) < len(mobis):
  print("NO")
  exit(0)

for alpha in s:
  if alpha in mobis:
    idx = mobis.index(alpha)
    g[idx] += 1

if g.count(0) > 0:
  print("NO")
else:
  print("YES")