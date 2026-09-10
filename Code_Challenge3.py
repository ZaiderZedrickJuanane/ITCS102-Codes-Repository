#Sender_Name = input("Name of Sender? -- ")
#Type_of_Item = input("Type of Item? ==")
Is_Fragile = bool(input("Is Fragile? "))
weight = float(input("Weight of the object? () "))
distance = float(input("distance (In km)? "))
Is_Express = bool(input("Is rush? "))
Is_International = bool(input("Is international? "))




# Calculating base cost

base_cost = (weight * 2.5) + (distance * .15)

#Free shipping


if  weight <= 2 and distance <= 100 and Is_Express == False and Is_International == False :
	Total = base_cost



#International Express

elif Is_International == True and Is_Express == True :
	print("Package is International")
	Total = (base_cost * 1.4) + 50

#Express or Heavy International

elif Is_Express == True or (Is_international == True and weight < 20) : 
	print("Package is Express or Heavy International")
	Total = (base_cost * 1.2) + 25

#Oversized
elif weight > 30 or distance > 1000 : 
	print("Oversized")
	Total = base_cost + 30
#Standard rate

else :
	Total = base_cost

print(Total)