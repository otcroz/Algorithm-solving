import sys


a = []

size = int(input())

for i in range(size):
    a.append(int(sys.stdin.readline()))

a.sort()

for i in range(size):
    sys.stdout.write(str(a[i]) + "\n")
