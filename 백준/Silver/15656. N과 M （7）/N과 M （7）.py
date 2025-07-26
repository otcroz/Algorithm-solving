n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
s = []
v = [0] * n

def back():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(n):
        v[i] = 1
        s.append(arr[i])
        back()
        s.pop()
        v[i] = 0
back()