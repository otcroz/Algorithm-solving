X = int(input())

d = [0] * 1000001

for i in range(2, X+1):
    d[i] = d[i-1] + 1 # 1을 빼줌

    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)

print(d[X])