from collections import deque

# 6방향 정의
directions = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1 ,0, 0)]

def in_range(l, x, y):
  if 0 <= x < R and 0 <= y < C and 0 <= l < L:
    return True

def bfs(level, x, y):
  global graph, v
  q = deque([(level, x, y)])
  v[level][x][y] = 0

  while q:
    l, a, b = q.popleft()

    for d in directions:
      nlvl, nx, ny = l + d[0], a + d[1], b + d[2]
      #print("현재 좌표: ", nlvl, nx, ny)

      if not in_range(nlvl, nx, ny):
        continue
      if graph[nlvl][nx][ny] == '#':
        continue
      if v[nlvl][nx][ny] != -1:
          continue
      
      if (nlvl, nx, ny) == (end[0], end[1], end[2]):
        v[nlvl][nx][ny] = v[l][a][b] + 1 
        return True
      
      q.append((nlvl, nx, ny))
      v[nlvl][nx][ny] = v[l][a][b] + 1
      #print("current: ", nlvl, nx, ny)
      #print("step_cnt: ", v[nlvl][nx][ny])
  return False

while True:
  L, R, C = map(int, input().split())

  # 종료 조건 확인
  if L == 0 and R == 0 and C == 0:
    break

  start, end = [0,0,0], [0,0,0] # 시작 위치와 도착 위치 설정
  graph = []
  v = [[[-1]*C for _ in range(R)] for _ in range(L)]
  for i in range(L):
    temp = []
    for _ in range(R):
      temp.append(list(input()))
    graph.append(temp)
    input() # 공백 유지

    # S 또는 E가 그래프 내에 있는지 확인
    for r in range(R):
      for c in range(C):
        if graph[i][r][c] == "S":
          start[0], start[1], start[2] = i, r, c
        if graph[i][r][c] == "E":
          end[0], end[1], end[2] = i, r, c

  #print("start, end", start, end)
  #print("graph: ", graph)
  #print(v)
  res = bfs(start[0], start[1], start[2])
  #print(res)
  if res:
    print(f'Escaped in {v[end[0]][end[1]][end[2]]} minute(s).')
  else:
    print('Trapped!')