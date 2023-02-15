cnt = 0

L = int(input())
arr = list(map(int, input().split()))
num = int(input())

arr.sort()

if num in arr:
    print(0)
else:
    min = 0
    max = 0

    for n in arr:
        if n < num:
            min = n
        elif n > num and max == 0:
            max = n
    max -= 1
    min += 1
    print((num-min)*(max-num+1) + (max-num))