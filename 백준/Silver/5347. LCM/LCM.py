n = int(input())

def gcd(n1, n2): 
    while (n2 != 0):
        n1, n2 = n2, n1 % n2
    
    return n1


for _ in range(n):
    a, b = map(int, input().split())

    if a > b:
        print((a*b) // gcd(a, b))
    else:
        print((a*b) // gcd(b, a))