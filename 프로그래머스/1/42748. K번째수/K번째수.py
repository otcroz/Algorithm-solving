def solution(array, commands):
    answer = []
    print(array)
    for command in commands:
        start = command[0]
        end = command[1]
        idx = command[2]
        # 1. 자르기
        new_arr = array[start-1:end]
        # 2. 정렬 후 특정 index pop
        new_arr.sort()
        item = new_arr.pop(idx-1)
        answer.append(item)
        
    return answer