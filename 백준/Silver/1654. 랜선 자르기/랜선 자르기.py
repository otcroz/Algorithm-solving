arr = []

N, line = map(int, input().split())

for i in range(N):
    arr.append(int(input()))

start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for n in arr:
        cnt += n // mid 

    if cnt >= line: # mid의 제곱이 n보다 작으면
        start = mid + 1
    elif cnt < line:
        end = mid - 1
print(end)
