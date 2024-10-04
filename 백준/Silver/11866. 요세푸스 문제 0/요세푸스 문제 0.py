from collections import deque

N, K = map(int, input().split())

dq = [i+1 for i in range(N)]

idx = 0
res = []
while dq:
    idx += K - 1
    if idx >= len(dq):
        idx %= len(dq)    
    res.append(str(dq.pop(idx)))

print('<', ", ".join(res), '>', sep="")