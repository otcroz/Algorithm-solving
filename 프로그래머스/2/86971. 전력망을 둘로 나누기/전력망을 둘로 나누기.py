from collections import deque
def solution(n, wires):
    
    # 그래프 등록, 방문 여부
    g = [[] for _ in range(n+1)]
    v = [0] * (n+1)
    
    for line in wires:
        node1, node2 = line[0], line[1]
        g[node1].append(node2)
        g[node2].append(node1)
    
    def bfs(v, res, i):
        nonlocal g
        q = deque([i])
        v[i] = 1
        cnt = 0
        
        while q:
            new = q.popleft()
            for node in g[new]:
                if v[node] == 0:
                    q.append(node)
                    v[node] = 1
                    cnt += 1 # 전선의 길이
        res.append(cnt)
        
        
    
    # 전선 하나씩 빼면서 각 전력망 길이의 차가 최소인 값 구하기
    min_len = 100 # 전선의 길이 차 최솟값
    for line in wires:
        # 변수 초기화
        v = [0] * (n+1)
        res = [] # 전선 길이들, 2개여야 함.
        # 전선 하나 제거하기
        node1, node2 = line[0], line[1]
        g[node1].remove(node2)
        g[node2].remove(node1)
        
        # 송전탑의 전선의 길이 각각 구하기
        for i in range(1, n+1):
            if v[i] == 0:
                bfs(v, res, i)
        print(res)
        
        if len(res) == 2: # 2개로 분할되었는지 확인
            min_len = min(min_len, abs(res[0] - res[1]))
        else:
            continue
        
        # 제거했던 전선 다시 추가하기
        g[node1].append(node2)
        g[node2].append(node1)
    
    
    return min_len