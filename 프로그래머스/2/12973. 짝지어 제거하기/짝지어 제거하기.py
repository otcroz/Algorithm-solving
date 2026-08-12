from collections import deque

def solution(s):
    
    origin = deque(list(map(str, s))[1:])
    q = [s[0]]
    
    while origin:
        target = origin.popleft()
        
        if q:
            if q[-1] == target:
                q.pop()
            else:
                q.append(target)
        else:
            q.append(target)
    if q:
        return 0
    else:
        return 1