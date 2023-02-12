arr = []

N = int(input())
a = input()
a = list(a)

for i in range(N):
    num = (ord(a[i]) - (ord('a') - 1))*(31**i)
    arr.append(num)

res = sum(arr)
print(res)