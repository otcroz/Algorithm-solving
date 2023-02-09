import sys

n1 = int(input())
A = set(map(int, input().split()))

n2 = int(input())
M = list(map(int, input().split()))

for i in range(len(M)):
        if M[i] in A:
            sys.stdout.write(str(1) + "\n")
        else:
            sys.stdout.write(str(0) + "\n")
