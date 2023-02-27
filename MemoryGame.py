import os
import random
import subprocess
import time
from Utils import Screen_cleaner
from Score import add_score
def generate_sequence(difficulty):
    list_of_numbers = random.sample(range(1, 101), difficulty)
    print (list_of_numbers)
    Screen_cleaner(0.7)
    return list_of_numbers
def get_list_from_user(difficulty):
    print ("enter the numbers sequence ")
    list_sequence =[]
    for i in range(difficulty):
        try:
            user_list_input = int(input("\n"))
            list_sequence.append(user_list_input)
        except ValueError:
            print("The provided value is not an integer")
            get_list_from_user(difficulty)
    return list_sequence


def is_list_equal(pc_list, user_list):
    pc_list.sort()
    user_list.sort()
    if pc_list != user_list:
        print('sorry wrong!!, Please try again')
        return False
    else:


        return True
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

    if is_list_equal(generate_sequence(difficulty),get_list_from_user(difficulty))==False:
        get_list_from_user(difficulty)
        print('sorry wrong!!, Please try again')
        exit_Q(difficulty)
        return False
    else:
        print('Congratulations!!')
        exit_Q(difficulty)
        add_score(difficulty)
        return True

