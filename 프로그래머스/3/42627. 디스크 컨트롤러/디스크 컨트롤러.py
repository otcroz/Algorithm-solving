import heapq

def solution(jobs):
    return_time = [0]*len(jobs) # 각 큐의 반환 시간
    arr = [] # 작업
    wait = [] # 대기 큐
    
    
    # 대기 큐: 번호, 요청 시각, 소요 시간 / 소요 적 > 요청 빠 > 번호 적
    for i, job in enumerate(jobs):
        heapq.heappush(arr, (job[0], job[1], i))
    
    t = 0 # 현재 시간
    while arr or wait:
        while arr and arr[0][0] <= t:
            req_time, work_time, n = heapq.heappop(arr)
            heapq.heappush(wait, (work_time, req_time, n))
            
        if wait: # 대기큐 존재
            work_time, req_time, n = heapq.heappop(wait)
            t += work_time
            return_time[n] = t - req_time # 반환 시간
        else: # 도착한 작업이 없는 경우
            t = arr[0][0]
    
    return sum(return_time) // len(jobs)