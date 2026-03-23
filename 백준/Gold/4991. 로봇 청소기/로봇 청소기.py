import sys
from collections import deque
input = sys.stdin.readline
d = [(0, -1), (0, 1), (1,0), (-1,0)]

# 청소 여부 확인
def is_clean():
    for i in range(h):
        for j in range(w):
            if g[i][j] == '*':
                return False
    return True

def in_range(y, x):
    if 0 <= y < h and 0 <= x < w:
        return True

# 로봇의 이동
def bfs(cur_pos, tar_pos):
    global w, h, g

    v = [[[0] for _ in range(w)] for _ in range(h)]
    y, x = cur_pos
    q = deque([(y, x, 0)])
    v[y][x] = 1

    while q:
        cur_y, cur_x, cnt = q.popleft()

        if cur_y == tar_pos[0] and cur_x == tar_pos[1]:
            return cnt

        for dy, dx in d:
            ny, nx = dy + cur_y, dx + cur_x
            if not in_range(ny, nx) or g[ny][nx] == 'x':
                continue
            if v[ny][nx] == 1:
                continue
            q.append((ny, nx, cnt + 1))
            v[ny][nx] = 1

    return INF

# 먼지 방문 순서 조합
def make_comb(depth, target_cnt, comb, start_pos, now_length):
    global result, targets, check

    if now_length >= result:
        return
    if depth == target_cnt:
        if now_length < result:
            result = now_length
    
    for i in range(target_cnt):
        if not check[i]:
            n_dist = now_length + dist[start_pos][i]
            comb.append(i)
            check[i] = 1

            make_comb(depth + 1, target_cnt, comb, i, n_dist)

            comb.pop()
            check[i] = 0


INF = int(1e9)
result = INF

while True:
    result = INF
    w, h = map(int, input().rstrip().split())
    if w == 0 and h == 0:
        break

    g = [list(input().rstrip()) for _ in range(h)]
    

    # 출발할 칸 정의
    targets = []
    start_pos = []
    for i in range(h):
        for j in range(w):
            if g[i][j] == "*":
                targets.append([i, j])
            elif g[i][j] == 'o':
                start_pos = [i, j]
    
    # 먼지들 사이의 거리, 청소기 위치
    dist = [[INF for _ in range(len(targets)+1)] for _ in range(len(targets)+1)]

    for i in range(len(targets)):
        for j in range(len(targets)):
            cnt = bfs(targets[i], targets[j])
            dist[i][j] = cnt

    # 먼지와 청소기의 위치 거리
    for i in range(len(targets)):
        cnt = bfs(start_pos, targets[i])
        dist[len(targets)][i] = cnt
        dist[i][len(targets)] = cnt
    dist[len(targets)][len(targets)] = 0

    # 먼지 칸 찾아가는 순서 구함.
    check = [0 for _ in range(len(targets))]
    combs = []
    make_comb(0, len(targets), combs, len(targets), 0)

    if result != int(1e9):
        print(result)
    else:
        print(-1)