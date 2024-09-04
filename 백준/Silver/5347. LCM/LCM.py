from math import gcd

def lcm(n1, n2):
    return  n1*n2 // gcd(n1, n2)

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))