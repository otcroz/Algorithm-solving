from collections import deque

def solution(n, computers):
    answer = 0
    
    v = [False] * n # 방문여부
    
    def bfs(n): # 노드 번호
        q = deque([n])
        v[n] = True
        
        while q:
            node = q.popleft()
            
            for i, c in enumerate(computers[node]):
                if not v[i] and i != node and c == 1:
                    v[i] = True
                    q.append(i)
                
    for i in range(n):
        if not v[i]: # 방문하지 않았을 때
            answer += 1
            bfs(i)
    
    
    
    return answer