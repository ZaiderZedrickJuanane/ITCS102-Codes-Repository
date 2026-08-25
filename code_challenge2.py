money = 12008

print("You have this amount of money : ", money)

#calculations
thousand = money//1000
money = money - thousand*1000
fivehundy = money//500
money = money - fivehundy*500
twohundy = money//200
money = money - twohundy*200
onehundy = money//100
money = money-onehundy*100
fifty = money//50
money = money - fifty*50
twenty = money//20
money = money - twenty*20
ten= money//10
money = money - ten*10
five = money//5
money = money- five*5
one = money//1
money = money - one

#printing statement



print("you have ", thousand,"quantity of 1000")
print("you have ", fivehundy,"quantity of 500")
print("you have ", twohundy,"quantity of 200")
print("you have ", onehundy,"quantity of 100")
print("you have ", fifty,"quantity of 50")
print("you have ", twenty,"quantity of 20")
print("you have ", ten,"quantity of 10")
print("you have ", five,"quantity of 5")
print("you have ", one,"quantity of 1")

