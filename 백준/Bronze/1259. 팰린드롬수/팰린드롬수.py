res = []
flag = 0

while True:
    flag = 0
    s = input()
    if s == '0': break
    for i in range(int(len(s)/2)):
        if(s[i] != s[-i-1]):
            print('no')
            flag = 1
            break
    if flag == 0:
        print('yes')