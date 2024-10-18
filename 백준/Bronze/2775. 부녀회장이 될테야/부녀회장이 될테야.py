T = int(input())

zero_level = [i for i in range(1, 15)]
apart = []
apart.append(zero_level)

for h in range(1, 15):
    temp = []
    for i in range(1, 15):
        sum = 0
        for j in range(0, i):
            sum += apart[h-1][j]
        temp.append(sum)
    apart.append(temp)

for _ in range(T):
    k = int(input())
    n = int(input())

    print(apart[k][n-1])