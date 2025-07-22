n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort() #O(n)
v = [0] * n

res = []
def dfs():
    if len(res) == m:
        print(" ".join(map(str, res)))
        return
    for j in range(n):
        if v[j] == 1:
            continue
        res.append(arr[j])
        v[j] = 1
        dfs()
        res.pop()
        v[j] = 0
dfs()