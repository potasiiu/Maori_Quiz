"""04_questiongen_v2.py
Edited code that uses a dictionary and a loop to iterate through the questions.
Uses string formatting to simply code and avoid repetition"""
# RNG for question generation
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
