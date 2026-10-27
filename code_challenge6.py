sample = int(input("Insert your number > "))
number = 1

for x in range(sample):
    for y in range(x+1):

        print(number,end=" ")
        number += 1

    print()