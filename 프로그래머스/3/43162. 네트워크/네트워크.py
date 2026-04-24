def solution(n, computers):
    answer = 0
    v = [False] * n
    
    def func(node):
        nonlocal v
        v[node] = True
        for j in range(len(computers)):
            if not v[j] and node != j and computers[node][j] == 1:
                func(j)
            
    for i in range(len(computers)):
        if not v[i]:
            answer += 1
            func(i)

    return answer