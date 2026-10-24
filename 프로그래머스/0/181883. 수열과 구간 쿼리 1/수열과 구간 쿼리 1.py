def solution(arr, queries):
    answer = [0] * len(arr)
    diff = [0] * (len(arr) + 1)
    
    # 차분 배열
    for s, e in queries:
        diff[s] += 1
        diff[e+1] -= 1
    
    print(diff)
    
    # 쿼리 처리
    answer[0] = diff[0] + arr[0]
    for i in range(1, len(arr)):
        diff[i] += diff[i-1]
        answer[i] = arr[i] + diff[i]
    
    
    return answer