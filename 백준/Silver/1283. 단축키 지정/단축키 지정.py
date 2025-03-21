N = int(input())

keys = []
for _ in range(N):
  s = list(input().split())

  flag = False
  for i in range(len(s)):
    if s[i][0].lower() not in keys:
      flag = True
      keys.append(s[i][0].lower())
      s[i] = '[' + s[i][0] + ']' + s[i][1:]
      print(' '.join(s))
      break
  
  if not flag:
    for i in range(len(s)):
      check = False
      for j in range(len(s[i])):
        if s[i][j].lower() not in keys:
          keys.append(s[i][j].lower())
          flag = True
          check = True
          s[i] = s[i][:j] + '[' + s[i][j] + ']' + s[i][j+1:]

          print(' '.join(s))
          break
      if check: break
  
  if not flag:
    print(' '.join(s))