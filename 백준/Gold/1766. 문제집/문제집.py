import heapq

N, M = map(int, input().split())
answer = []
g = [[] for _ in range(N+1)]
inDegree = [0] * (N+1)
h = []

for i in range(M):
    first, second = map(int, input().split())
    g[first].append(second)
    inDegree[second] += 1

for i in range(1, N+1):
    if inDegree[i] == 0:
        heapq.heappush(h, i)
#print(g, inDegree)
while h:
    tmp = heapq.heappop(h)
    answer.append(tmp)
    for i in g[tmp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(h, i)

print(' '.join(map(str, answer)))