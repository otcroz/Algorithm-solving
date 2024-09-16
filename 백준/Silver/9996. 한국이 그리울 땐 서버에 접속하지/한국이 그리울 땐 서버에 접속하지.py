n = int(input())
start, end = input().split('*')
length = len(start) + len(end)

for i in range(n):
  s = input()

  if len(s) < length:
    print('NE')
  elif s[:len(start)] == start and s[-len(end):] == end:
    print("DA")
  else:
    print("NE")