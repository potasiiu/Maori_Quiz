"""The Welcome Card V1
After obtaining the user details the user will then be asked
if they have played through the quiz before"""


name = input("What is your name? ")  # Ask for the user's name
print()
age = int(input("What is your age? "))  # Ask for the user's age
print()
welcome = f"Welcome to the Maori Month Quiz {name} ({age}"
top_bottom = "*" * len(welcome)  # For formatting the welcome statement
print()
print(f"{top_bottom}\n"
      f"{welcome}\n"
      f"{top_bottom}")
