N, L = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]

def check(line):
    used = [0] * N
    for i in range(N-1):
        if line[i] == line[i+1]:
            continue
        diff = line[i+1] - line[i]
        # 높이 차 2 이상이면 불가
        if abs(diff) > 1:
            return False
        # 오르막
        if line[i] < line[i+1]:
            h = line[i]
            for j in range(i, i-L, -1):
                if j < 0 or line[j] != h or used[j]:
                    return False
                used[j] = 1
        # 내리막
        else:
            h = line[i+1]
            for j in range(i+1, i+1+L):
                if j >= N or line[j] != h or used[j]:
                    return False
                used[j] = 1
    return True


cnt = 0 # 지나갈 수 있는 길
for i in range(N):
    if check(g[i]): # 행
        cnt += 1
    if check([g[j][i] for j in range(N)]): # 열
        cnt += 1

print(cnt)