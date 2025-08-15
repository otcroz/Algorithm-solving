
def solution(k, dungeons):
    
    dungeons.sort(key=lambda x:x[-0])
    
    v = [0] * len(dungeons)
    COUNT = len(dungeons)
    answer = 0
    
    def dfs(energy, n):
        nonlocal answer,k
        answer = max(answer, n)
        if answer == COUNT:
            return
        for i in range(COUNT):
            min_hp, use_hp = dungeons[i]
            if energy >= min_hp and v[i] == 0:
                v[i] = 1
                dfs(energy-use_hp, n+1)
                v[i] = 0
    
    dfs(k,0)
    print(answer)
    return answer