from collections import deque

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

# 초기 상어 위치
for i in range(n):
    for j in range(n):
        if g[i][j] == 9:
            sx, sy = i, j
            g[i][j] = 0

# 변수 설정
time = 0 # 물고기가 도움 요청 없이 체류한 시간
fish_size = 2 # 아기상어 크기
eat = 0 # 물고기를 먹은 횟수
d = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 북 서 남 동

# 범위 내인지 확인
def in_range(x, y):
    if 0 <=x < n and 0<=y<n:
        return True

# 현재 공간 물고기 확인: 모두 0이거나, 아기 상어의 크기보다 큰 경우 return true
def check_space():
    for i in range(n):
        for j in range(n):
            if g[i][j] != 0 and g[i][j] < fish_size:
                return False
    return True # 더 이상 먹을 수 있는 물고기가 없을 때

# bfs: 물고기 상하좌우 이동
def bfs(i, j, fish_size):
    dist = [[-1]*n for _ in range(n)] # 이동 최단 거리 기록
    dist[i][j] = 0
    q = deque([(i, j)]) # 위치, 이동 시간
    fish = []
    
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and dist[nx][ny] == -1:
                if fish_size >= g[nx][ny]: # 지나갈 수 있는 경우
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny)) # 이동할 경로 추가
                    if 0 < g[nx][ny] < fish_size: # 먹을 수 있는 경우
                        fish.append((dist[nx][ny], nx, ny))
    return sorted(fish) # 거리, 행, 열 순으로 정렬

# 실행
while True:
    fish = bfs(sx, sy, fish_size)
    if not fish:
        break
    dist, nx, ny = fish[0]
    time += dist # 시간 추가
    sx, sy = nx, ny # 상어의 위치
    g[nx][ny] = 0
    eat += 1 # 물고기가 
    if fish_size == eat: # 물고기 크기만큼 먹었을 때
        fish_size += 1
        eat = 0

print(time)