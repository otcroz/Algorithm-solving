n = int(input())

for i in range(n):
    a, b = map(sorted, input().split())
    
    if a==b: print("Possible")
    else: print("Impossible")