"""00_base_file_v1.py
This is the base file where all the components will be compiled into a program"""


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
    return name, age


def yes_no(question_text):
    while True:

        # Asks the user the yes or no questions
        answer = input(question_text).lower()

        # If they answer yes, output "Yes"
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they answer no, output "No"
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # If anything else is inputted, output <Error>
        else:
            print("<Error> Please input y/n")


def instructions(proceed_text):
    instructions_title = "How to play"
    print("*" * len(instructions_title))
    print(instructions_title)
    print("*" * len(instructions_title))
    # The instructions
    print("When the quiz begins, a question on the Maori Months will be shown.\n"
          "Then enter the answer to the question.\n"
          "There will be 10 questions\n"
          "Capitalization is very important. Remember that!\n"
          "If you get all of the questions right, you will get a prize!\n"
          "Good Luck.")
    # Asks the user to press the Enter Key to continue

    while True:
        proceed = input(proceed_text)
        if proceed != "":
            print("Invalid input. Please try again.")
        else:
            break


def maoriquiz():
    import random

    # The questions for the quiz
    questions = {"What is Kohi-tātea in English? ": "January",
                 "What is Hui-tanguru in English? ": "February",
                 "What is Poutū-te-rangi in English? ": "March",
                 "What is Paenga-whāwhā in English? ": "April",
                 "What is Haratua in English? ": "May",
                 "What is Pipiri in English? ": "June",
                 "What is Hōngongoi in English? ": "July",
                 "What is Here-turi-kōkā in English? ": "August",
                 "What is Mahuru in English? ": "September",
                 "What is Whiringa-ā-nuku in English? ": "October",
                 "What is Whiringa-ā-rangi in English? ": "November",
                 "What is Hakihea in English? ": "December"}

    # Points variable
    points = 0

    for i in range(10):
        question = random.choice(list(questions.keys()))
        answer = input(question)
        if answer.lower() == questions[question].lower():
            points += 1
            print("Correct!\n"
                  "You gained 1 point.\n"
                  f"You now have {points} points.")
        else:
            print(f"Nice try. The correct answer is {questions[question]}.\n"
                  f"You have {points} points.")
        del questions[question]

    # Rewards the player with a message showing how well they did
    if points == 10:
        print("Congratulations! You got every single answer correct\n"
              "You have achieved with Excellence")
    elif 7 <= points <= 9:
        print("Congratulations! You did very well\n"
              f"You got {points} out of 10!\n"
              "You have achieved with Merit\n"
              "You can try again for Excellence")
    elif 4 <= points <= 6:
        print("Good Job. You didn't do too bad\n"
              f"You got {points} out of 10\n"
              "You have passed\n"
              "You can try again for a better grade")
    else:
        print("Nice try. However, you did not get enough points to pass\n"
              f"You got {points} out of 10\n"
              "You did not pass.\n"
              "You can try again to pass")


# Main Routine
welcomecard()
question_ = yes_no("Have you played before (Y/N)? ")

if question_ == "No":
    instructions("Press <Enter> to continue")

maoriquiz()
play = ""
while play != "x":
    play_again = yes_no("Would you like to play again (Y/N)? ")

    if play_again == "Yes":
        maoriquiz()
    elif play_again == "No":
        print(f"Thanks for playing,\n"
              "Farewell")
        break
    else:
        print("Invalid input. Please input Y/N")
