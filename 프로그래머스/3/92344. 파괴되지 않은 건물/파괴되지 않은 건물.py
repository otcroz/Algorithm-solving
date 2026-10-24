def solution(board, skill):
    n, m = len(board), len(board[0])
    answer = [[0]*m for _ in range(n)]
    diff = [[0]*(m+1) for _ in range(n+1)]
    
    answer[0][0] = board[0][0] + diff[0][0]
    
    # 2차원 차분 배열
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            value = -degree
        else:
            value = degree
        
        diff[r1][c1] += value
        diff[r1][c2+1] -= value
        diff[r2 + 1][c1] -= value
        diff[r2 + 1][c2 + 1] += value
    
    # 가로 누적합 계산
    for i in range(n):
        for j in range(1, m):
            diff[i][j] += diff[i][j-1]
    # 세로 누적합 계산
    for j in range(m):
        for i in range(1, n):
            diff[i][j] += diff[i-1][j]
            
    # 파괴되지 않은 값 찾기
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + diff[i][j] > 0:
                cnt +=1
    
    return cnt