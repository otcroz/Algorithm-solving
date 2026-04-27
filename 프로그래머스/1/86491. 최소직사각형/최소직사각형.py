def solution(sizes):
    answer = 0
    
    w, h = [], []
    for size in sizes:
        w.append(max(size))
        h.append(min(size))
    
    answer = max(w) * max(h)
    
    return answer