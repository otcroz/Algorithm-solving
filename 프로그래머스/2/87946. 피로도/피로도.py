def solution(k, dungeons):
    answer = -1
    v = [] # 방문 던전
    
    def dfs(cur_k, v, cnt): # 현재 피로도, 던전
        nonlocal answer
        
        for i in range(len(dungeons)):
            if cur_k < dungeons[i][0]:
                answer = max(answer, cnt)
                continue
            if i not in v:
                v.append(i)
                dfs(cur_k - dungeons[i][1], v, cnt + 1)
                v.pop()
        
    dfs(k, v, 0)
    
    if answer == -1:
        return 0
    else:
        return answer