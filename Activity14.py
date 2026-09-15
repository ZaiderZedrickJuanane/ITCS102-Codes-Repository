age = int(input("Age ---> "))
Is_employed = bool(eval(input("Are you Employed (True or False) --> ")))
credit_score = int(input("What is your credit score --> "))
annual_income = int(input("What is your annual income --> "))
has_collateral = bool(eval(input("Has collateral (True or False) ---> ")))
collateral = input("What is your collateral? --->")
baseline_interest_rate = 0

# pass : Let the code run without putting any code in
# used if you don't have any code to run


#Baseline
if age >= 21 and age <= 65 and Is_employed == True : 
    
    if credit_score >= 750 : #Tier 1: High Credit 
        if annual_income >= 100000 :
            print("Loyalty discount. Baseline Interest Rate : 4.5%")
        
        else :
            print("Baseline Interest Rate : 5%")

    elif credit_score >= 600 and credit_score <750 : #Tier 2: Fair Credit
        if has_collateral == True :
            print("Baseline Interest Rate : 7%")
        elif annual_income < 40000 :
            print("Baseline Interest Rate : 9.5%")
    else : #Tier 3: Low Credit 
        print("Rejected : Credit Score too Low")
else :
    print("Rejected: Fails baseline criteria ")