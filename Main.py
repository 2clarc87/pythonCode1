while(True):
    choice = int(input("What do you want to do:\n1)Name\n2)Health\n"))
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
    else:
        break
