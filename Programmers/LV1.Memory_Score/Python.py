def solution(name, yearning, photo):
    answer = []
    
    for foto in photo : #search every photo
        arr = []
        for ppl in foto :
            if ppl in name : #check if the person on the list
                arr.append(name.index(ppl))
        temp = 0
        for i in arr : #sum up all the points

            temp += yearning[i]
        answer.append(temp)
    
    return answer
