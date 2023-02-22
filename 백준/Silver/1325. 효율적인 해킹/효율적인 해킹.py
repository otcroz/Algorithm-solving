import sys
from collections import deque
input = sys.stdin.readline


def count(where):
    q = deque()
    q.append(where)
    visited = [False] * (N+1)
    visited[where] = True
    cnt = 1
    while q:
        node = q.popleft()
        for nnode in arr[node]:
            if not visited[nnode]:
                q.append(nnode)
                cnt += 1
                visited[nnode] = True
    return cnt


N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[b].append(a)

result = []
for i in range(N+1):
    result.append(count(i))

max_value = max(result)
for i in range(1, N+1):
    if result[i] == max_value:
        print(i, end=' ')