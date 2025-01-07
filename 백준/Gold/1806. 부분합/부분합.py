N, S = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

left, right = 0, 0
tmp = 0
answer = 100000

while True:
  if tmp >= S:
    answer = min(right - left, answer)
    tmp -= arr[left]
    left += 1
  elif right == N:
    break
  else:
    tmp += arr[right]
    right += 1

if answer == 100000:
  answer = 0

print(answer)