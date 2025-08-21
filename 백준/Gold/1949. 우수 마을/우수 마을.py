import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
village = list(map(int, input().split()))
v = [0] * n # 마을 방문 여부
d = [[0, 0] for _ in range(n)] # 최대값 저장
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1) 
    g[b-1].append(a-1)

# 우수 마을 최댓값
def dfs(node):
    v[node] = 1
    d[node][0] = 0 # node가 우수마을이 아닐 때
    d[node][1] = village[node] # node가 우수마을일 때

    for nxt in g[node]: # 연결된 노드 탐색
        if v[nxt] == 0:
            dfs(nxt)
            d[node][0] += max(d[nxt][0], d[nxt][1]) # 연결된 마을은 우수마을의 여부 상관 없음
            d[node][1] += d[nxt][0] # 연결된 마을은 우수마을이면 안된다.

dfs(0)
print(max(d[0][0], d[0][1]))