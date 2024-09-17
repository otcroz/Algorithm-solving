import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

left = 0
right = n - 1

cnt = 0
while left < right:
  if arr[left] + arr[right] > x:
    right -= 1
  elif arr[left] + arr[right] < x:
    left += 1
  else:
    cnt += 1
    left += 1
    right -= 1
print(cnt)