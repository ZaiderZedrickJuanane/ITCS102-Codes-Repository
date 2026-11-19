#dictionary and list

#dictionary functions
    # .append(value: ) -- add
    # .inset(index: , value: ) -- add in specific position
    # .pop() -- delete using index, default : last part
    # .remove -- delete using value

fruit_basket = [""] #empty list

fruit_basket = ["longgan","lipute","duhat","atis"]

#add
fruit_basket.append("banana")
fruit_basket.append("orang")
fruit_basket.append("grapes")
fruit_basket.append("mango")
fruit_basket.append("apple")

print(fruit_basket)



#add in specific indexes

fruit_basket.insert(2,"pineapple")



# delete by index
fruit_basket.pop(2) #deletes pineapple
print(fruit_basket)


#delete by value 
fruit_basket.remove('orang')
print(fruit_basket)


#list slicing
print(fruit_basket[2]) # prints specific values inside the list using index
# print(fruit_basket['duhat']) # prints specific values inside the list using the value itself

print(fruit_basket[0 : 4]) # prints a certain RANGE of values inside the list