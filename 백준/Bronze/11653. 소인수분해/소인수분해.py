n = int(input())

i = 2
for i in range(2, n+1):
    if n % i == 0:
        while n % i == 0 : # 소수, 나누어질 때까지 반복
            print(i)
            n /= i