def solution(brown, yellow):
    answer = []
    
    sum_color = brown + yellow
    i = 1
    while True:
        y_h = i
        y_w = yellow // y_h
        if sum_color == 2*y_w + 2*y_h + y_w*y_h + 4 and y_w*y_h == yellow:
            break
        i+=1
        
    
    answer = [y_w+2,y_h+2]
    print(answer)
    
    return answer