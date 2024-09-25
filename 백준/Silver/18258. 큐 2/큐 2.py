from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
dq = deque()

for _ in range(N):
    n = input().split()

    if n[0] == 'push':
        dq.append(n[1])
    elif n[0] == 'pop':
        if len(dq) == 0:
            print( -1)
        else:
            print(dq.popleft())
    elif n[0] == 'size':
        print(len(dq))
    elif n[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif n[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif n[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[len(dq)-1])