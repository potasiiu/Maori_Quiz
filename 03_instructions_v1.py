"""03_instructions_v1.py
This is the component for the instructions
for teaching the user how this program works"""

# The instructions for the quiz
print("When the quiz begins, a question on the Maori Months will be shown.\n"
      "Then enter the answer to the question.\n"
      "If you get all of the questions right, you will get a prize!\n"
      "Good Luck.")
loop = ""
while loop != "x":
    Continue = input("Press <Enter> to continue")
    if Continue == "":
        print("program continues")
        loop = "x"
    else:
        print("Invalid input. Please Try Again")
