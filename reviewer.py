#inputs
age = int(input("Age ---> "))
rev = float(input("Revenue ---> "))
cc = int(input("credit score ---> "))
yrs = float(input("years of business ---> "))
has_defaults = bool(eval(input("filed bankruptcy? ---> ")))
collateral = input("collateral name ---> ")
c_value = float(input("collateral value ---> "))


#changing values
max_loan = 0.0
base_fee = 0.0


#baseline

if age >= 21 and yrs >= 2.0 and has_defaults == False :
    print("Baseline passed")
    if cc >= 720 : #tier1
        max_loan = rev * 3 #maximum value set
        print("Maximum loanable amount is set to", max_loan)
        print("High credit score")

        if rev >= 50000 : #if revenue is equals to or higher than 50k
            print("revenue higher than 50k")
            base_fee = max_loan * 0.015 
            print("base fee is set to", base_fee)

        else : # if revenue is lower than 50k
            print("revenue lower than 50k")
            base_fee = max_loan * 0.025 
            print("base fee is set to", base_fee)

        #collateral
        if collateral >= max_loan : 
            print("Accepted since collateral value is higher than max loan")

        else :
            print("Rejected : Insufficient collateral value for ", collateral)

        #surcharge
        if collateral % 5000 != 0 :
            base_fee += 250
            print("Additioal fee is added")



    elif cc >= 620 and cc < 720 : #Tier 2
        max_loan = rev * 1.5

        if yrs >= 5.0 : #If business is operating more than 5 years
            base_fee = max_loan * 0.02
            print("Business is operating in more than or equal to 5 years")
        else : # If business is operating less than 5 years
            base_fee = max_loan * 0.035
            print("Business is operating in less than 5 years")

          #collateral
            if collateral >= max_loan : 
                print("Accepted since collateral value is higher than max loan")
    
            else :
                print("Rejected : Insufficient collateral value for ", collateral)
    
            #surcharge
            if collateral % 5000 != 0 :
                base_fee += 250
                print("Additioal fee is added")
    elif cc < 620 : #Tier 3
        print("REJECTED : CREDIT SCORE TOO LOW")

    elif cc > 1000 and cc < 1 :
        print("INVALID")

else : 
    print("Did not meet the baseline")