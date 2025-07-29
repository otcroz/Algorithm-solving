import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
v = [0] * len(arr)

res = []
res_comb = set()
def back(res_comb):
    if len(res) == m:
        res_tuple = tuple(res)
        if res_tuple not in res_comb: #동일한 조합이 없는 경우에만
            res_comb.add(res_tuple)
        return
    for i in range(len(arr)):
        if v[i] == 0:
            v[i] = 1
            res.append(arr[i])
            back(res_comb)
            res.pop()
            v[i] = 0
back(res_comb)
for res in sorted(res_comb):
    print(' '.join(map(str, res)))