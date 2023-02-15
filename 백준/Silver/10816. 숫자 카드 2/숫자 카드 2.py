from collections import Counter
import sys

N = int(input())
arr1 = list(map(int, sys.stdin.readline().split()))
arr1.sort()

M = int(input())
arr2 = list(map(int, sys.stdin.readline().split()))

cnt = Counter(arr1)

for i in arr2:
    print(cnt[i], end=' ')