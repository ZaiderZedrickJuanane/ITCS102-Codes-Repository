#functions

# reusable and customizable
# 

def triangle(n):
    for x in range(n):
        for y in range(n+1,0,-1):
            print('*',end=" ")

        print()

print(triangle(6))

def box(b1):
    for x in range(b1):
        for y in range(b1):
            if x == 0 or x == b1-1 or y == 0 or y == b1-1:
                
                print(y,end=" ")

            else :
                print(" ",end=" ")
        
        print()
        



def fact(n):
    fact = 1
    for x in range (n,0,-1):
        fact *= x
    return fact



# def sum(n1,n2):
#     return n1 + n2


# def minus (s1,s2):
#     return s1 - s2




# print(sum(5,7))

# print(minus(9,3))