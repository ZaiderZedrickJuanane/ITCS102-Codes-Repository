
n = int(input("Input your number : "))


for i in range(n):
    for k in range (n):
        if i + k == n-1 or k == n-1:
            print("*",end="   ")
        else:
            print(" ",end="   ")
    print()

for i in range(n):
    for k in range (n):
        if i + k == n-1 or k == 0:
            print("*",end="   ")
        else:
            print(" ",end="   ")
    print()

# for i in range(1,c+1): #For Upper
#     for k in range(1,r+1):
#         if (i <=5 and (i + k == 6 or k == 5)) or (i >= 6 and (i + k == 10 or  k ==1)):
#             print("*",end="  ")

#         else:
#             print(" ",end="  ")

#     print()





# for i in range(1,r+1): #For Upper
#     for k in range(1,r+1):
#         if i + k == 6 or k == 5:
#             print("*",end=" ")

#         else:
#             print(" ",end=" ")

#     print()


# for i in range(1,r): #For lower
#     for k in range(1,r):
#         if i + k == 5 or k == 1:
#             print("*",end=" ")

#         else:
#             print(" ",end=" ")

#     print()