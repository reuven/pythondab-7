""" The most amazing first description I have written in a module!

See how much I've learnt already

Amazing!!
"""


def menu(*foods):
    foods = [food.lower() for food in foods]
    while True:
        print(f"Menu: {', '.join(foods)}")
        user_choice = input("Choose one: ").strip().lower()
        if user_choice in foods:
            return user_choice
        print("Not available today! Try something else...")


# 2. modify ur module such that running it from cmd line asks the user for input....

# if __name__ == "__main__":
#     print("Executing the module as a script")
#     user_choice = menu("ABACHA", "rice", "Fish")
#     print("You chose:", user_choice)


# 3. Modify your module so that running it from the command line uses sys.argv to get any command-line arguments, and pass those to the menu()
if __name__ == "__main__":
    import sys
    print("sys.argv:", sys.argv)

    if len(sys.argv) < 2:
        print("Please provide some foods as command-line arguments.")
    else:
        user_choice = menu(*sys.argv[1:])
        print(f"\nYou chose: {user_choice}")

