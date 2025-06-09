N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [False] * (N+1)

min_ability = float('inf')

def sum_teams_ability(team):
    sum_ability = 0

    for i in team:
        for j in team:
            sum_ability += arr[i-1][j-1]

    return sum_ability

def back(depth, idx):
    global min_ability
    if depth == N // 2:
        a_team = [i for i in range(1, N+1) if v[i]]
        b_team = [i for i in range(1, N+1) if not v[i]]

        a_sum = sum_teams_ability(a_team)
        b_sum = sum_teams_ability(b_team)

        sub = abs(a_sum - b_sum)
        min_ability = min(min_ability, sub)

        if min_ability == 0:
            print(0)
            exit(0)
        return
    
    for p in range(idx, N+1):
        v[p] = True
        back(depth + 1, p + 1)
        v[p] = False

back(0, 1)
print(min_ability)