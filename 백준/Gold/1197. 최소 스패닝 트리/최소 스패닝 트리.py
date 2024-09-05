import sys
sys.setrecursionlimit(10**6)  # 재귀 한도를 10^6으로 설정

v, e = map(int, input().split())

edges = []

for _ in range(e):
    edges.append(list(map(int, input().split())))

root = dict()
for i in range(1, v+1):
    root[i] = i

def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]

def union(x, y):
    x = find(x)
    y = find(y)

    root[y] = x

edges = sorted(edges, key=lambda x: x[2])

cost = 0

for edge in edges:
    if find(edge[0]) == find(edge[1]): # 사이클인 경우
        continue
    else:
        cost += edge[2]
        union(edge[0], edge[1]) # 엣지 연결

print(cost)