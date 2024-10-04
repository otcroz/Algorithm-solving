N, M = map(int, input().split())

graph = [list(map(str, input())) for _ in range(N)]

res = []
for a in range(N - 7):
    for b in range(M - 7):
        cnt = 0
        index1 = 0
        index2 = 0

        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if graph[i][j] != 'W':
                        index1 += 1
                    if graph[i][j] != 'B':
                        index2 += 1
                else:
                    if graph[i][j] != 'B':
                        index1 += 1
                    if graph[i][j] != 'W':
                        index2 += 1
        res.append(min(index1, index2))
print(min(res))