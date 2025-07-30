T = int(input())

for _ in range(T):
    n=int(input())
    big_n=n+1

    str_n = str(n)
    
    if big_n % int(str_n[-2:]) != 0:
        print("Bye")
    else:
        print("Good")