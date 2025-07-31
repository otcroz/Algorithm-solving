n = int(input())
d = [0] * (n+1)

if n == 1: print(1); exit(0)
if n == 2: print(2); exit(0)
d[1] = 1
d[2] = 2
for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]) % 15746

print(d[n])