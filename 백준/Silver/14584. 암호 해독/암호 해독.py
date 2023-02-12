arr = []
new_pwd = []
flag = 0

pwd = input()
N = int(input())

for i in range(0, N):
    arr.append(input())
    
while(True):
    # 문자 chr 바꾸기
    new_pwd = []
    for s in pwd:
        new_pwd.append(chr((ord(s) - ord('a') + 1) % 26 + ord('a')))
    pwd = new_pwd
    
    # 문자열 각각 확인
    for i in range(0, len(arr)):
        if arr[i] in ''.join(new_pwd):
            flag = 1
            break
    if flag == 1:
        break

print(''.join(new_pwd))