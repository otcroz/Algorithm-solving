from collections import deque

def solution(n, edge):
    answer = 0
    
    g = [[] for _ in range(n+1)]
    
    for a, b in edge:
        g[a].append(b); g[b].append(a)
    
    # 변수 정의
    dist = [-1] * (n+1) # 거리
    q = deque([1])
    dist[1] = 0
    
    while q:
        node = q.popleft()
        for nxt in g[node]:
            if dist[nxt] == -1:
                dist[nxt] = dist[node] + 1
                q.append(nxt)
    
    max_dist = max(dist)
    answer = dist.count(max_dist)
    
    return answer