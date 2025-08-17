def solution1(s):
    answer = ''
    counter = 0
    
    for x in s : 
        if x == ' ':
            counter = 0
            answer = answer + " "

        elif counter % 2 == 0 :
            answer = answer + x.upper()
            counter += 1
            
        else : 
           answer = answer + x.lower() 
           counter += 1
        
    return answer

def solution2(s):
    result = []
    counter = 0
    
    for ch in s :
        if ch == ' ':
            counter = 0
            result.append(' ')
            continue

        elif counter % 2 == 0 :
            result.append(ch.upper())
            
        else : 
            result.append(ch.lower())
           
        counter += 1
        
    return ''.join(result)