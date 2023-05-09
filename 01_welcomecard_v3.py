"""welcomecard V3
Turns welcomecard_v2 into a function"""


def welcomecard():
    # Asks the User for their name
    name = input("What is your name? ")

    # Asks the user for their age
    age = input("What is your age? ")

    # Welcomes the user
    print(f"Welcome to the Maori Quiz {name}")

    while True:

        # Asks user if they have played before
        answer = input("Have you played before? ").lower()

        # If the user answers yes then the program continues
        if answer == "yes" or answer == "y":
            print("program continues")
            return name, age, answer

        # If the user answers no then the instructions will be shown
        elif answer == "no" or answer == "n":
            print("show instructions")
            return name, age, answer

        # If the user inputs anything else an error will be shown
        else:
            print("<ERROR> Please input Y/N")

# Main routine
welcomecard()
