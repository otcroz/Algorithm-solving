from collections import deque

d = [(0,1), (0,-1), (1,0), (-1,0)]

def solution(maps):
    answer = 0
    
    def in_range(x, y, n, m): # 범위를 확인하는 함수
        if 0<=x<n and 0<=y<m:
            return True
    
    def bfs(i, j, v, n, m, maps): # 너비 탐색 함수
        q = deque([(i, j)])
        v[i][j] = 1

        while q:
            a, b = q.popleft()

            for x, y in d:
                nx, ny = a + x, b + y
                if not in_range(nx, ny, n, m):
                    continue
                if maps[nx][ny] == 0: # 벽일 때
                    continue
                if v[nx][ny] != 0: # 방문했을 때 

                    continue
                q.append((nx, ny))
                v[nx][ny] = v[a][b] + 1
                
        return v[n-1][m-1]
    
    # 상대팀 진영 좌표
    n,m = len(maps), len(maps[0])
    v = [[0]*m for _ in range(n)]
    
    # bfs 탐색
    answer = bfs(0, 0, v, n, m, maps)
    
    # 최소 횟수
    if answer == 0:
        return -1
    else:
        return answer

