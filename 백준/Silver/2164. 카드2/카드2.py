from collections import deque
import sys

input = sys.stdin.readline
dq = deque()
cnt = 0

N = int(input())
for i in range(N):
    dq.append(i+1)

while(len(dq) != 1):
    if cnt % 2 == 0:
        dq.popleft()
    else:
        temp = dq.popleft()
        dq.append(temp)
    cnt += 1
print(dq[0])