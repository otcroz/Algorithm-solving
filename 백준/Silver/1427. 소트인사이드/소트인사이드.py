import sys

arr = []

num = input()
arr = list(num)

arr.sort(reverse=True)

for i in range(len(num)):
    print(arr[i], end='')