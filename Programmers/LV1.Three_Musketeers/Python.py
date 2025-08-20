#My original solution
def solution1(number):
    counter = 0
    
    for x in range (len(number) - 2) :
        for y in range (len(number) - x - 2) :
            for z in range (len(number) - (x + y + 1) - 1) :
                if number[x] + number[x + y + 1] + number[x + y + z + 2] == 0 :
                    counter += 1
    
    return counter

#Simplified version of solution1
def solution2(number):
    counter = 0
    n = len(number)
    
    for x in range(n - 2) :
        for y in range(x+1, n-1) :
            for z in range(y+1, n) :
                if number[x] + number[y] + number[z] == 0 :
                    counter += 1
    
    return counter