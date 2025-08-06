n,k = map(int, input().split())
things = [tuple(map(int, input().split())) for _ in range(n)]

d = [[0] * (k+1) for _ in range(n+1)] # 2차원 배열 d[n][k] 개수에 따라서 무게, 가치 최대

for i in range(1, n+1):
    w, v = things[i-1]
    for j in range(k+1): # j 무게까지 사용할 때
        if j < w:
            # 물건을 담지 X
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j-w] + v, d[i-1][j]) # 물건 추가 vs 물건 추가 x
print(d[n][k])