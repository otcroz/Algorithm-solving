from collections import deque

v = [-1] * 100001

def bfs(n, k):
    v[n] = 0
    q = deque([n])
    
    while q:
        x = q.popleft()

        if x == k:
            return v[k]
        
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx < 100001:
                if v[nx] == -1:
                    if nx == 2*x: 
                        v[nx] = v[x]
                        q.appendleft(nx) # 2*x를 먼저 처리해줘야 한다.
                    else:
                        v[nx] = v[x] + 1
                        q.append(nx)
                    
    return -1

n, k = map(int, input().split())

if n == k:
    print(0)
else:
    print(bfs(n, k))