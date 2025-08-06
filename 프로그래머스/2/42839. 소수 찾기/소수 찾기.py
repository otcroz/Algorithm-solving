from itertools import permutations
def solution(numbers):
    answer = 0
    
    num_arr = list(numbers)
    #print(num_arr)
    
    num_arr.sort() # 오름차순 sort
    prime = [] # 소수 저장
    for i in range(1, len(numbers)+1):
        arr = permutations(num_arr,i)
        arr = [''.join(map(str,i)) for i in arr] # 각 튜플 요소들 합치기
        arr = list(set(arr)) # 중복 없애기
        
        # 순열로 만들어진 숫자들이 소수인지 확인
        
        for item in arr:
            res = is_prime(int(item))
            if res != 0:
                prime.append(res)
    prime = list(set(prime)) # 중복되는 숫자 없애기
    answer += len(prime)
    
    return answer
    
def is_prime(num):
    if num <= 1:
        return 0
    for i in range(2, num):
        if num % i == 0:
            return 0
    return num