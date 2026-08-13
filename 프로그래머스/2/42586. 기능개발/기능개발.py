from collections import deque

def solution(progresses, speeds):
    answer = []
    
    q = deque(progresses)

    while q:
        leng = len(q)
        cnt = 0 # 같은 날 출시될 때 카운트 계산
        for i in range(leng):
            q[i] += speeds[i]
        while q and q[0] >= 100:
            q.popleft()
            speeds = speeds[1:]
            cnt += 1
        if cnt != 0:
            answer.append(cnt)
        
    return answer

