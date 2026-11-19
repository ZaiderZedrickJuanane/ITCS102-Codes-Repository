shonen = []
korean = []
isekai = []
adventure = []
fantasy = []

while True:
    ans = input('Do you watch or read any anime --? [yes / no] ').lower()

    if ans == "yes" :
        print('What kind of anime do you watch or read?? ')
        print('1 - shonen\n2 - korean\n3 - isekai\n4 - adventure\n5 - fantasy ')

        choice = int(input("Input -- >"))

        if choice == 1:
            print("SHONEN")
            title = input("Please type the title of the anime here -- > ")
            shonen.append(title)

            print("List of Shonen")
            print(shonen)

        elif choice == 2:
            print("Korean")
            title = input("Please type the title of the anime here -- > ")
            korean.append(title)

            print("List of korean")
            print(korean)
        elif choice == 3:
            print("isekai")
            title = input("Please type the title of the anime here -- > ")
            isekai.append(title)

            print("List of Isekai")
            print(isekai)
        elif choice == 4:
            print("adventure")
            title = input("Please type the title of the anime here -- > ")
            adventure.append(title)

            print("List of Adventure")
            print(adventure)
        elif choice == 5:
            print("Fantasy")
            title = input("Please type the title of the anime here -- > ")
            fantasy.append(title)

            print("List of Fantasy")
            print(fantasy)



        con = input('do you wish to continue, [yes / no] ').lower()
        
        if con == 'yes':
            continue

        else:
            print('goodbye')
            break

    else : 
        print('Invalid Answer')
        break
