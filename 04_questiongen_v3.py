"""04_questiongen_v3.py
Edited code that uses a dictionary and a loop to iterate through the questions.
Uses string formatting to simply code and avoid repetition"""


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
maoriquiz()
