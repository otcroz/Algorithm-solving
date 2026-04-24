def solution(numbers, target):
    answer = 0
    
    def func(n, cur):
        if n == len(numbers):
            if target == cur:
                return 1
            else:
                return 0
        return func(n+1, cur-numbers[n]) + func(n+1, cur+numbers[n])
    
    answer = func(0, 0)
    return answer