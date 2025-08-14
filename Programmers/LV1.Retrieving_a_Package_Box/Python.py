def solution(n, w, num):
    answer = 0
    row = 0
    col = 0
    my_dict = {}
    flag = -1
    
    for x in range(n) :
       my_dict[x+1] = [row, col]
    
    for x in range(n) :
        if x % w == 0:
            row += 1
            flag *= -1
        
        else :
            col = col + flag
        
        my_dict[x+1][0] = row
        my_dict[x+1][1] = col
    
    temp = 0
    
    if [row, my_dict.get(num)[1]] in my_dict.values() :    
        temp = row
    else :
        temp = row - 1
    
    answer = temp + 1 - my_dict.get(num)[0]   
    
    return answer