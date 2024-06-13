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


# Main routine

print()
print("➕➖ Welcome to Basic Facts Quiz✖️➗")
print()

want_instructions = yes_no("Do you want to read the instructions?")

if want_instructions == "yes":
    instructions()

print("program continues")