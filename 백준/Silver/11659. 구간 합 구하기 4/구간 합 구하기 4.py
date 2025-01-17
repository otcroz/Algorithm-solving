N, M = map(int, input().split())

arr = list(map(int, input().split()))

part_sum = [0]
tmp = 0
for i in arr:
    tmp += i
    part_sum.append(tmp)

for _ in range(M):
    a, b = map(int, input().split())
    res = part_sum[b] - part_sum[a - 1]

    print(res)