from collections import deque

snt = ''

while(True):
    snt = input()
    if snt == ".":
        break

    dq = deque()

    for s in snt:
        if s == '(' or s == '[' :
            cur = s
            dq.append(s)
        elif s == ')':
            if len(dq) != 0 and dq[-1] == '(':
                dq.pop()
            else:
                dq.append(s)
                break
        elif s == ']':
            if len(dq) != 0 and dq[-1] == '[':
                dq.pop()
            else:
                dq.append(s)
                break
    if len(dq) == 0:
        print('yes')
    else:
        print('no')