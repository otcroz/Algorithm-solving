n = input()
arr = [0] * 10

for i in range(len(n)):
  num = int(n[i])
  if num == 6 or num == 9:
    if arr[6] <= arr[9]:
      arr[6] += 1
    else:
      arr[9] += 1
  else:
    arr[num] += 1
print(max(arr))