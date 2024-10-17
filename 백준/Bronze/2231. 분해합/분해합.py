N = int(input())

min = 1000000
for i in range(N, 0, -1): # 거꾸로
    sub = N - i
    sub_sum = sum(list(map(int, str(i))))
    if sub == sub_sum:
        if min > sub_sum:
            min = i
if min == 1000000:
    min = 0
print(min)