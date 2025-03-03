a, b = map(int, input().split())

visited = [False] * (a+1)
arr = []

def dfs():
    if len(arr) == b:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1, a+1):
        if visited[i]:
            continue
        else:
            visited[i] = True
            arr.append(i)
            dfs()
            arr.pop()
            visited[i] = False
dfs()