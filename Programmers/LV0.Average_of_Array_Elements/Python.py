def solution(numbers):
    answer = 0
    temp = 0
    for x in numbers:
        temp += x
        
    answer = temp / len(numbers)
    return answer