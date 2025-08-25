def solution(num_list):
    answer = 0
    
    for x in num_list :
        counter = 0
        temp = x
        
        while temp > 1 :
            temp = temp // 2
            counter += 1

        answer += counter
        
    return answer