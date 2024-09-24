from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

stack = deque()

# push pop empty size top
for _ in range(n):
    ins = input()
    ins = ins.split()

    if ins[0] == 'push':
        stack.append(int(ins[1]))
    elif ins[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif ins[0] == 'size':
        print(len(stack))
    elif ins[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
    elif ins[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)