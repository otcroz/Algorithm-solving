from collections import deque
import sys

cur = 1
arr = []
dq = deque()
flag = 0

N = int(input())

for i in range(N):
    num = int(sys.stdin.readline())
    while cur <= num:
        dq.append(cur)
        arr.append('+')
        cur += 1

    if dq[-1] == num:
        dq.pop()
        arr.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in arr:
        print(i)