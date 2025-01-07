N, M = map(int, input().split(" "))

arr = []
for i in range(N):
  arr.append(int(input()))

arr.sort()

answer = 2000000000
i = 0
left, right = 0, 0

while(right < N):
  tmp = arr[right] - arr[left]

  if tmp < M:
    right += 1
  elif tmp > M:
    answer = min(answer, tmp)
    left += 1
  else:
    answer = M
    break

print(answer)