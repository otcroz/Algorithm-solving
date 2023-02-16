N = int(input())

if N < 100:
    print(N)
else:
    cnt = 99
    for n in range(100, N+1):
        num = str(n)

        arr = []
        for i in range(len(num) -1):
            arr.append(int(num[i+1]) - int(num[i]))

        if arr.count(arr[0]) == len(arr):
            cnt += 1
    print(cnt)