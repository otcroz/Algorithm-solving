n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
s = []
v = [0] * n

def back(a):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(a, n):
        if v[i] == 0:
            v[i] = 1
            s.append(arr[i])
            back(i+1)
            s.pop()
            v[i] = 0
back(0)