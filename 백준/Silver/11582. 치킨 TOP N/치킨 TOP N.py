N = int(input())
c = list(map(int, input().split()))
k = int(input())

index = N // k

for i in range(0, N, index):
  arr = c[i:i+index]
  arr.sort()
  for j in arr:
    print(j, end=' ')