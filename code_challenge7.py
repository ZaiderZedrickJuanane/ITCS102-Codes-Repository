size = int(input("Input size > "))

center = size//2

if center % 2 == 0 :
    size += 1





for x in range(size) :
    for y in range(size):
        distance = abs(x- center) + abs (y - center)
        if distance <= center and distance % 2 == center % 2 :
            print("*",end=" ")
        else :
            print(" ",end=" ")

    print()
    

