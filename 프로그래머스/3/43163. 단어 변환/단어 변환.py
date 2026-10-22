from collections import deque

def solution(begin, target, words):
    answer = 0
    v = [False] * len(words)
    
    # target이 words에 없을 때
    if target not in words:
        return answer
    
    def check_spell_cnt(cur, nxt):
        cnt = 0
        for i in range(len(cur)):
            if cur[i] != nxt[i]:
                cnt += 1
        if cnt == 1:
            return True
        else:
            return False
        
    
    def bfs(begin):
        q = deque([(begin, 0)])
        cnt = 0
        
        while q:
            current, cnt = q.popleft()
            
            if current == target:
                return cnt
            
            for i, next in enumerate(words):
                if check_spell_cnt(current, next) == 1:
                    v[i] = True
                    q.append((next, cnt+1))
        
    
    answer = bfs(begin)
    
    
    return answer