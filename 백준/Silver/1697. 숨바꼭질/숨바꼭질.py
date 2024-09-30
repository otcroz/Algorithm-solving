import sys
from collections import deque
input = sys.stdin.readline

MAX = 10**5 # 동생, 내가 갈 수 있는 최대 점, 시간초과 방지
visited = [0] * (MAX + 1)

n, m = map(int, input().split())

def bfs(n):
    dq = deque([n])
    
    while dq:
        a = dq.popleft()
        
        if a == m:
            return visited[m]
        
        for i in (a + 1, a - 1, a * 2):
            if 0 <= i <= MAX and not visited[i]:
                dq.append(i)
                visited[i] = visited[a] + 1

print(bfs(n))