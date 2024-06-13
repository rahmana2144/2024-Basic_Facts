import random


def int_check(question, low=None, high=None, exit_code="xxx"):
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


def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


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

Press <enter> for  infinite mode.

Pick your level of difficulty between level's 1-3, 1 being the easiest, 2 being medium, 3 being hardest.

Your questions will vary from Addition, Subtraction, Multiplication, Division or All

Your goal is to answer your questions correctly within your attempts

Good luck!!

    ''')


# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting the game

# Initialise game variables
mode = "regular"
num_questions = 0
question_incorrect = 0
question_correct = 0
quiz_history = []
end_quiz = ""
math_list = ["addition", "subtraction", "multiplication", "division", "all"]

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
    print("You chose infinite mode")

# Choose difficulty level
difficulty = int_check("Choose your difficulty Level (level 1 being easy, Level 2 being medium, Level 3 being "
                       "hard): ",
                       low=1, high=3)

math_type = string_checker("Which type of math equation would you like to do?"
                           "(addition, subtraction, multiplication, division, all)", math_list)

# question loop starts here
while num_questions < question_attempt:

    # Quiz headings
    if mode == "infinite":
        quiz_heading = f"\n ✨✨✨Question  {num_questions + 1}✨✨✨ (Infinite mode) "
    else:
        quiz_heading = f"\n ✨✨✨Question {num_questions + 1} of {question_attempt}✨✨✨"

    print(quiz_heading)

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

    # Makes sure the answer is an integer
    num_3 = num_1 + num_2
    num_4 = num_1 * num_2
    question_list = ["addition question", "subtraction question", "multiplication question", "division question"]
    user_choice = ""
    # Generates what math type they want
    if math_type == "addition":
        question_form = "addition question"
    elif math_type == "subtraction":
        question_form = "subtraction question"
    elif math_type == "multiplication":
        question_form = "multiplication question"
    elif math_type == "division":
        question_form = "division question"
    else:
        question_form = random.choice(question_list)

    # generates the questions
    if question_form == "addition question":
        user_choice = int_check(f"What is {num_1} + {num_2}? ",
                                exit_code="xxx")
        answer = num_1 + num_2

    elif question_form == "subtraction question":
        user_choice = int_check(f"What is {num_3} - {num_2}? ",
                                exit_code="xxx")
        answer = num_1

    elif question_form == "multiplication question":
        user_choice = int_check(f"What is {num_1} x {num_2}? ",
                                exit_code="xxx")
        answer = num_1 * num_2

    else:
        question_form = "division question"
        user_choice = int_check(f"What is {num_4} / {num_2}? ",
                                exit_code="xxx")
        answer = num_1
    if user_choice == "xxx":
        end_quiz = "yes"
        break

    # Adjust questions incorrect / questions correct counters and add results to quiz history
    if user_choice == answer:
        feedback = f"You got the answer correct, it is {answer}"
        history_item = f"Question {num_questions + 1}: You got the answer correct, it is {answer} ."

    else:
        feedback = f"You got the answer incorrect, it was {answer}"
        history_item = f"Question {num_questions + 1}: You got the answer incorrect, it was {answer} ."
        question_incorrect += 1

    # if users are in infinite mode, increase number of questions
    if mode == "infinite":
        question_attempt += 1
    num_questions += 1

    print(feedback)

    # if the user types the exit code they are able to end the quiz
    if end_quiz == "yes":
        print("Thank you for your attempt!")
        break

    # Add round result to quiz history
    history_feedback = f"Question {num_questions}: {feedback}"
    quiz_history.append(history_feedback)

# Quiz loop ends here


# Quiz history / Statistics area

if num_questions > 0:
    # Calculate Statistics
    question_correct = num_questions - question_incorrect
    percent_won = question_correct / num_questions * 100
    percent_lost = question_incorrect / num_questions * 100

    # Output quiz statistics
    print("📊📊📊Quiz Statistics📊📊📊")
    print(f"👍 The Questions you got correct: {percent_won:.2f} \t "
          f"😥 The Questions you got incorrect: {percent_lost:.2f} \t")

    # ask user if they want to see their quiz history and output if its requested
    see_history = yes_no("\nDo you want to see your quiz history? ")
    if see_history == "yes":
        for item in quiz_history:
            print(item)

    print()
    print("Thanks for attempting my quiz.")

# End quiz if user hasn't answered a question
else:
    print("🐔🐔🐔Oops - You chickened out! 🐔🐔🐔")
