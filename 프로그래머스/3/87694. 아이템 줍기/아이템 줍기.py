from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    
    rectangle = [
    [sx * 2, sy * 2, ex * 2, ey * 2]
    for sx, sy, ex, ey in rectangle]
    
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    answer = 0
    d = [(0,1),(0,-1),(1,0),(-1,0)]
    
    route = [] # 가장자리 루트
    
    # 직사각형의 모든 가장자리 저장
    for rect in rectangle:
        sx, sy, ex, ey = rect[0], rect[1], rect[2], rect[3]
        
        for x in range(sx, ex+1):
            route.append((x, sy))
            route.append((x, ey))
            
        for y in range(sy, ey+1):
            route.append((sx, y))
            route.append((ex, y))
    
    # 직사각형 범위 내에 포함되는 가장자리 제거
    new_route = []
    for r in route:
        flag = 0
        for rect in rectangle:
            sx, sy, ex, ey = rect[0], rect[1], rect[2], rect[3]
            if sx < r[0] < ex and sy < r[1] < ey:
                flag = 1
                break
        if flag == 0:
            new_route.append(r)

    route = set(new_route)
    
    
    def bfs(cur_x, cur_y): # 캐릭터 이동
        q = deque([(cur_x, cur_y, 1)])
        v = {(cur_x, cur_y)}
        
        while q:
            a, b, cnt = q.popleft()
            
            if (a, b) == (itemX, itemY):
                return cnt // 2
            
            for dx, dy in d:
                nx, ny = a + dx, b + dy
                if (nx, ny) in route and (nx, ny) not in v:                    
                    v.add((nx, ny))
                    q.append((nx, ny, cnt+1))
    
    answer = len(route) # 최댓값
    
    answer = bfs(characterX, characterY)
    
    return answer