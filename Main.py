while(True):
    choice = int(input("\n\nWhat do you want to do:\n1)Name\n2)Health\n3)Robot Game\n"))
    if choice == 1:
        name = input("What is your name:")
        lastName = input("What is your last name:")
        print(f"Hello {name} {lastName}")
    elif choice == 2:
        health = "♥" * int(input("Number of lives:"))
        energy = "♦" * int(input("Number of lives:"))
        shield = "♦" *int(input("Number of lives:"))
        print(f"Health:{health}")
        print(f"Health:{energy}")
        print(f"Health:{shield}")
    elif choice == 3:
        eyes = input("What do you want the eyes to be:")
        mouth = input("what do you want the mouth to be:")
        print(f"##########\n#  {eyes}  {eyes}  #\n#  {mouth*4}  #\n##########")

    else:
        break
