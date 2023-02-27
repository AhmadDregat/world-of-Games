from random import randrange

from Score import add_score


def generate_number(Difficulty):
    x=randrange(1,Difficulty)
    print (x)
    return x

def get_guess_from_user():
    try:
        user_guess = int(input("please enter number\n"))
    except ValueError:
        print("The provided value is not an integer")
        get_guess_from_user()
    return user_guess
def compare_results(secret_number, guess_number):
    if secret_number == guess_number:
        return True
    else:
        return False
def exit_Q (difficulty):
    ask_user = input("""Did you want to play the game again?
            if yes, please enter Y, otherwise press any key to exit.
             """)
    if (ask_user == "Y" or ask_user == "y"):
        print("welcome again:)")
        play(difficulty)
    else:
        print("Goodbye!")
def play(difficulty):
    pc_number = generate_number(difficulty)
    user_guess = get_guess_from_user()
    if compare_results(pc_number,user_guess) == True:
        add_score(difficulty)
        print("Congratulations!!!")
        exit_Q(difficulty)

        return True
    else:
        print("Sorry, Please try again")
        exit_Q(difficulty)
        return False

