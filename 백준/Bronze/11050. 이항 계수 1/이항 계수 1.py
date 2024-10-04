N, K = map(int, input().split())

def fact(N):
    res = 1
    for i in range(1, N+1):
        res *= i
    return res

print(int(fact(N) / (fact(N-K) * fact(K))))