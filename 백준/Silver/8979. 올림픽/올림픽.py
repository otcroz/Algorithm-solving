n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))

# 순위 정하기
res = set()
res.add((arr[0][0], 1))
score = 1
for i in range(1, n):
    num = arr[i][0]
    if arr[i][3] == arr[i-1][3] and arr[i][1] == arr[i-1][1] and arr[i][2] == arr[i-1][2]:
        res.add((num, score))
    else: # 순위 반영
        score = len(arr[:i]) + 1
        res.add((num ,score))
#print("res: ", res)
for item in res:
    if item[0] == k:
        print(item[1])
        break