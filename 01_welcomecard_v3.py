"""welcomecard V3
Turns welcomecard_v2 into a function"""


def welcomecard():
    # Asks the User for their name
    name = input("What is your name? ")

    # Asks the user for their age
    age = input("What is your age? ")

    # Welcomes the user
    welcome = f"Welcome to the Maori Quiz {name} ({age})"
    top_bottom = "*" * len(welcome)
    print(top_bottom)
    print(welcome)
    print(top_bottom)


# Main routine
welcomecard()
