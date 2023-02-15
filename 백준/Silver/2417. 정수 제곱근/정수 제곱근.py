n = int(input())

start = 0
end = n

while start <= end:
    mid = (start + end) // 2

    if mid**2 < n: # mid의 제곱이 n보다 작으면
        start = mid + 1
    else:
        end = mid - 1

print(start)