def solution(n, lost, reserve):
    answer = 0
    lost.sort(); reserve.sort()
    
    remove_res = []
    # 자신이 도난당한 경우
    for i in range(len(reserve)):
        if reserve[i] in lost: # 본인이 도난당한 경우
            remove_res.append(reserve[i])
            lost.remove(reserve[i])
    for item in remove_res:
        reserve.remove(item)
    
    while reserve:
        res = reserve.pop()
        
        for nxt_res in range(res+1, res-2, -2):
            if 0 < nxt_res <= n:
                if nxt_res in lost:
                    lost.remove(nxt_res)
                    break
                    
    answer = n - len(lost)
    return answer