"""The Welcome Card V1
The welcome card is to welcome the user to the program
It will be formatted in a way that will be appealing to the user"""

welcome = "Welcome to the Maori Month Quiz"
top_bottom = "*" * len(welcome)  # For formatting the welcome statement
print(f"{top_bottom}\n"
      f"{welcome}\n"
      f"{top_bottom}")
print()
name = input("What is your name? ")  # Ask for the user's name
print(f"{top_bottom}")
age = int(input("What is your age? "))  # Ask for the user's age
print()
print(f"Welcome {name} ({age}) to the Maori Quiz")
