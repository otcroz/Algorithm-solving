import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = [tuple(map(int,input().split())) for _ in range(n)]

left, right = 0, int(1e9)
answer = -1

def count(x):
    return sum(1 for a, b in s if a + x >= b)

while left <= right:
    mid = (left+right) // 2
    if count(mid) >= k:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)