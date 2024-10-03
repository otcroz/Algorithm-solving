n, m = map(int, input().split())

s = []
def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if i not in s: # 중복x
            s.append(i)
            dfs()
            s.pop() # 부모 노드 이동
dfs()