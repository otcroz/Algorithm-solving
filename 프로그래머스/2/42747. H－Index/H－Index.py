def solution(citations):
    
    citations.sort(reverse=True)
    
    for i, cite in enumerate(citations):
        if i+1 > cite:
            return i
    
    return len(citations)