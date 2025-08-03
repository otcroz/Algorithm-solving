from sys import stdin
input = stdin.readline
arr = list(input())

change = ('0', '1')
res = []
for i in range(2): # 0, 1을 뒤집는 경우의 수
  flip = 0 # 뒤집는 횟수
  copy = arr[:]

  j = 0
  while j < len(arr):
    if copy[j] == change[i]:
      copy[j] = change[i-1]
      flip += 1
      
      while True:
        if j+1 < len(arr):
          if copy[j+1] == change[i]:
            copy[j+1] = change[i-1]
            j += 1
          else: break
        else: break
    j+=1
      
  res.append(flip)

print(min(res))