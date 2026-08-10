def solution(array, commands):
    answer = []
    
    for command in commands:
        s = command[0]
        e = command[1]
        idx = command[2]
        
        arr = array[s-1:e]
        arr.sort()
        answer.append(arr[idx-1])
    
    return answer