import sys

arr = []
ans = []
flag = 0

N = int(input())

for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort(reverse=True)

for i in range(N-2):
    for j in range(i+1, N- 1):
        if arr[i] < arr[j] + arr[j+1]:
            ans.extend([arr[i], arr[j], arr[j+1]])
            flag = 1
            break

    if flag == 1: break

if flag == 1:
    print(sum(ans))
else: print(-1)
