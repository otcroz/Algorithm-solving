from collections import deque

t = int(input())

def bfs():
    q = deque([(home_x,home_y)])

    while q:
        x, y = q.popleft()
        
        if abs(x-fin_x) + abs(y-fin_y) <= 1000:
            print('happy')
            return
        for i in range(store):
            if not visited[i]:
                nx, ny = graph[i]
                if abs(x - nx) + abs(y - ny) <= 1000: # 현재 위치에서 편의점까지
                    visited[i] = 1
                    q.append((nx, ny))
    print('sad')


for _ in range(t):
    store = int(input())
    home_x, home_y = map(int, input().split())
    graph = [tuple(map(int, input().split())) for _ in range(store)]
    fin_x, fin_y = map(int, input().split())

    visited = [0 for _ in range(store + 1)] # 출발 제외
    bfs()