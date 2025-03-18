import sys

input = lambda: sys.stdin.readline().rstrip()

t, w = map(int, input().split())

arr = [0]
for _ in range(t):
    arr.append(int(input()))

d = [[0]*(w+1) for _ in range(t+1)]

for i in range(1, t+1): # 움직이지 않을 때

    #1번 위치에 자두가 떨어질 때
    if arr[i] == 1:
        d[i][0] = d[i-1][0] + 1
    #2번 위치에 자두가 떨어질 때
    else:
        d[i][0] = d[i-1][0]

    for j in range(1, w+1): # 1번 이상 움직일 때
        if (arr[i] == 1 and j%2 == 0) or (arr[i] == 2 and j%2 == 1): # 자두를 받을 때
            d[i][j] = max(d[i-1][j], d[i-1][j-1]) + 1
        else: # 자두를 받지 못할 때
            d[i][j] = max(d[i-1][j], d[i-1][j-1])

print(max(d[t]))