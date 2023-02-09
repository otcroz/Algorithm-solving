import sys

N = int(input())
list = []

for i in range(N):
    n = int(sys.stdin.readline())

    if n==0 :
        list.pop()
    else:
        list.append(n)


print(sum(list))
