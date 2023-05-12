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
    picked_question = random.randint(0,11)
    # Question for January
    if picked_question == 0:
        answer = input(questions[0])
        if answer == "January":
            print("Correct!\n" # If they get it correct they get this message and one point
                  "You gained 1 Point.\n"
                  f"You now have {points}.")
            points += 1
        else:
            print("Nice try. The Correct answer is: January\n" # If they get it wrong then this message will appear
                  f"You have {points}")
    questions.remove(questions[0]) # This removes the item from the list so there won't be duplicate items
    # Question for February
    if picked_question == 1:
        answer = input(questions[1])
        if answer == "February":
            print("Correct!\n"
                  "You gained 1 Point.\n"
                  f"You now have {points}.")
            points += 1
        else:
            print("Nice try. The Correct answer is: February\n"
                  f"You have {points}")
    questions.remove(questions[1])
    # Question for March
    if picked_question == 2:
        answer = input(questions[2])
        if answer == "March":
            print("Correct!\n"
                  "You gained 1 Point.\n"
                  f"You now have {points}.")
            points += 1
        else:
            print("Nice try. The Correct answer is: March\n"
                  f"You have {points}")
    questions.remove(questions[2])
    # Question for April
    if picked_question == 3:
        answer = input(questions[3])
        if answer == "April":
            print("Correct!\n"
                  "You gained 1 Point.\n"
                  f"You now have {points}.")
            points += 1
        else:
            print("Nice try. The Correct answer is: April\n"
                  f"You have {points}")
    questions.remove(questions[3])
    # Question for May
    if picked_question == 4:
        answer = input(questions[4])
        if answer == "May":
            print("Correct!\n"
                  "You gained 1 Point.\n"
                  f"You now have {points}.")
            points += 1
        else:
            print("Nice try. The Correct answer is: May\n"
                  f"You have {points}")
    questions.remove(questions[4])
    # Question for June
    if picked_question == 5:
        answer = input(questions[5])
        if answer == "June":
            print("Correct!\n"
                  "You gained 1 Point.\n"
                  f"You now have {points}.")
            points += 1
        else:
            print("Nice try. The Correct answer is: June\n"
                  f"You have {points}")
    questions.remove(questions[5])
    # Question for July
    if picked_question == 6:
        answer = input(questions[6])
        if answer == "July":
            print("Correct!\n"
                  "You gained 1 Point.\n"
                  f"You now have {points}.")
            points += 1
        else:
            print("Nice try. The Correct answer is: July\n"
                  f"You have {points}")
    questions.remove(questions[6])
    # Questions for August

