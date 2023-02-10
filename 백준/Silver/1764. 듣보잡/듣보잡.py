import sys

arr1 = []
arr2 = []

N, M = map(int, input().split())

for i in range(N):
    arr1.append(sys.stdin.readline())
    
for i in range(M):
    arr2.append(sys.stdin.readline())

arr1 = set(arr1)
arr2 = set(arr2)

ans = list(arr1 & arr2)
ans.sort()

print(len(ans))
for name in ans:
    print(name, end='')
