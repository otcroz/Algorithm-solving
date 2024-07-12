A = int(input())
B = int(input())
C = int(input())

res = A*B*C


num = list(str(res))

for i in range(0, 10):
    print(num.count(str(i)))
