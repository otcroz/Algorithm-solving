from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F + 1)]

def bfs():
    q = deque([])
    q.append(S)

    visited[S] = 1

    while q:
        y = q.popleft()
        
        if y == G:
            return visited[y] - 1
        else:
            for x in (y + U, y - D):
                if (0 < x <= F) and visited[x] == 0:
                    visited[x] = visited[y] + 1
                    q.append(x)
    return 'use the stairs'

print(bfs())