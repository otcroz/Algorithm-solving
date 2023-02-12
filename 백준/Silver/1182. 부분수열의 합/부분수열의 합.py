arr = []
count = 0
add = 1

N, S = map(int, input().split())
num = list(map(int, input().split()))


def dfs(start):
    global count
    if sum(arr) == S and len(arr) > 0:
        count += 1

    for i in range(start, N):
        arr.append(num[i])
        dfs(i + 1)
        arr.pop()

dfs(0)
print(count)