sum = 0

t= True
while t == True :
    number = int(input("Type the number you want to add : "))

    if number == 0 :
        print("Your total summary is : ", sum)
        break
        

    else:
        sum += number
        print("Total sum so far : ", sum)
        continue
