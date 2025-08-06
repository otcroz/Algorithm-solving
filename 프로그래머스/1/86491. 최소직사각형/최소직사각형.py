
def solution(sizes):
    answer = 0
    
    width, height = [], []
    for item in sizes:
        width.append(max(item))
        height.append(min(item))
        
    max_w = max(width)
    max_h = max(height)
    answer = max_w*max_h
    
    
    return answer

