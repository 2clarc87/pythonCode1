import math
while True:
    choice = int(input("\n\nWhat do you want to do:\n1)Name\n2)Health\n3)Robot Game\n4)Age Check\n5)Count\n6)Game\n"))
    if choice == 1:
        name = input("What is your name:")
        lastName = input("What is your last name:")
        print(f"Hello {name} {lastName}")
    elif choice == 2:
        health = "♥" * int(input("Number of lives:"))
        energy = "♦" * int(input("Amount of energy:"))
        shield = "♦" *int(input("Amount of shield:"))
        print(f"Health:{health}")
        print(f"Health:{energy}")
        print(f"Health:{shield}")
    elif choice == 3:
        eyes = input("What do you want the eyes to be:")
        mouth = input("what do you want the mouth to be:")
        print(f"##########\n#  {eyes}  {eyes}  #\n#  {mouth*4}  #\n##########")
    elif choice == 4:
        age = int(input("How old are you:"))
        if age >= 18:
            print("You are an Adult.")
        else:
            print("You are a child.")
    elif choice == 5:
        number = int(input("What do you want to count to:"))
        for i in range(number-1):
            print(i+1, end=", ")
        print(i+2)
    elif choice == 6 or choice == 7:
        array = [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]
        while True:
            for j in range(3):
                print("")
                for i in range(3):
                    print(array[i][2-j], end="")
            print("\n")
            enter = int(input("Enter what you what to change:"))
            if enter == 0:
                break
            elif enter <= 3:
                y = 0
            elif enter <= 6:
                y = 1
            else:
                y = 2
            x = (enter % 3)-1
            if array[x][y] == "X":
                array[x][y] = " "
            else:
                array[x][y] = "X"
    else:
        break
