# My original solution - /Use counter; if at any point ')' exceeds '(', return False
def solution1(s):
    counter = 0
    
    if s[0] == ")" :
        return False
    
    if s[-1] == "(":
        return False
        
    for x in range (len(s)) : 
        if s[x] == "(" :
            counter += 1
        elif s[x] == ")" :
            counter -= 1
        if counter < 0 :
            return False
    
    if counter == 0 :
        return True
    
    else :
        return False
    
    # Using stack
    def solution2(s):
        stack = []
    
        for i in s : 
            if i == "(" :
                stack.append(i)
            elif i == ")" :
                if not stack :
                    return False
                stack.pop()
        
        if not stack :
            return True
    
        else :
            return False