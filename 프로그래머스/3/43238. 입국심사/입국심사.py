def solution(n, times):
    answer = 0
    
    left = 1
    right = max(times) * n # 처리할 최대 시간
    answer = right
    
    while left <= right:
        mid = (left + right) // 2 # 평균적으로 처리할 사람 수
        
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break
                
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer