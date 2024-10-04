N, M = map(int, input().split())

arr = list(map(int, input().split()))
max = 0

arr.sort()

for i in range(N - 2):
    for j in range(1, N - 1):
        for k in range(2, N):
            if i == j or i == k or j == k:
                continue
            else:
                s = arr[i] + arr[j] + arr[k]
                if s > max and s <= M:
                    max = s
print(max)