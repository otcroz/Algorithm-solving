import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
nodes = [0] + [0] +  list(map(int, input().split())) # 연결
connect = [0] + list(map(int, input().split())) # 각 노드의 실력
v = [0] * (n+1) # 방문 여부
d = [[0, 0] for _ in range(n+1)]
tree = [[] for _ in range(n+1)]

# 연결
for i in range(2, n+1):
    tree[nodes[i]].append(i)

def dfs(node):
    v[node] = 1

    for nxt in tree[node]:
        if v[nxt] == 0:
            dfs(nxt)
            d[node][0] += max(d[nxt][0], d[nxt][1]) # node가 멘토링 포함 x > nxt가 포함되든 말든 상관 X

    for nxt in tree[node]: # node가 멘토링 포함 O
        d[node][1] = max(d[node][1], d[node][0] - max(d[nxt][0], d[nxt][1]) + (connect[node]*connect[nxt]) + d[nxt][0])
dfs(1)
print(max(d[1]))