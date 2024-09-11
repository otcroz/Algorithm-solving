from array import ArrayType


n, m = map(int, input().split())

arr = [0]
for i in range(46):
    for _ in range(i):
        arr.append(i)

print(sum(arr[n: m+1]))