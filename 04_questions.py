import math
import random


def int_check(question, low=None, high=None, exit_code=None):
    # If any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = f"Please enter an integer that is more than / equal to {low}"

    # if the number needs to be between low and high
    else:
        error = f"Please enter an integer that is between {low} and {high}"

    while True:
        response = input(question).lower()

        # check for infinite mode
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if the response is valid, return it
            else:
                return response

        except ValueError:
            print(error)


# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # check use response, question
        # repeats if users say yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instructions():
    print('''
**** Instructions ****

To begin, choose the number of questions you want to attempt 

Pick your level of difficulty between level's 1-3, 1 being the easiest, 2 being medium, 3 being hardest.

Your questions will vary from Addition, Subtraction, Multiplication, Division

Then choose how many questions you'd like to attempt. 

Press <enter> for  infinite mode.

Your goal is to answer your questions correctly within your attempts

Good luck!!

    ''')


# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting the game

# Initialise game variables
mode = "regular"
num_questions = 0
history = []


print()
print("➕➖ Welcome to Basic Facts Quiz✖️➗")
print()

want_instructions = yes_no("Do you want to read the instructions?")

if want_instructions == "yes":
    instructions()

# Ask user for number of questions/ infinite mode
question_attempt = int_check("How Many Questions would you like to attempt? (Push <enter> for infinite mode): ",
                             low=1, exit_code="")

if question_attempt == "":
    mode = "infinite"
    question_attempt = 5

# Choose difficulty level
print()
difficulty = int_check("Choose your difficulty Level (level 1 being easy, Level 2 being medium, Level 3 being "
                       "hard): ",
                       low=1, high=3)
# question loop starts here
while num_questions < question_attempt:

    # Quiz headings
    if mode == "infinite":
        quiz_heading = f"\n Question  {num_questions + 1 } (Infinite mode) "
    else:
        quiz_heading = f"\n ✨✨✨Question {num_questions + 1} of {question_attempt}✨✨✨"

    print(quiz_heading)
    math_list = ["addition", "subtraction", "multiplication", "division"]

    # generates number's difficulty for the question
    if difficulty == "3":
        num_1 = random.randint(1, 40)
        num_2 = random.randint(1, 40)
    elif difficulty == "2":
        num_1 = random.randint(1, 30)
        num_2 = random.randint(1, 30)
    else:
        num_1 = random.randint(1, 15)
        num_2 = random.randint(1, 15)

    question_type = random.choice(math_list)
    user_choice = ""

    # generates the questions
    if question_type == "addition":
        user_choice = int_check(f"What is {num_1} + {num_2}? ")
        answer = num_1 + num_2

        if user_choice != answer:
            feedback = "incorrect"
        else:
            feedback = "correct"

        print(feedback)
    elif question_type == "subtraction":
        user_choice = int_check(f"What is {num_1} - {num_2}? ")
        answer = num_1 - num_2

        if user_choice != answer:
            feedback = "incorrect"
        else:
            feedback = "correct"

        print(feedback)
    elif question_type == "multiplication":
        user_choice = int_check(f"What is {num_1} x {num_2}? ")
        answer = num_1 * num_2

        if user_choice != answer:
            feedback = "incorrect"
        else:
            feedback = "correct"

        print(feedback)
    else:
        user_choice = int_check(f"What is {num_1} / {num_2}? ")
        answer = num_1 / num_2

        if user_choice != answer:
            feedback = "incorrect"
        else:
            feedback = "correct"
        print(feedback)
    # num_questions = int_check(user_choice, low=1)

    if mode == "infinite":
        question_attempt += 1

    num_questions += 1

    # if the user types the exit code they are able to leave the game
    if user_choice == "xxx":
        print("Thank you for your attempt!")

        print()
        break



