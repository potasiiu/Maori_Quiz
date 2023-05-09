"""Instructions V1
This will be the instructions to the Quiz and will only be shown to the user
If they have chosen that they have not played before"""


# Asks if the user has played before
answer = input("Have you played before? ").lower()

if answer == "yes" or answer == "y":
    print("Program continues")

elif answer == "no" or answer == "n":
    print("instructions")

else:
    print("<Error> please answer the question properly")
