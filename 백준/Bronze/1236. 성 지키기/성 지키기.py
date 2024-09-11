n, m = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]

a = 0
for i in range(n):
    if 'X' not in arr[i]:
        a += 1
b = 0
for i in range(m):
    temp = ''
    for j in range(n): 
        temp += arr[j][i]
    if 'X' not in temp:
        b += 1

print(max(a, b))