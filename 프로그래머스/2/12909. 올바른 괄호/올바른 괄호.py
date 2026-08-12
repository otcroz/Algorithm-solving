def solution(s):
    stack = []
    if s[0] == ')':
            return False
        
    for one in s:
        if len(stack) == 0 and one == ')':
            return False
        if one == '(':
            stack.append(one)
        elif one == ')':
            stack.pop()
    
    if len(stack) == 0:
        return True
    else:
        return False
    
   