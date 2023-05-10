"""02_yesnofunction_v1.py
This will be a function for asking yes or no questions, and will be used for asking if the user has played before
This function will be able to be used with any yes or no questions"""


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


# Main Routine
question = yes_no("Have you played before? ")
if question == "No":
    print("Instructions")

        
