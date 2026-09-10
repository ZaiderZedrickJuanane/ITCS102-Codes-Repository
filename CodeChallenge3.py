Sender_Name = input("Name of Sender? --> ")
Type_of_Item = input("Type of Item? ---> ")
Is_Fragile = bool(eval(input("Is Fragile? (True or False) ---> ")))
weight = float(input("Weight of the object? (in kg) ---> "))
distance = float(input("distance (In km) ---- > "))
is_express = bool(eval(input("Express? (True or False) --> ")))
is_international = bool(eval(input("International? (True or False ) --> ")))



# Calculating base cost

base_cost = (weight * 2.5) + (distance * .15)

#Free shipping


if  weight <= 2 and distance <= 100 and is_express == False and is_international == False :
	print("Free Shipping!!")
	Total = 0
	

#International Express

elif is_international == True and is_express == True :
	print("Package is International is applied")
	Total = (base_cost * 1.4) + 50

#Express or Heavy International

elif is_express == True or (is_international == True and weight > 20) : 
	print("Package is Express or Heavy International is applied")
	Total = (base_cost * 1.2) + 25

#Oversized
elif weight > 30 or distance > 1000 : 
	print("Oversized is applied")
	Total = base_cost + 30
#Standard rate

else :
	Total = base_cost
	print("Standard rate is applied")


print("--------------------------")
print("Name of the sender : ", Sender_Name)
print("Type of Item : ", Type_of_Item )
print("Total Output  : PHP ", Total)
