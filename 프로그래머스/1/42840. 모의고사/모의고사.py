def solution(answers):
    answer = []
    
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    correct_answer = [0, 0, 0] # 1,2,3 수포자의 정답 기록
    length = len(answers) # 문제의 길이  

    # 각 배열을 문제 수와 맞추기
    if length < len(one):
        one = one[:length]
    else:
        one = one * ((length // len(one))+1)
    if length < len(two):
        two = two[:length]
    else:
        two = two * ((length // len(two))+1)
    if length < len(three):
        three = three[:length]
    else:
        three = three * ((length // len(three))+1)
        
    #print(one, two, three)
    
    # 문제를 맞췄는지 각각 확인
    for i in range(length):
        if answers[i] == one[i]:
            correct_answer[0] += 1
        if answers[i] == two[i]:
            correct_answer[1] += 1
        if answers[i] == three[i]:
            correct_answer[2] += 1                
    #print(correct_answer)
    answer = [i+1 for i in range(3) if correct_answer[i] == max(correct_answer)]
    answer.sort()

    return answer