N = int(input())

s = [0] * N
cnt = 0
def attack(row): # 말을 놓아도 되는지 판단
    for before in range(row):
        if s[before] == s[row] or abs(s[row] - s[before]) == abs(row - before):
            return False
    return True

def backtrack(row):
    global cnt
    if row == N:
        cnt += 1
        return
    for i in range(N):
        s[row] = i
        if attack(row):
            backtrack(row+1)

backtrack(0)
print(cnt)