def solution(numbers):
    answer = ''
    
    str_num = list(map(str, numbers))
    str_num.sort(key=lambda x: x*3, reverse=True)
    
    if str_num[0] == "0":
        answer = "0"
    else:
        answer= ''.join(map(str,str_num))
    return answer