N, M = map(int, input().split())

s = []

def dfs(start):
    # 길이가 같으면 출력 후 return
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    # push, pop
    for i in range(start, N+1):
        s.append(i)
        dfs(i)
        s.pop() # 마지막 숫자 제거
dfs(1)