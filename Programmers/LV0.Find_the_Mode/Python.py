def solution(array):
    answer = 0
    cur_max = 0
    flag = False
    
    #make dictionary to count
    count_dict = {}
    
    for x in array:
        if x in count_dict:
            count_dict[x] += 1
        else :
            count_dict[x] = 1
 
    #find a key with maximum value
    for cnt in count_dict.values():
        cur = cnt
        if cur > cur_max:
            cur_max = cur
            
    for key, value in count_dict.items():
        if (value == cur_max):
            if flag:
                return -1
            else:
                answer = key
                flag = True

    return answer