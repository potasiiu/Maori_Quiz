"""04_questiongen_v1.py
This will be for generating the questions for the quiz"""
# RNG for question generation
import random

points = 0
questions = ["What is Kohi-tātea in English? ", "What is Hui-tanguru in English? ",
             "What is Poutū-te-rangi in English? ", "What is Paenga-whāwhā in English? ",
             "What is Haratua in English? ", "What is Pipiri in English? ", "What is Hōngongoi in English? ",
             "What is Here-turi-kōkā in English? ", "What is Mahuru in English? ",
             "What is Whiringa-ā-nuku in English? ", "What is Whiringa-ā-rangi in English? ",
             "What is Hakihea in English? "]

for item in range(10):
    picked_question = random.randint(0, 11)
    # Question for January
    if picked_question == 0:
        answer = input(questions[0])
        if answer == "January":
            points += 1  # Gives 1 point for a correct answer
            print("Correct!\n"  # If they get it correct they get this message and one point
                  "You gained 1 Point.\n"
                  f"You now have {points} points.")
        else:
            print("Nice try. The Correct answer is: January\n"  # If they get it wrong then this message will appear
                  f"You have {points} points.")
    # Question for February
    if picked_question == 1:
        answer = input(questions[1])
        if answer == "February":
            points += 1
            print("Correct!\n"
                  "You gained 1 Point.\n"
                  f"You now have {points} points.")
        else:
            print("Nice try. The Correct answer is: February\n"
                  f"You have {points} points.")
    # Question for March
    if picked_question == 2:
        answer = input(questions[2])
        if answer == "March":
            points += 1
            print("Correct!\n"
                  "You gained 1 Point.\n"
                  f"You now have {points} points.")
        else:
            print("Nice try. The Correct answer is: March\n"
                  f"You have {points} points.")
    # Question for April
    if picked_question == 3:
        answer = input(questions[3])
        if answer == "April":
            points += 1
            print("Correct!\n"
                  "You gained 1 Point.\n"
                  f"You now have {points} points.")
        else:
            print("Nice try. The Correct answer is: April\n"
                  f"You have {points} points.")
    # Question for May
    if picked_question == 4:
        answer = input(questions[4])
        if answer == "May":
            points += 1
            print("Correct!\n"
                  "You gained 1 Point.\n"
                  f"You now have {points} points.")
        else:
            print("Nice try. The Correct answer is: May\n"
                  f"You have {points} points.")
    # Question for June
    if picked_question == 5:
        answer = input(questions[5])
        if answer == "June":
            points += 1
            print("Correct!\n"
                  "You gained 1 Point.\n"
                  f"You now have {points} points.")
        else:
            print("Nice try. The Correct answer is: June\n"
                  f"You have {points} points.")
    # Question for July
    if picked_question == 6:
        answer = input(questions[6])
        if answer == "July":
            points += 1
            print("Correct!\n"
                  "You gained 1 Point.\n"
                  f"You now have {points} points.")
        else:
            print("Nice try. The Correct answer is: July\n"
                  f"You have {points} points.")
    # Questions for August
    if picked_question == 7:
        answer = input(questions[7])
        if answer == "August":
            points += 1
            print("Correct!\n"
                  "You gained 1 Point.\n"
                  f"You now have {points} points.")
        else:
            print("Nice try. The Correct answer is August\n"
                  f"You have {points} points.")
    # Question for September
    if picked_question == 8:
        answer = input(questions[8])
        if answer == "September":
            points += 1
            print("Correct!\n"
                  "You gained 1 Point.\n"
                  f"You now have {points} points.")
        else:
            print("Nice try. The Correct answer is September\n"
                  f"You have {points} points.")
    # Question for October
    if picked_question == 9:
        answer = input(questions[9])
        if answer == "October":
            points += 1
            print("Correct!\n"
                  "You gained 1 point.\n"
                  f"You now have {points} points.")
        else:
            print("Nice try. The Correct answer is October\n"
                  f"You have {points} points.")
    # Question for November
    if picked_question == 10:
        answer = input(questions[10])
        if answer == "November":
            points += 1
            print("Correct!\n"
                  "You gained 1 point.\n"
                  f"You now have {points} points.")
        else:
            print("Nice try. The Correct answer is November\n"
                  f"You have {points} points.")
    # Question for December
    if picked_question == 11:
        answer = input(questions[11])
        if answer == "December":
            points += 1
            print("Correct!\n"
                  "You gained 1 point.\n"
                  f"You now have {points} points.")
        else:
            print("Nice try. The Correct answer is December\n"
                  f"You have {points} points.")

# Main Routine
if points == 10:
    print("Congratulations! You got every single answer correct\n"
          "You have achieved with Excellence")
elif 7 <= points <= 9:
    print("Congratulations! You did very well\n"
          "You have achieved with Merit\n"
          "You can try again for Excellence")
elif 3 <= points <= 6:
    print("Good Job. You didn't do too bad\n"
          "You have passed\n"
          "You can try again for a better grade")
else:
    print("Nice try. However, you did not get enough points to achieve\n"
          "You did not pass.\n"
          "You can try again to pass")
