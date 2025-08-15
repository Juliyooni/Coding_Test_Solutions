n = int(input())
counter = 0

for x in range (n):
    counter += 1
    for y in range (counter):
        print('*', end = "")
    print()
