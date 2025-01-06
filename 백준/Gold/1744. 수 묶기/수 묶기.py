N = int(input())

minus_n = []
plus_n = []
res = 0
for i in range(0, N):
  tmp = int(input())

  if tmp > 1:
    plus_n.append(tmp)
  elif tmp <= 0:
    minus_n.append(tmp)
  else:
    res += tmp
      
plus_n.sort(reverse=True)
minus_n.sort()

# 양수일 때
for i in range(0, len(plus_n), 2):
  if i+1 >= len(plus_n):
    res += plus_n[i]
  else:
    res += plus_n[i]*plus_n[i+1]

# 음수일 때
for i in range(0, len(minus_n), 2):
  if i+1 >= len(minus_n):
    res += minus_n[i]
  else:
    res += minus_n[i]*minus_n[i+1]

print(res)