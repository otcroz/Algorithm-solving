from collections import deque

level_change = []

def solution(begin, target, words):
    ALPHA_CNT = len(begin)
    # 스펠링이 다른 알파벳 개수 확인
    def check_diff_spell(tar, cur):
        cnt = 0
        for i in range(ALPHA_CNT):
            if tar[i] != cur[i]:
                cnt += 1
        return cnt
    
    def bfs(begin, target):
        global level_change
        q = deque([(begin, 0)])
        
        while q:
            cur, cnt = q.popleft() # 현재 알파벳
            for word in words:
                # 타겟에 도달했을 때
                if cur == target:
                    level_change.append(cnt)
                    return
                # 알파벳 비교 수행
                res = check_diff_spell(cur, word)
                
                if res == 1: # 다른 알파벳이 1개일 때
                    q.append((word, cnt+1))
        
    #target이 words 내에 있는지 확인
    if target not in words:
        return 0
    
    bfs(begin, target)
    
    return min(level_change)