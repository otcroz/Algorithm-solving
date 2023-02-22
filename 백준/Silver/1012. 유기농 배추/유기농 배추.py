from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

T = int(input())
link = 0

def bfs(a, b):
  Q = deque([(a, b)])
  while Q:
    x, y = Q.popleft()
  
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
  
      if 0 <= nx < N and 0 <= ny < M:
        if graph[nx][ny] == 1:
          graph[nx][ny] = 0
          Q.append([nx, ny])
        

test_count = 0
while test_count < T:
  M, N, K = map(int, input().split())
  graph = [[] for _ in range(N)]
  
  # 초기화
  for i in range(N):
    for k in range(M):
      graph[i].append(int('0')) 
  
  # 배추의 위치
  for i in range(K):
    a, b = map(int, input().split())
    graph[b][a] = 1
  
  # 탐색
  for i in range(N):
    for j in range(M):
      if graph[i][j] == 1:
        link += 1
        graph[i][j] = 0
        bfs(i, j)
     
  print(link)
  link = 0
  test_count += 1