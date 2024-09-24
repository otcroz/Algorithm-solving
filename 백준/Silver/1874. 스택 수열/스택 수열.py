import sys
from collections import deque

input = sys.stdin.readline
stack = deque()
arr = [] # 부호
flag = 0
cur = 1 # 현재 숫자

N = int(input())

for _ in range(N):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        arr.append('+')
        cur+=1
    
    if stack[-1] == num:
        stack.pop()
        arr.append('-')
    else:
        print('NO')
        flag = 1
        break
if flag == 0:
    for i in arr:
        print(i)