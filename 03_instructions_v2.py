"""03_instructions_v2.py
Turns v1 into a function"""


# The Function
def instructions(proceed_text):
    instructions_title = "How to play"
    print("*" * len(instructions_title))
    print(instructions_title)
    print("*" * len(instructions_title))
    # The instructions
    print("When the quiz begins, a question on the Maori Months will be shown.\n"
          "Then enter the answer to the question.\n"
          "If you get all of the questions right, you will get a prize!\n"
          "Good Luck.")
    # Asks the user to press the Enter Key to continue

    while True:
        proceed = input(proceed_text)
        if proceed != "":
            print("Invalid input. Please try again.")
        else:
            break


# Main Routine
instructions("Press <Enter> to continue")
