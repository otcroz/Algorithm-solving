import sys

input = lambda: sys.stdin.readline().rstrip()

N, d, k, c = map(int, input().split())

dishes = [int(input()) for _ in range(N)]

dishes += dishes[0:k]
dished_length = len(dishes)
max_cnt = 0

for i in range(0, dished_length-k):
    temp = list(set(dishes[i:i+k]))
    cnt = len(temp)
    if c not in temp:
        cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)