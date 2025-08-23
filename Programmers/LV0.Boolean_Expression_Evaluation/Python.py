def solution(x1, x2, x3, x4):
    answer = False
    a = False
    b = False
    
    if x1 or x2 :
        a = True
    
    if x3 or x4 :
        b = True
        
    if a and b : 
        answer = True
        
    return answer