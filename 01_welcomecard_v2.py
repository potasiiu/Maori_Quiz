"""The Welcome Card V1
After obtaining the user details the user will then be asked
if they have played through the quiz before"""

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
print(f"Welcome {name} to the Maori Quiz")
print()
# Asks the user if they have played before
played_before = input("Have you played the game before? ").lower()
if played_before == "yes" or played_before == "y":
    print("continue")
elif played_before == "no" or played_before == "y":
    print("shows instructions")
else:
    print("<ERROR> Please input Y/N")
