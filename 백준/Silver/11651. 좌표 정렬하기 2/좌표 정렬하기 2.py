import sys

arr = []

N = int(input())

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(str(arr[i][0]) + " " + str(arr[i][1]))
