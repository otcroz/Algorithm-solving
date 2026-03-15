import sys
input = sys.stdin.readline

n, m = map(int, input().split())
names = [int(input()) for _ in range(n)]

d = [[-1] * (m+1) for _ in range(n)] # 저장값: 나머지 제곱
d[0][names[0]] = 0 # 첫 번째 이름

for r in range(n-1):
    for c in range(1, m+1):
        if d[r][c] != -1:
            # 뒤에 이름을 붙이는 경우
            if c+1+names[r+1] <= m:
                d[r+1][c+names[r+1]+1] = d[r][c]
            
            # 다음 줄에 이름을 쓰는 경우
            if d[r+1][names[r+1]] != -1:
                d[r+1][names[r+1]] = min(d[r+1][names[r+1]], d[r][c] + (m-c)**2)
            else:
                d[r+1][names[r+1]] = d[r][c] + (m-c)**2

ans = int(1e9)
for i in range(1, m+1):
    if d[n-1][i] != -1:
        ans = min(ans, d[n-1][i])
print(ans)